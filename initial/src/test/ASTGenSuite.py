import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl_0(self):
        
        input = """int a,b[10];"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_var_decl_1(self):
        
        input = """int b[10];"""
        expect = str(Program([VarDecl("b",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_var_decl_2(self):
        
        input = """int a,b,c,d,e[10];"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",IntType()),VarDecl("e",ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var_decl_3(self):
        
        input = """
        int a;
        float b;
        string c;
        boolean d;
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_var_decl_4(self):
        
        input = """
        int a[10];
        float b,c[5];
        string d[10];
        """
        expect = str(Program([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",FloatType()),VarDecl("c",ArrayType(5,FloatType())),VarDecl("d",ArrayType(10,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_func_decl_1(self):
        
        input = """int foo() {}"""
        expect = str(Program([FuncDecl(Id("foo"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_func_decl_2(self):
        
        input = """int foo(int a, float b) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_func_decl_3(self):
        
        input = """int foo(int a, float b[]) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_func_decl_4(self):
        
        input = """int[] foo(int a, float b) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_func_decl_5(self):
        
        input = """int[] foo(int a, float b[]) {}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_func_decl_6(self):
        
        input = """int foo(int a, float b) {
            int c,d;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([VarDecl("c",IntType()),VarDecl("d",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_func_decl_7(self):
        
        input = """int foo(int a, float b) {
            int c[5];
            float d;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([VarDecl("c",ArrayType(5,IntType())),VarDecl("d",FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_func_decl_8(self):
        
        input = """int foo(int a, float b) {
            return;
            break;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([Return(),Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_func_decl_9(self):
        
        input = """int foo(int a, float b) {
            a = b;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([BinaryOp("=",Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))


    def test_func_decl_10(self):
        
        input = """int foo(int a, float b) {
            return a + b;
        }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",FloatType())],IntType(),Block([Return(BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_func_decl_11(self):
        """Simple program: int main() {}"""
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_func_decl_12(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_func_decl_13(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_func_decl_13(self):
        
        input = """
            int[] foo(int a, float b[]) {
                int c[3];
                if (a>0) foo(a-1,b);
                return c; 
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")])),Return(Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_func_decl_14(self):
        
        input = """
            int main()
            {
                // printf() displays the string inside quotation
                printf("Hello, World!");
                return 0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("printf"),[StringLiteral("Hello, World!")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_func_decl_15(self):
        
        input = """
            int main() {
            boolean boo[2];
            boo[1] = true;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("boo",ArrayType(2,BoolType())),BinaryOp("=",ArrayCell(Id("boo"),IntLiteral(1)),BooleanLiteral("true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_func_decl_16(self):
        
        input = """
            int foo (int a , float b[])
        {
            boolean c ;
            int i ;
            i = a + 3 ;
            if (i > 0) {
                int d ;
                d = i + 3 ;
                putInt(d) ;
            }
            return i ;
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_func_decl_17(self):
        
        input = """
            string name() {
                return "name";
            }
        """
        expect = str(Program([FuncDecl(Id("name"),[],StringType(),Block([Return(StringLiteral("name"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_func_decl_18(self):
        
        input = """
            boolean isFalse(boolean a) {
                if (a == true) {return false;}
            }
        """
        expect = str(Program([FuncDecl(Id("isFalse"),[VarDecl("a",BoolType())],BoolType(),Block([If(BinaryOp("==",Id("a"),BooleanLiteral("true")),Block([Return(BooleanLiteral("false"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_func_decl_19(self):
        
        input = """
            float[] add(float a, float b[]) {
                for (i = 0; i >= 0; i = i + 1) {
                    b[i] = a + b[i];
                }
                return b;
            }
        """
        expect = str(Program([FuncDecl(Id("add"),[VarDecl("a",FloatType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(FloatType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("b"),Id("i")),BinaryOp("+",Id("a"),ArrayCell(Id("b"),Id("i"))))])),Return(Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_func_decl_20(self):
        
        input = """
            string[] school(string a, string b, string c) {}
        """
        expect = str(Program([FuncDecl(Id("school"),[VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType())],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))