import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_1(self):
        
        input = """
            float[] add(float a, float b[]) {
                for (i = 0; i >= 0; i = i + 1) {
                    b[i] = a + b[i];
                }
                return b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204)) 