
from flet import ListView, Text, Switch, Dropdown, dropdown


def settingsView(theme_changed, font_dropdown_change, color_scheme_seed_dropdown_change, fonts: dict, current_font_family: str, current_color_scheme_seed: str, current_them_mode: str) -> ListView:
    lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    settings_label = Text("Settings", style="displayMedium")
    theme_switch = Switch(label=f"{current_them_mode.title()} Mode",
                          value=False if current_them_mode == "light" else True, on_change=theme_changed)
    fonts_label = Text("Font", style="bodyMedium")
    fonts_dropdown = Dropdown(
        on_change=font_dropdown_change,
        hint_text=f"Current Font:  {current_font_family}",
        options=[
            dropdown.Option(font) for font in fonts.keys()
        ],
    )
    scheme_color = Text("Scheme Color", style="bodyMedium")
    scheme_colors_dropdown = Dropdown(
        on_change=color_scheme_seed_dropdown_change,
        hint_text=f"Current Color:  {current_color_scheme_seed}",
        options=[
            dropdown.Option(color) for color in ['blue', 'red', 'pink', 'yellow', 'purple', 'orange']
        ],
    )
    lv.controls.extend([settings_label, theme_switch,
                        fonts_label, fonts_dropdown, scheme_color, scheme_colors_dropdown])

    return lv
