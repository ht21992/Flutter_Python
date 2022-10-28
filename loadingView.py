from flet import ProgressBar, Image, Row, animation, transform, Text


def loadingView():
    pb = ProgressBar(width=300, height=10)
    img = Image(
        src=f"/icons/logo.png",
        width=100,
        height=100,
        fit="contain",
        offset=transform.Offset(-2, 0),
        animate_offset=animation.Animation(1000),
    )

    loadingRow = Row(

        [
            img,
            pb,
            Text(0)

        ],
        alignment="center",
    )

    return loadingRow
