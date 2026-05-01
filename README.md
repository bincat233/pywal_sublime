# Pywal for Sublime

This is a modern script for generating Sublime Text (ST4/ST3) color schemes from pywal colors. For the best possible experience, use it with an adaptive theme (e.g., the built-in Adaptive theme).

It automatically maps pywal colors to modern Sublime Text color scheme features and syntax scopes.

## Modernization Features
- Outputs modern ST4 `.sublime-color-scheme` format with variables support for easy tweaking.
- Expanded syntax scope coverage (Markdown, built-in types, UI elements).
- Smart path detection (works with both ST3 and ST4 configurations out of the box).
- CLI arguments support for custom input/output paths.

## Usage

1. Clone/download the repo:
   ```bash
   git clone https://github.com/bincat233/pywal_sublime ~/.config/sublime-text/Packages/pywal_sublime
   ```
2. Copy the script to your `$PATH` for easy access:
   ```bash
   mkdir -p ~/.local/bin
   cp ~/.config/sublime-text/Packages/pywal_sublime/pywal_sublime.py ~/.local/bin/pywal_sublime
   chmod +x ~/.local/bin/pywal_sublime
   ```
3. Set your Sublime Text preferences (`Preferences.sublime-settings`):
   ```json
   {
       "color_scheme": "Packages/User/PyWal.sublime-color-scheme",
       "theme": "Adaptive.sublime-theme"
   }
   ```
4. Run `pywal_sublime.py` whenever you run `wal` (e.g., by using the `wal -o` flag):
   ```bash
   wal -i /path/to/wallpaper.jpg -o pywal_sublime
   ```

### Advanced Usage

You can specify custom paths for the input `colors.json` and output color scheme:

```bash
pywal_sublime --path ~/.cache/wal/custom_colors.json --out ~/Desktop/CustomWal.sublime-color-scheme
```
