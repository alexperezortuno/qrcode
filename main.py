import io

import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SolidFillColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer
from PIL import Image, ImageDraw

factory = qrcode.image.svg.SvgPathImage
code = "https://facebook.com"

qr_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=40,
    border=4,
    image_factory=factory
)
qr_code.add_data(code)
qr_code.make(fit=True)

img = qr_code.make_image()
img.save("wifi.svg")

qr_code_png = qr_code.make_image()
qr_code_png.save("wifi.png")

qr = qrcode.QRCode()
qr.add_data(code)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(code)

img_1 = qr.make_image(image_factory=StyledPilImage,
                      module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage,
                      color_mask=RadialGradiantColorMask(
                          back_color=(216, 64, 168),
                          center_color=(29, 25, 210),
                          edge_color=(123, 44, 189),
                      ))
img_3 = qr.make_image(image_factory=StyledPilImage,
                      module_drawer=GappedSquareModuleDrawer())
img_1.save('img_1.png')
img_2.save('img_2.png')
img_3.save('img_3.png')


def style_eyes(img):
    img_size = img.size[0]
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((40, 40, 110, 110), fill=255)
    draw.rectangle((img_size - 110, 40, img_size - 40, 110), fill=255)
    draw.rectangle((40, img_size - 110, 110, img_size - 40), fill=255)
    return mask


qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(code)

qr_eyes_img = qr.make_image(image_factory=StyledPilImage,
                            eye_drawer=RoundedModuleDrawer(radius_ratio=1.2),
                            color_mask=SolidFillColorMask(back_color=(255, 255, 255),
                                                          front_color=(255, 110, 0)))

qr_img = qr.make_image(image_factory=StyledPilImage,
                       module_drawer=CircleModuleDrawer(),
                       color_mask=SolidFillColorMask(front_color=(59, 89, 152)),
                       embeded_image_path="./assets/facebook.png")

mask = style_eyes(qr_img)
final_img = Image.composite(qr_eyes_img, qr_img, mask)
final_img.save('qr.png')
