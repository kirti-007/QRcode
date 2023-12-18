import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Size of each box in the QR code
    border=1,     # Border size around the QR code
)

# Add data to the QR code
data = "https://www.youtube.com/channel/UCLUtl643JXl1Jew4eaVnhtQ"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="whitesmoke")

img.save("my_youtube.png")


