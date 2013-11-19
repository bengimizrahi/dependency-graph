import unittest

from dgg import dgg

class TestDot(unittest.TestCase):

    def test_validate(self):
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
        self.assertTrue(dgg.validate(data))


if __name__ == "__main__":
    unittest.main()
