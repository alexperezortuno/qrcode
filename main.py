import io

import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SolidFillColorMask, SquareGradiantColorMask, \
    HorizontalGradiantColorMask, VerticalGradiantColorMask, ImageColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer, \
    VerticalBarsDrawer, HorizontalBarsDrawer
from PIL import Image, ImageDraw

factory = qrcode.image.svg.SvgPathImage
code = "WIFI:S:WIFI_NAME;T:WPA;P:WIFI_PASSWORD;H:;"

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
img.save("img_wifi.svg")

qr_code_png = qr_code.make_image()
qr_code_png.save("img_wifi.png")

qr = qrcode.QRCode()
qr.add_data(code)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(code)

img_rounded = qr.make_image(image_factory=StyledPilImage,
                            module_drawer=RoundedModuleDrawer())

img_gapped = qr.make_image(image_factory=StyledPilImage,
                           module_drawer=GappedSquareModuleDrawer())

img_circle = qr.make_image(image_factory=StyledPilImage,
                           module_drawer=CircleModuleDrawer())

img_vertical_bars = qr.make_image(image_factory=StyledPilImage,
                                  module_drawer=VerticalBarsDrawer())

img_horizontal_bars = qr.make_image(image_factory=StyledPilImage,
                                    module_drawer=HorizontalBarsDrawer())

img_solids = qr.make_image(image_factory=StyledPilImage,
                           color_mask=SolidFillColorMask())
img_radial = qr.make_image(image_factory=StyledPilImage,
                           color_mask=RadialGradiantColorMask(
                               back_color=(216, 64, 168),
                               center_color=(29, 25, 210),
                               edge_color=(123, 44, 189),
                           ))
img_square = qr.make_image(image_factory=StyledPilImage,
                           color_mask=SquareGradiantColorMask(
                               back_color=(255, 255, 255),
                               center_color=(29, 25, 210),
                               edge_color=(123, 44, 189),
                           ))
img_horizontal_gradient = qr.make_image(image_factory=StyledPilImage,
                                        color_mask=HorizontalGradiantColorMask(
                                            back_color=(255, 255, 255),
                                            left_color=(29, 25, 210),
                                            right_color=(123, 44, 189),
                                        ))
# img_color_mask = qr.make_image(image_factory=StyledPilImage,
#                                module_drawer=ImageColorMask())

img_rounded.save('img_rounded.png')
img_radial.save('img_radial.png')
img_gapped.save('img_gapped.png')
img_circle.save('img_circle.png')
img_vertical_bars.save('img_vertical_bars.png')
img_horizontal_bars.save('img_horizontal_bars.png')
img_solids.save('img_solids.png')
img_square.save('img_square.png')
img_horizontal_gradient.save('img_horizontal_gradient.png')
# img_color_mask.save('img_color_mask.png')


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

qr_eyes_img.save('img_qr_eyes.png')

qr_img = qr.make_image(image_factory=StyledPilImage,
                       module_drawer=CircleModuleDrawer(),
                       color_mask=SolidFillColorMask(front_color=(59, 89, 152)),
                       embeded_image_path="./assets/wifi.png")
qr_img.save('img_qr.png')

mask = style_eyes(qr_img)
final_img = Image.composite(qr_eyes_img, qr_img, mask)
final_img.save('img_masked.png')
