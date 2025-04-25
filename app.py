from flask import Flask, render_template, request

from vcard_utils import generate_vcard_qr
from generate_card import generate_card_image
from ai_templates import get_ai_templates
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form
        files = request.files

        name = data.get("name")
        title = data.get("title")
        company = data.get("company")
        email = data.get("email")
        phone = data.get("phone")
        website = data.get("website")
        address = data.get("address")
        font_name = data.get("font_name") or "arial.ttf"
        layout = data.get("layout") or "default"
        # colors = "#000000"  # Removed for now, not used

        logo_path = save_file(files.get("logo"))
        profile_path = save_file(files.get("profile_pic"))
        background_path = save_file(files.get("background"))

        # Generate Business Card Image
        card_path = generate_card_image(
            name=name,
            title=title,
            company=company,
            email=email,
            phone=phone,
            website=website,
            font_name=font_name,
            layout=layout,
            logo_path=logo_path,
            profile_path=profile_path,
            background_path=background_path
        )

        # Generate QR Code with vCard data
        qr_path = generate_vcard_qr(name, company, email, phone, website, address)

        return render_template("index.html", card_path=card_path, qr_path=qr_path,
                               templates=get_ai_templates(), dark_mode=data.get("theme") == "dark")

    return render_template("index.html", templates=get_ai_templates())


def save_file(file):
    if file and file.filename:
        upload_folder = os.path.join("static", "uploads")
        os.makedirs(upload_folder, exist_ok=True)
        path = os.path.join(upload_folder, file.filename)
        try:
            file.save(path)
            return path
        except Exception as e:
            print("Error saving file:", e)
            return None
    return None


if __name__ == "__main__":
    app.run(debug=True)
