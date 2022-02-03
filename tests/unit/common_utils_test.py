import pytest

import utils.common_utils as commons

class TestClass:
    def test_checkSymbols(self):
        s1 = "(){}"
        s2 = "( { [ () [] ] } )"
        s3 = "/* abcd /* efgh */ ijkl */"
        s4 = "(()"
        s5 = ""
        
        c1 = commons.checkSymbols(s1)
        c2 = commons.checkSymbols(s2)
        c3 = commons.checkSymbols(s3)
        c4 = commons.checkSymbols(s4)
        c5 = commons.checkSymbols(s5)

        assert c1 == True
        assert c2 == True
        assert c3 == True
        assert c4 == False
        assert c5 == True

    def test_removeComments(self):
        s1 = "/* abcd /* efgh */ ijkl */"
        s2 = "/**/"
        s3 = "/*( { [*/ () [] ] } )"

        r1 = commons.removeComments(s1)
        r2 = commons.removeComments(s2)
        r3 = commons.removeComments(s3)

        assert r1 == " ijkl */"
        assert r2 == ""
        assert r3 == " () [] ] } )"

    def test_costProrating(self):
        amount1 = 47
        amount2 = 0
        weights1 = [0.2,0.3,0.3,0.2]
        weights2 = [0,0.5,0,0.4]
        weights3 = [0.1,0.2]

        s1 = commons.costProrating(amount1,weights1)
        s2 = commons.costProrating(amount1,weights2)
        s3 = commons.costProrating(amount2,weights3)

        assert s1 == [10, 14, 14, 9]
        assert s2 == [0, 26, 0, 21]
        assert s3 == [0, 0]
