import unittest
import json
from types import SimpleNamespace
from collections import namedtuple

class Test_Simple2_Test(unittest.TestCase):
    def test_B(self):
        self.assertFalse(False);

        data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

        # Parse JSON into an object with attributes corresponding to dict keys.
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        print(x.name, x.hometown.name, x.hometown.id)



        # Load json from file

        # This loads a json file directly into a new object
        with open('Example.json') as json_file:
            data = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))

            print(data.name, data.hometown.name, data.hometown.id)


if __name__ == '__main__':
    unittest.main()
