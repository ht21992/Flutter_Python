from flet import ButtonStyle, colors


ButtonStyles = {'light': {'primary': {'color': {
    "hovered": colors.WHITE,
    "": colors.BLUE,
}, 'bgcolor': {"hovered": colors.BLUE,
               "": colors.WHITE, }}, 'secondary': {'color': {
                   "hovered": colors.WHITE,
                   "": colors.GREEN,
               }, 'bgcolor': {"hovered": colors.GREEN,
                              "": colors.WHITE, }}},

    'dark': {'primary': {'color': {
        "hovered": colors.BLACK,
        "": colors.BLUE,
    }, 'bgcolor': {"hovered": colors.BLUE,
                   "": colors.BLACK12, }}, 'secondary': {'color': {
                       "hovered": colors.BLACK,
                       "": colors.GREEN,
                   }, 'bgcolor': {"hovered": colors.GREEN,
                                  "": colors.BLACK12, }}},

}


def determine_button_style(theme_mode: str, button_variant: str) -> ButtonStyle:

    btn_style = ButtonStyle(ButtonStyles[theme_mode][button_variant]
                            ['color'], ButtonStyles[theme_mode][button_variant]['bgcolor'])
    # print(btn_style)
    return btn_style
