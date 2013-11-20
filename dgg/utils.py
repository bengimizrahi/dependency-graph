import re
import textwrap


def removeWhitespaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def convertToColumnText(text, width):
    return textwrap.fill(text, width=width)

def removeWhitespacesAndColumnizeDictValues(data, width):
    newData = dict()
    for key in data:
        text = removeWhitespaces(data[key])
        newData[key] = convertToColumnText(text, width=width)
    return newData
