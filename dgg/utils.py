import re

def removeWhitespaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def removeWhitespacesInDictValues(data):
    newData = dict()
    for key in data:
        newData[key] = removeWhitespaces(data[key])
    return newData
