
from flet import (Card, Column, Container, Text, TextButton, icons, IconButton, ButtonStyle, colors,
                  Image, border_radius,  GridView)


def booksGridView(books: object, handleFavClicked, handleTitleClicked, grid_size: float = 300, no_book_msg="Nothing Found"):

    gridview = GridView(
        expand=True, max_extent=grid_size, child_aspect_ratio=1,)
    if (books.count() == 0):
        gridview = Text(no_book_msg,
                        size=18,
                        weight="bold",
                        color="red"
                        )
        return gridview

    for book in books:
        book_details = f"Author: {book['author']}\nCountry: {book['country']}\nLanguage: {book['language']}\nYear: {book['year']}\nPages: {book['pages']}"
        if book['fav']:

            FavButton = IconButton(
                icon=icons.FAVORITE,
                icon_color="pink600",
                icon_size=20,
                tooltip="remove it from favorites",
                on_click=handleFavClicked,
                data=book
            )
        else:

            FavButton = IconButton(
                icon=icons.FAVORITE,
                icon_color="black",
                icon_size=20,
                tooltip="add it to favorites",
                on_click=handleFavClicked,
                data=book
            )

        gridview.controls.append(
            Card(
                content=Container(



                    content=Column(

                        [
                            Image(
                                src=f"{book['imageLink']}",
                                width=1000,
                                height=130,
                                fit="cover",
                                repeat="noRepeat",
                                border_radius=border_radius.all(10),
                            ),


                            TextButton(content=Text(value=f"{book['title']}", size=12),
                                       on_click=handleTitleClicked,
                                       tooltip=book_details,
                                       data=book,
                                       style=ButtonStyle(
                                color={
                                    "hovered": colors.BLACK,
                                    "": colors.BLUE,
                                },
                                overlay_color={"": colors.WHITE, }


                            )
                            ),
                            FavButton,

                        ],
                        spacing=0,

                    ),

                ),

            )
        )

    return gridview
