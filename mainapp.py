

import flet
from flet import (animation, Column, Theme,  Icon, Row, Text, icons, TextField, SnackBar, transform,
                  OutlinedButton, Page, ElevatedButton, NavigationRail, NavigationRailDestination, VerticalDivider, FilePicker, FilePickerResultEvent)
from booksGridView import booksGridView
from bookSingleView import bookSingleView
from addBookView import addBookView
from settingsView import settingsView
from loadingView import loadingView
from styles import determine_button_style
from utils import copy_image_into_assets_directory
from database import get_books, update_fav_by_id, get_favs, add_book, search_by_title


from time import sleep


def main(page: Page):

    # set page properties


    page.title = "Library - Home"
    page.window_min_width = 700
    page.window_min_height = 700
    page.window_max_width = page.window_width
    page.window_max_height = page.window_height
    page.vertical_alignment = "center"
    page.fonts = {
        "Raleway": "Raleway-Black.ttf",
        "JosefinSans": "fonts/JosefinSans-Regular.ttf",
        "National Cartoon": "fonts/National-Cartoon.ttf",
        "Playfair": "fonts/PlayfairDisplay-Black.ttf",
        "Roboto": "fonts/Roboto-Black.ttf",
        "Lato": "fonts/Lato-Black.ttf",
        "Montserrat": "fonts/Montserrat-Black.ttf",
        "WorkSans": "fonts/WorkSans-Regular.ttf"
    }

    page.theme = Theme(font_family="Raleway", color_scheme_seed='blue')
    page.dark_theme = Theme(
        font_family=page.theme.font_family, color_scheme_seed='blue')
    page.theme_mode = 'light'

    # changing route functions start

    def change_page(e):
        routes = {0: home_page, 1: fav_page, 2: add_book_page, 3: setting_page}
        routes[e.control.selected_index]()
        page.update()

    def fav_page():
        fav_books = get_favs()
        mainRow.controls.pop(-1)
        gv = booksGridView(fav_books, handleFavClicked,
                           handleTitleClicked, no_book_msg="You don't have a favorite book")
        mainRow.controls.append(Column([Text("My favorite books", style="displayMedium"), gv],
                                       alignment="start", expand=True))
        page.update()

    def home_page():
        mainRow.controls.pop(-1)
        books = get_books()
        gv = booksGridView(books,
                           handleFavClicked, handleTitleClicked)
        mainRow.controls.append(Column([Text("Books List", style="displayMedium"), Row([searchfield, OutlinedButton(style=determine_button_style(page.theme_mode, 'secondary'),
                                                                                                                    text="Search", on_click=handleSearchBookClicked, )]), gv],
                                       alignment="start", expand=True))
        page.update()

    def add_book_page():
        mainRow.controls.pop(-1)
        add_book_view, input_boxes = addBookView()
        page.overlay.append(pick_files_dialog)
        upload_image_btn = ElevatedButton(
            "Book Image",
            icon=icons.UPLOAD_FILE,
            on_click=lambda _: pick_files_dialog.pick_files(
                allow_multiple=False,
                allowed_extensions=['jpg', 'png']
            ),
        )
        input_boxes.append(selected_file)
        add_book_view.content.controls.append(Row(
            controls=[upload_image_btn, selected_file],
            alignment="center",

        ))
        add_book_view.content.controls.append(Row(
            [
                OutlinedButton(
                    text="Add Book", on_click=handleAddBookClicked, data=input_boxes)

            ],
            alignment="center",

        ),
        )
        mainRow.controls.extend([add_book_view])

        page.update()

    def setting_page():
        mainRow.controls.pop(-1)
        lv = settingsView(theme_changed, font_dropdown_change, color_scheme_seed_dropdown_change, fonts=page.fonts,
                          current_font_family=page.theme.font_family, current_color_scheme_seed=page.theme.color_scheme_seed, current_them_mode=page.theme_mode)
        mainRow.controls.append(lv)
        page.update()
    # changing route functions end

    # settings functions start

    def theme_changed(e):
        page.dark_theme.font_family = page.theme.font_family
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        e.control.label = "Light Mode" if page.theme_mode == "light" else "Dark Mode"
        page.update()

    def color_scheme_seed_dropdown_change(e):
        page.theme.color_scheme_seed = e.control.value
        page.dark_theme.color_scheme_seed = e.control.value
        page.update()

    def font_dropdown_change(e):
        page.theme.font_family = e.control.value
        if page.theme_mode == "dark":
            page.dark_theme.font_family = page.theme.font_family
        page.update()

    # settings functions end

    # button handler functions start

    def handleAddBookClicked(e):

        title = e.control.data[0].value.strip()
        author = e.control.data[1].value.strip()
        country = e.control.data[2].value.strip()
        language = e.control.data[3].value.strip()
        pages = e.control.data[4].value.strip()
        year = e.control.data[5].value.strip()
        link = e.control.data[6].value.strip()
        imageLink = selected_file.value

        if any([field.value == '' for field in e.control.data]):
            page.snack_bar = SnackBar(Text("Please check your inputs"))
            page.snack_bar.open = True
            page.update()

        else:
            msg, signal = add_book(title, author, country, imageLink,
                                   language, link, pages, year)
            if signal:
                copy_image_into_assets_directory(selected_file.data)
            page.snack_bar = SnackBar(
                Text(msg))

            page.snack_bar.open = True
            page.update()

    def handleSearchBookClicked(e):
        title = searchfield.value.strip()
        if title != "":
            searched_books = search_by_title(title)
            mainRow.controls.pop(-1)
            gv = booksGridView(
                searched_books, handleFavClicked, handleTitleClicked)
            mainRow.controls.append(Column([Text(f"Searched result for {title}", style="displayMedium"), Row([searchfield, OutlinedButton(
                text="Search", on_click=handleSearchBookClicked, style=determine_button_style(page.theme_mode, 'secondary')), OutlinedButton(style=determine_button_style(page.theme_mode, 'primary'),
                                                                                                                                             text="Go Home", on_click=handleBackClicked)]), gv],
                alignment="start", expand=True))
            searchfield.value = ''
            page.update()

    def handleFavClicked(e):
        update_fav_by_id(e.control.data['_id'], e.control.data['fav'])
        e.control.data['fav'] = not e.control.data['fav']
        e.control.tooltip = "remove it from favorites" if e.control.data[
            'fav'] else "add it to favorites"
        e.control.icon_color = "pink600" if e.control.icon_color == 'black' else 'black'
        e.control.update()

    def handleBackClicked(e):
        rail.selected_index = 0
        home_page()

    def handleTitleClicked(e):
        mainRow.controls.pop(-1)
        gv = bookSingleView(e.control.data, handleFavClicked,
                            open_url, handleBackClicked)
        mainRow.controls.append(gv)
        page.update()

    def open_url(e):
        page.launch_url(str(e.control.data).strip())

    def pick_files_result(e: FilePickerResultEvent):
        selected_file.value = (
            ", ".join(map(lambda f: f.name, e.files)
                      ) if e.files else "Cancelled!"
        )
        selected_file.data = (
            ", ".join(map(lambda f: f.path, e.files)
                      ) if e.files else "Cancelled!"
        )
        selected_file.update()

    # button handler functions ends

    rail = NavigationRail(
        selected_index=0,
        label_type="all",
        # extended=True,
        min_width=100,
        min_extended_width=400,
        animate_scale=animation.Animation(600, "bounceOut"),
        # leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
        leading=Text(
            value="Library",
            size=24,

            weight="bold",
            italic=True,
            text_align="center"

        ),

        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.BOOK, label="Books",
            ),
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="My Favorites"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.CREATE),
                selected_icon_content=Icon(icons.CREATE),
                label="Add Book",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ],
        on_change=change_page,
    )

    selected_file = Text()
    pick_files_dialog = FilePicker(on_result=pick_files_result)
    books = get_books()
    booksGrid = booksGridView(books, handleFavClicked, handleTitleClicked, grid_size=(
        page.window_width / (page.window_height / 170)))
    searchfield = TextField(height=40, label="Search by title name",
                            text_size=12, on_submit=handleSearchBookClicked)
    mainRow = Row([
        rail,
        VerticalDivider(width=1),
        Column([Text("Books List", style="displayMedium"), Row([searchfield, OutlinedButton(
            text="Search", on_click=handleSearchBookClicked, style=determine_button_style(page.theme_mode, 'secondary'))]), booksGrid],
            alignment="start", expand=True),
    ],
        expand=True,)

    # loading starts
    loadingRow = loadingView()
    logo, progress_bar, loading_text = loadingRow.controls
    loadingBanner = Row(
        [Text("Library App using Flet and Mongo DB", style="titleLarge")], alignment="center")
    page.add(
        loadingBanner,
        loadingRow,

    )
    for i in range(0, 30):
        progress_bar.value = i * 0.04
        logo.offset = transform.Offset(0, 0)
        sleep(0.1)

        loading_text.value = "100 %" if i * 4 > 100 else f"{i * 4} %"
        page.update()
    page.controls.remove(loadingBanner)
    page.controls.remove(loadingRow)
    # loading ends

    page.add(
        mainRow,

    )
    page.update()


flet.app(target=main, assets_dir="assets")
