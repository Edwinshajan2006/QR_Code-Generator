import qrcode

def generate_qrcode(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print("QR Code saved as", filename)

data = input("Enter text or URL: ")
file = input("Enter file name (example: qr.png): ")

generate_qrcode(data, file)
