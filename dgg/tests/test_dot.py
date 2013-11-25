import unittest

from dgg import dgg, utils


class TestDot(unittest.TestCase):

    data = {
        "n1": {
            "label": "$f1|{$f2|$f3|$f4}|$f5",
            "fields": {
                "f1": "n1-field1",
                "f2": "n1-field2",
                "f3": "n1-field3",
                "f4": "n1-field4",
                "f5": "n1-field5",
            },
            "refs": ["n2"],
            "backrefs": [],
        },
        "n2": {
            "label": "$f1|{$f2|$f3|$f4}|$f5",
            "fields": {
                "f1": "n2-field1",
                "f2": "n2-field2",
                "f3": "n2-field3",
                "f4": "n2-field4",
                "f5": "n2-field5",
            },
            "refs": ["n1"],
            "backrefs": [],
        }
    }

    def test_validate(self):
        self.assertTrue(dgg.validate(self.data))

    def test_createDotGraph(self):
        self.assertEqual(dgg.createDotGraph(self.data),
            {
                'n1': {
                    'refs': ['n2'],
                    'name': 'n1',
                    'label': 'n1-field1|{n1-field2|n1-field3|n1-field4}|n1-field5'
                },
                'n2': {
                    'refs': ['n1'],
                    'name': 'n2',
                    'label': 'n2-field1|{n2-field2|n2-field3|n2-field4}|n2-field5'
                },
            })

    def test_createDotText(self):
        dg = dgg.createDotGraph(self.data, 20)
        dgg.createDotText("test_createDotGraph", dg)


class TestUtils(unittest.TestCase):

    def test_removeWhiteSpaces(self):
        text = "    a b  c\nd   \ne\n   f   \n   g    "
        cleanText = utils.removeWhitespaces(text)
        self.assertEqual(cleanText.count(' '), 6)

    def test_removeWhitespacesAndColumnizeDictValues(self):
        data = {"f1": "    a b  c\nd   \ne\n   f   \n   g    "}
        newData = utils.removeWhitespacesAndColumnizeDictValues(data, 4)
        self.assertEqual(newData["f1"].count('\n'), 3)


if __name__ == "__main__":
    unittest.main()
