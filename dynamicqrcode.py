# import qrcode
# from PIL import Image, ImageDraw, ImageFont
# upi_id =  '7034130100@ybl'


# phonepe_url = f"upi://pay?pa={upi_id}&pn=Dett&mc=1234&am=100&cu=INR"
# phonepe_qr = qrcode.make(phonepe_url)

# phonepe_qr.save("phonepe_qr.png")


# phonepe_qr.show()


import qrcode
from PIL import Image
order_id = "DETT-1234"
upi_id = '7034130100@ybl'
amount = 100 
phonepe_url = f"upi://pay?pa={upi_id}&pn=Dett&mc=1234&am={amount}&cu=INR"

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(phonepe_url)
qr.make(fit=True)

qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

logo_path = "D:\Practice\python dynamic qr code\logo.png"
try:
    logo = Image.open(logo_path)
    qr_width, qr_height = qr_img.size
    logo_size = qr_width // 4 
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_img.paste(logo, pos, mask=logo)

except FileNotFoundError:
    print("⚠️ Logo file not found. QR code will be generated without a logo.")
    
    
qr_img.show()