from __future__ import print_function

import difflib
import os
import unittest

import remove_py_md

class TestRemovePy(unittest.TestCase):

    def test_store_input(self):
        test_file = 'tests/test.md'
        test_out = 'tests/test_no_py.md'
        gold = 'tests/gold.md'
        remove_py_md.remove_py(test_file)
        
        with open(gold, 'r') as f:
            gold_lines = f.readlines()
        with open(test_out, 'r') as f:
            test_lines = f.readlines()

        # might break due to line ending..
        diff = difflib.unified_diff(gold_lines, test_lines)
        
        list_diff = list(diff)
        if list_diff:
            print("Files differ:")
            for l in list_diff:
                print(l, end='')
            self.fail("Files differed")
        else:
            self.remove_file(test_out)
            
    def remove_file(self, file):
        os.remove(file)
        
if __name__ == '__main__':
    unittest.main()
