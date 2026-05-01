#! /usr/bin/env python3
import json
import os
import argparse
from pathlib import Path

def make_rule(name, scope, **kwargs):
    """Helper function for generating color scheme entries"""
    return {"name": name, "scope": scope, **kwargs}

def main():
    parser = argparse.ArgumentParser(description="Generate Sublime Text color scheme from pywal colors.")
    parser.add_argument("--path", type=str, help="Custom path to colors.json")
    parser.add_argument("--out", type=str, help="Custom output path for the color scheme")
    args = parser.parse_args()

    # Determine paths
    home = Path.home()
    wal_path = Path(args.path) if args.path else home / ".cache/wal/colors.json"
    
    # Standard Sublime Text config directory
    st_config_dir = home / ".config/sublime-text"
    # Fallback for ST3 if directory exists and ST4 doesn't (though ST4 is standard now)
    if not st_config_dir.exists():
        st_config_dir = home / ".config/sublime-text-3"

    theme_out_path = Path(args.out) if args.out else st_config_dir / "Packages/User/PyWal.sublime-color-scheme"

    if not wal_path.exists():
        print(f"Error: {wal_path} not found. Make sure pywal has generated colors.")
        return

    with open(wal_path) as f:
        wal = json.load(f)

    colors = {f"color{i}": wal['colors'][f'color{i}'] for i in range(16)}
    special = wal['special']

    # Modern .sublime-color-scheme format
    # Using 'variables' allows for easier manual tweaking later
    scheme = {
        "name": "Pywal",
        "author": "pywal_sublime",
        "variables": {
            **colors,
            "background": special['background'],
            "foreground": special['foreground'],
            "caret": special['cursor'],
        },
        "globals": {
            "background": "var(background)",
            "foreground": "var(foreground)",
            "caret": "var(caret)",
            "invisibles": "var(color1)",
            "line_highlight": "var(color2)",
            "selection": "var(color6)",
            "selection_border": "var(color6)",
            "misspelling": "var(color5)",
            "shadow": "var(color0)",
            "active_guide": "var(color4)",
            "stack_guide": "var(color3)",
            "highlight": "var(color5)",
            "find_highlight": "var(color3)",
            "find_highlight_foreground": "var(color15)",
        },
        "rules": [
            make_rule("Comment", "comment", foreground="var(color2)"),
            make_rule("String", "string", foreground="var(color4)"),
            make_rule("Number", "constant.numeric", foreground="var(color5)"),
            make_rule("Built-in constant", "constant.language", foreground="var(color5)"),
            make_rule("User-defined constant", "constant.character, constant.other", foreground="var(color5)"),
            make_rule("Variable", "variable", foreground="var(foreground)"),
            make_rule("Keyword", "keyword, storage.type, storage.modifier", foreground="var(color3)"),
            make_rule("Storage", "storage", foreground="var(color3)"),
            make_rule("Storage type", "storage.type", foreground="var(color6)", font_style="italic"),
            make_rule("Class name", "entity.name.class", foreground="var(color1)", font_style="italic"),
            make_rule("Inherited class", "entity.other.inherited-class", foreground="var(color1)", font_style="italic"),
            make_rule("Function name", "entity.name.function", foreground="var(color1)", font_style="italic"),
            make_rule("Function argument", "variable.parameter", foreground="var(color6)"),
            make_rule("Tag name", "entity.name.tag", foreground="var(color3)"),
            make_rule("Tag attribute", "entity.other.attribute-name", foreground="var(color1)"),
            make_rule("Library function", "support.function", foreground="var(color6)"),
            make_rule("Library constant", "support.constant", foreground="var(color6)"),
            make_rule("Library class/type", "support.class, support.type", foreground="var(color6)", font_style="italic"),
            make_rule("Invalid", "invalid", foreground="var(foreground)", background="var(color5)"),
            make_rule("Markup Quote", "markup.quote", foreground="var(color4)"),
            make_rule("Markup Heading", "markup.heading", foreground="var(color1)"),
            make_rule("Markup Bold", "markup.bold", font_style="bold"),
            make_rule("Markup Italic", "markup.italic", font_style="italic"),
            make_rule("Markup Link", "markup.underline.link", foreground="var(color2)"),
        ]
    }

    # Ensure output directory exists
    theme_out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(theme_out_path, 'w') as f:
        json.dump(scheme, f, indent=4)
    
    print(f"Successfully generated {theme_out_path}")

if __name__ == "__main__":
    main()
