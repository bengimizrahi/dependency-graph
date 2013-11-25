from string import Template

import utils


def validate(data):
    if not isinstance(data, dict):
        return False
    if any((n.isdigit() for n in data)):
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

def createDotGraph(data, columnWidth=25):
    dotGraph = dict()
    for name in data:
        node = data[name]
        dotNode = dict()
        dotNode["name"] = name
        dotNode["label"] = Template(node["label"]).substitute(
            **(utils.removeWhitespacesAndColumnizeDictValues(node["fields"], columnWidth)))
        dotNode["refs"] = node["refs"]
        dotGraph[name] = dotNode
    return dotGraph

def createDotText(filename, dotGraph):
    textSnippetForNodes = "\n".join(('%s [label="%s"];' % (n["name"], n["label"])
        for n in dotGraph.itervalues()))
    textSnippetForEdges = "\n".join(('%s -> %s;' % (n["name"],t) for n in dotGraph.itervalues() for t in n["refs"]))
    template = """digraph {
node [shape=record];
%s
%s
};"""
    with file("{}.gv".format(filename), "w") as f:
        print >>f, template % (textSnippetForNodes, textSnippetForEdges)