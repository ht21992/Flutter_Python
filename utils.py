import shutil


def copy_image_into_assets_directory(src_dir):
    original = src_dir
    target = "./assets/images/"
    shutil.copy(original, target)
