import re

def normalize_title(title: str | None):
    if not title:
        return "@PdfKutubxonaBot"

    title = re.sub(r"(http[s]?://\S+|t\.me/\S+|@\S+)", "@PdfKutubxonaBot", title)

    if len(title.strip()) < 3:
        return "@PdfKutubxonaBot"

    return title.strip()