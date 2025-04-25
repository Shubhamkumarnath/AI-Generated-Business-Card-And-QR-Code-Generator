import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyCxCX9vD9HxuHfQCUfYlIHHT8Hnfsy1ClQ")

# Initialize once to reuse
model = genai.GenerativeModel("gemini-pro")

def get_ai_suggestions(job_title):
    prompt = (
        f"Suggest a modern color scheme (two distinct hex colors) and a professional font name "
        f"for a business card for a {job_title}. "
        f"Respond strictly in the following format:\n"
        f"Colors: #HEX1, #HEX2\nFont: Font Name"
    )

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Defaults in case parsing fails
        colors = "#000000, #FFFFFF"
        font = "Arial"

        for line in text.splitlines():
            if line.lower().startswith("colors:"):
                colors = line.split(":", 1)[1].strip()
            elif line.lower().startswith("font:"):
                font = line.split(":", 1)[1].strip()

        return colors, font

    except Exception as e:
        print("[AI] Error getting suggestions:", e)
        return "#000000, #FFFFFF", "Arial"

def get_background_description(job_title):
    prompt = (
        f"Suggest a simple, elegant background design idea for a business card for a {job_title}. "
        f"Keep it modern, minimal, and professional."
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("[AI] Error getting background idea:", e)
        return "A soft gradient with subtle geometric patterns."
