from PIL import Image, ImageDraw, ImageFont


def code_to_image(code):
    # Monospaced font path (replace with your font path if needed)
    font_path = "arial.ttf"
    font_size = 18
    line_height = 22

    # Calculate the image height based on the number of lines
    num_lines = code.count('\n') + 1
    image_height = num_lines * line_height + (line_height * 2)

    # Create an image with a white background
    image_width = 1080
    image = Image.new("RGB", (image_width, image_height), "#dddddd")
    draw = ImageDraw.Draw(image)

    # Load a monospaced font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    text_color = "#404040"
    draw.text((20, line_height), code, font=font, fill=text_color)

    image.save("code_image.png")


# Usage
your_python_code = open(0, encoding='utf8').read()
code_to_image(your_python_code)
