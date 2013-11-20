import unittest

from dgg import dgg, utils


class TestDot(unittest.TestCase):

    data = {
        "1": {
            "label": "$f1|{$f2|$f3|$f4}|$f5",
            "fields": {
                "f1": "1-field1",
                "f2": "1-field2",
                "f3": "1-field3",
                "f4": "1-field4",
                "f5": "1-field5",
            },
            "refs": ["2"],
            "backrefs": [],
        },
        "2": {
            "label": "$f1|{$f2|$f3|$f4}|$f5",
            "fields": {
                "f1": "2-field1",
                "f2": "2-field2",
                "f3": "2-field3",
                "f4": "2-field4",
                "f5": "2-field5",
            },
            "refs": ["1"],
            "backrefs": [],
        }
    }

    def test_validate(self):
        self.assertTrue(dgg.validate(self.data))

    def test_createDotGraph(self):
        self.assertEqual(dgg.createDotGraph(self.data),
            {
                '1': {
                    'refs': ['2'],
                    'name': '1',
                    'label': '1-field1|{1-field2|1-field3|1-field4}|1-field5'
                },
                '2': {
                    'refs': ['1'],
                    'name': '2',
                    'label': '2-field1|{2-field2|2-field3|2-field4}|2-field5'
                },
            })


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
