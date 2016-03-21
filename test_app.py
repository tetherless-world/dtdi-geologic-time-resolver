import unittest
import app


class TestGeologicTimeResolver(unittest.TestCase):

    def test_hello(self):
        hello = app.hello()
        self.assertIsNotNone(hello)

    def test_resolve_within(self):
        out = app.resolve_geologic_time_within(0, 100)
        self.assertIsNotNone(out)

    def test_resolve_intersects(self):
        out = app.resolve_geologic_time_intersects(0, 100)
        self.assertIsNotNone(out)

    def test_extreme_resolves_within(self):
        out = app.resolve_geologic_time_within(5400, 5600)
        self.assertIsNotNone(out)

    def test_resolves_within_with_no_higher_concept(self):
        out = app.resolve_geologic_time_within(540, 542)
        self.assertIsNotNone(out)


if __name__ == '__main__':
    unittest.main()
