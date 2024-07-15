import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=10,)
qr.add_data("https://koushikkoush.github.io/Portfolio/")
qr.make(fit=True)
img=qr.make_image(fill_color="darkblue",back_color="lightgray")
img.save("Portfolio.png")