
import re


def extract_multiplier(text):
    """
    Mengambil angka multiplier dari teks OCR.
    Contoh: 2.50x menjadi 2.50
    """

    if not text:
        return None

    text = text.lower().replace(",", ".")

    match = re.search(r"(\d+(?:\.\d+)?)\s*x", text)

    if not match:
        return None

    try:
        value = float(match.group(1))

        if value <= 0:
            return None

        return value

    except ValueError:
        return None
