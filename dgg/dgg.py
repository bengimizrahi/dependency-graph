def validate(data):
    if not isinstance(data, dict):
        return False
    for node in data.itervalues():
        if not isinstance(node, dict):
            return False
        if set(["label", "fields", "refs"]) - set(node.keys()):
            return False
        if not isinstance(node["label"], str):
            return False
        if not isinstance(node["fields"], dict):
            return False
        for key, value in node["fields"].iteritems():
            if not (isinstance(key, str) and isinstance(value, str)):
                return False
        if type(node["refs"]) not in (tuple, list):
            return False
    return True
