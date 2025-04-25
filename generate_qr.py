import qrcode
from qrcode.constants import ERROR_CORRECT_H

def generate_qr_code(data, output_path="static/qr_code.png", box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generates a QR code with enhanced customization.
    
    Args:
        data (str): The data to encode in the QR code.
        output_path (str): Where to save the QR code image.
        box_size (int): Size of each box in pixels.
        border (int): Thickness of the border (minimum is 4).
        fill_color (str): Color of the QR code dots.
        back_color (str): Background color of the QR code.
    
    Returns:
        str: Path to the saved QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_path)
    return output_path

