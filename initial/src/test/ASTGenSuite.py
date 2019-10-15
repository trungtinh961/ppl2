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
        
        input = """int foo() {};"""
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

    