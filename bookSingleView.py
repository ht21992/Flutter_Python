

from flet import (Card, Column, Container,  Row, Text, icons, IconButton, ListTile,
                  OutlinedButton, Image, border_radius)

from styles import determine_button_style


def bookSingleView(data, handleFavClicked, open_url, handleBackClicked, current_theme='light'):
    if data['fav']:
        FavButton = IconButton(
            icon=icons.FAVORITE,
            icon_color="pink600",
            icon_size=30,
            tooltip="remove it from favorites",
            on_click=handleFavClicked,
            data=data
        )
    else:

        FavButton = IconButton(
            icon=icons.FAVORITE,
            icon_color="black",
            icon_size=30,
            tooltip="add it to favorites",
            on_click=handleFavClicked,
            data=data
        )

    bookView = Container(content=Card(
        content=Container(
            content=Column(
                [
                    ListTile(
                        title=Image(
                            src=f"{data['imageLink']}",
                            height=230,
                            fit="cover",
                            repeat="noRepeat",
                            border_radius=border_radius.all(10),
                        ),
                        subtitle=Column([Row([
                            FavButton,
                            Text(f"{data['title']}",
                                 size=24,
                                 weight="bold",

                                 ),
                        ]), Row([
                                Text("Author: ",
                                     size=18,
                                     weight="bold",

                                     ),
                                Text(f"{data['author']}",
                                     size=18,

                                     ),
                                ]), Row([
                                    Text("Country: ",
                                         size=18,
                                         weight="bold",

                                         ),
                                    Text(f"{data['country']}",
                                         size=18,

                                         ),
                                ]), Row([
                                        Text("Language: ",
                                             size=18,
                                             weight="bold",

                                             ),
                                        Text(f"{data['language']}",
                                             size=18,

                                             ),
                                        ]), Row([
                                            Text("Pages: ",
                                                 size=18,
                                                 weight="bold",

                                                 ),
                                            Text(f"{data['pages']}",
                                                 size=18,

                                                 ),
                                        ]),
                            Row([
                                Text("Year: ",
                                     size=18,
                                     weight="bold",


                                     ),
                                Text(f"{data['year']}",
                                     size=18,

                                     ),
                            ])])
                    ),
                    Row(
                        [OutlinedButton(style=determine_button_style(current_theme, 'secondary'),
                                        text="Open Wiki", on_click=open_url, data=data['link']), OutlinedButton(style=determine_button_style(current_theme, 'primary'),
                                                                                                                text="Go Home", on_click=handleBackClicked)],
                        alignment="end",
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    ), expand=1, padding=20)

    return bookView
