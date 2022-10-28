

from flet import Text, border_radius, Row, Container, Column, TextField


def addBookView():
    fields = {'title': {'label': 'title', 'width': 500},
              'author': {'label': 'author', 'width': 500},
              'country': {'label': 'country', 'width': 245},
              'language': {'label': 'language', 'width': 245},
              'pages': {'label': 'pages', 'width': 245},
              'year': {'label': 'year', 'width': 245},
              'link': {'label': 'link', 'width': 500},
              }

    input_boxes = []

    for f in fields.values():
        input_boxes.append(
            TextField(label=f['label'].title(), text_size=12, width=f['width']))

    view = Container(

        border_radius=border_radius.all(20),

        content=Column(
            controls=[
                Row(controls=[Text("Add a New Book",  style="displayMedium",
                                   size=32,
                                   italic=True,
                                   text_align="center")]),
                Row(
                    controls=[input_boxes[0]],



                ),
                Row(
                    controls=[input_boxes[1]],

                ),
                Row(
                    controls=input_boxes[2:4],


                ),
                Row(
                    controls=input_boxes[4:6],

                ),

                Row(
                    controls=[input_boxes[6]],

                ),



            ]
        )
    )

    return view, input_boxes
