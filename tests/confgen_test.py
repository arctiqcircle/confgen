import os
import unittest

import confgen


class TestGeneration(unittest.TestCase):
    def test_looping_yaml(self):
        data_filename = "data/data.yml"
        temp_filename = "templates/looping_template.j2"
        data = confgen.unpack(data_filename)
        assert len(data) > 0
        template = confgen.read_template(temp_filename)
        renders = []
        for entry in data:
            renders.append(template.render(entry))
        assert len(renders) > 0
        print(renders)

    def test_looping_csv(self):
        data_filename = "data/data.csv"
        temp_filename = "templates/looping_template.j2"
        data = confgen.unpack(data_filename)
        assert len(data) > 0
        template = confgen.read_template(temp_filename)
        renders = []
        for entry in data:
            renders.append(template.render(entry))
        assert len(renders) > 0
        print(renders)


if __name__ == '__main__':
    unittest.main()
