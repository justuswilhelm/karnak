from unittest import TestCase

from karnak import compile


class Step1TestCase(TestCase):
    def test(self):
        with open("test/fixtures/in1.kr") as fd:
            inp = fd.read()
        with open("test/fixtures/in1.as") as fd:
            out = fd.read()
        self.assertEqual(compile(inp), out)
