from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size)
        img.save(output_path)
def rotate_image(input_path, output_path, angle):
    with Image.open(input_path) as img:
        img = img.rotate(angle)
        img.save(output_path)