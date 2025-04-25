from PIL import Image, ImageDraw, ImageFont
import os

def paste_image(card, image_path, position, size):
    if image_path and os.path.exists(image_path):
        try:
            img = Image.open(image_path).convert("RGBA").resize(size)
            card.paste(img, position, img)
        except Exception as e:
            print(f"[ERROR] Unable to paste image: {e}")
    else:
        print(f"[WARN] Image not found: {image_path}")

def generate_card_image(
    name, title, company, email, phone, website,
    logo_path=None, profile_path=None, background_path=None,
    font_name="arial.ttf", colors=None, layout=1
):
    width, height = 1000, 600
    bg_color = colors["bg"] if colors and "bg" in colors else (20, 30, 50)
    text_color = colors["text"] if colors and "text" in colors else (255, 255, 255)

    card = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(card)

    # Background image
    if background_path and os.path.exists(background_path):
        bg = Image.open(background_path).convert("RGBA").resize((width, height))
        card.paste(bg, (0, 0), bg)

    # Fonts
    try:
        font_large = ImageFont.truetype(font_name, 48)
        font_medium = ImageFont.truetype(font_name, 34)
        font_small = ImageFont.truetype(font_name, 26)
    except:
        font_large = font_medium = font_small = ImageFont.load_default()

    # Logo (top-left)
    paste_image(card, logo_path, (40, 40), (100, 100))

    # Profile (top-right)
    paste_image(card, profile_path, (width - 190, 40), (150, 150))

    # Centered vertical text on left half
    text_x = 180
    start_y = 200
    spacing = 50

    draw.text((text_x, start_y), name, font=font_large, fill=text_color)
    start_y += spacing
    draw.text((text_x, start_y), title, font=font_medium, fill=text_color)
    start_y += spacing
    draw.text((text_x, start_y), company, font=font_medium, fill=text_color)
    start_y += spacing + 10
    draw.text((text_x, start_y), f"Email: {email}", font=font_small, fill=text_color)
    start_y += spacing - 10
    draw.text((text_x, start_y), f"Phone: {phone}", font=font_small, fill=text_color)
    start_y += spacing - 10
    draw.text((text_x, start_y), f"Website: {website}", font=font_small, fill=text_color)

    # Save
    output_dir = "static/generated"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "final_business_card.png")
    card.save(output_path)
    print(f"[✔] Card saved: {output_path}")
    return output_path
