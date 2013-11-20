import re

def removeWhitespaces(text):
    return re.sub(r'\s+', ' ', text).strip()

