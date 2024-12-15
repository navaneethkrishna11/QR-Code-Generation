import qrcode
def generate_qr_code(url, filename='website.png'):
    qr = qrcode.QRCode(
        version=1,  
        box_size=10,  
        border=5  
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(filename)
    return filename
if __name__ == "__main__":
    website_url = "url link"
    qr_code_path = generate_qr_code(website_url)
    print(f"QR Code generated: {qr_code_path}")
