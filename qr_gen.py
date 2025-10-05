# pip install qrcode[pil]
import qrcode

# 1) Si vous utilisez un domaine personnalisé :
#TARGET_URL = "https://montadocuments.tn"

# 2) Si vous commencez sur GitHub Pages sans domaine :
TARGET_URL = "https://montadocuments.github.io"

qr = qrcode.QRCode(
    version=4,  # auto-ajuster si besoin
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)
qr.add_data(TARGET_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_montadocuments.png")
print("QR code généré : qr_montadocuments.png ->", TARGET_URL)
