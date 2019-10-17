import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_var_decl_1(self):        
        input = """int a,b[10];"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType()))]))
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
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"), [], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_func_decl_12(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_func_decl_13(self):
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_func_decl_14(self):
        input = """
            int[] foo(int a, float b[]) {
                int c[3];
                if (a>0) foo(a-1,b);
                return c; 
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(3,IntType())),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")])),Return(Id("c"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_func_decl_15(self):        
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

    def test_func_decl_16(self):        
        input = """
            int main() {
            boolean boo[2];
            boo[1] = true;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("boo",ArrayType(2,BoolType())),BinaryOp("=",ArrayCell(Id("boo"),IntLiteral(1)),BooleanLiteral("true"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_func_decl_17(self):        
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

    def test_func_decl_18(self):        
        input = """
            string name() {
                return "name";
            }
        """
        expect = str(Program([FuncDecl(Id("name"),[],StringType(),Block([Return(StringLiteral("name"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_func_decl_19(self):        
        input = """
            boolean isFalse(boolean a) {
                if (a == true) {return false;}
            }
        """
        expect = str(Program([FuncDecl(Id("isFalse"),[VarDecl("a",BoolType())],BoolType(),Block([If(BinaryOp("==",Id("a"),BooleanLiteral("true")),Block([Return(BooleanLiteral("false"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_func_decl_20(self):        
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

    def test_func_decl_21(self):        
        input = """
            string[] school(string a, string b, string c) {}
        """
        expect = str(Program([FuncDecl(Id("school"),[VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType())],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_expression_1(self):        
        input = """
            int main() {
            a = !b + -a;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",UnaryOp("!",Id("b")),UnaryOp("-",Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_expression_2(self):        
        input = """
            int main() {
            a = b / c % d * e;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("*",BinaryOp("%",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_expression_3(self):        
        input = """
             int main() {
            a = b + c - -d * e[a];
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",Id("b"),Id("c")),BinaryOp("*",UnaryOp("-",Id("d")),ArrayCell(Id("e"),Id("a")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_expression_4(self):        
        input = """
            int main() {
            a = b < (c > d);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("<",Id("b"),BinaryOp(">",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_expression_5(self):        
        input = """
            int main() {
            a = b < c + d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("<",Id("b"),BinaryOp("+",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_expression_6(self):        
        input = """
            int main() {
            a = b < c == d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("==",BinaryOp("<",Id("b"),Id("c")),Id("d")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_expression_7(self):        
        input = """
            int main() {
            a = b && c == d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("&&",Id("b"),BinaryOp("==",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_expression_8(self):        
        input = """
            int main() {
            a = b || c && d;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("||",Id("b"),BinaryOp("&&",Id("c"),Id("d"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_expression_9(self):        
        input = """
        int main() {
            a = b+c*d/e-f<g==h;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("==",BinaryOp("<",BinaryOp("-",BinaryOp("+",Id("b"),BinaryOp("/",BinaryOp("*",Id("c"),Id("d")),Id("e"))),Id("f")),Id("g")),Id("h")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_expression_10(self):        
        input = """
            int main() {
            12 = 5 * 9 / 10 + 15 % 8 && 1 < 10;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",IntLiteral(12),BinaryOp("&&",BinaryOp("+",BinaryOp("/",BinaryOp("*",IntLiteral(5),IntLiteral(9)),IntLiteral(10)),BinaryOp("%",IntLiteral(15),IntLiteral(8))),BinaryOp("<",IntLiteral(1),IntLiteral(10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_expression_11(self):        
        input = """
            int main() {
            a = b + foo(5) - (foo() % 1);
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",Id("b"),CallExpr(Id("foo"),[IntLiteral(5)])),BinaryOp("%",CallExpr(Id("foo"),[]),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_expression_12(self):        
        input = """
            int main() {
            foo(2)[3+x] = a[b[2]] +3;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_expression_13(self):        
        input = """
        void foo (float a[]) {}
        void goo (float x[]) {
            float y[10];
            int z[10];
            foo(x); 
            foo(y); 
            foo(z); 
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(FloatType()))],VoidType(),Block([])),FuncDecl(Id("goo"),[VarDecl("x",ArrayPointerType(FloatType()))],VoidType(),Block([VarDecl("y",ArrayType(10,FloatType())),VarDecl("z",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("x")]),CallExpr(Id("foo"),[Id("y")]),CallExpr(Id("foo"),[Id("z")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_expression_14(self):        
        input = """
            void foo ( ) {
            if(a<b) return ; 
            else return 2; 
        }       
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([If(BinaryOp("<",Id("a"),Id("b")),Return(),Return(IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_expression_15(self):        
        input = """
            int[] foo (int b[]){
                int a [1];
                if (b>c) return a;
                else return b;
            }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl("a",ArrayType(1,IntType())),If(BinaryOp(">",Id("b"),Id("c")),Return(Id("a")),Return(Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_statement_1(self):        
        input = """
        int main() {
            if (a>b) a=1;
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_statement_2(self):        
        input = """
            int main() {
            if (a>b) a=1; else a=0;
            }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_statement_3(self):        
        input = """
        int main() {
            if (a>b) {
                int c[5];
                c[2] = b + a * 10 % c[d[e[t+m+5]]];
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("a"),Id("b")),Block([VarDecl("c",ArrayType(5,IntType())),BinaryOp("=",ArrayCell(Id("c"),IntLiteral(2)),BinaryOp("+",Id("b"),BinaryOp("%",BinaryOp("*",Id("a"),IntLiteral(10)),ArrayCell(Id("c"),ArrayCell(Id("d"),ArrayCell(Id("e"),BinaryOp("+",BinaryOp("+",Id("t"),Id("m")),IntLiteral(5))))))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_statement_4(self):        
        input = """
        int main(){
            do {
                int a[2];
            }
            {
                a+b;
            }
            while (a<5);
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",ArrayType(2,IntType()))]),Block([BinaryOp("+",Id("a"),Id("b"))])],BinaryOp("<",Id("a"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_statement_5(self):        
        input = """
        int main(){
            do {
                int a[2];
            }
            {
                a+b;
            }
            while a<5==9%7;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",ArrayType(2,IntType()))]),Block([BinaryOp("+",Id("a"),Id("b"))])],BinaryOp("==",BinaryOp("<",Id("a"),IntLiteral(5)),BinaryOp("%",IntLiteral(9),IntLiteral(7))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_statement_6(self):        
        input = """
        int main(){
            do {
                foo(5);
            }
            while (a<5);
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([CallExpr(Id("foo"),[IntLiteral(5)])])],BinaryOp("<",Id("a"),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_statement_7(self):        
        input = """
        int main(){
            for(i = 0; i < 10; i=i+1) {
                putIntLn("Hello world!\\n");
            }
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[StringLiteral("Hello world!\\n")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_statement_8(self):        
        input = """
        int main(){
            for(i = 0; i < foo(2)[foo(4)[a+b+c]]; i = i + 1) {
                putIntLn("Hello world!\\n");
            }
        }   
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),ArrayCell(CallExpr(Id("foo"),[IntLiteral(4)]),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c"))))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[StringLiteral("Hello world!\\n")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_statement_9(self):        
        input = """
        int main(){
            for (i = 0; i < 10; i = i + 1) {
                printf("Hello world!\\n");
            }
            {

            }
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral("Hello world!\\n")])])),Block([])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_statement_10(self):        
        input = """
        int main(){
            for (i = 0; i < 10; i = i + 1) {
                for (j = 10; j >= 0; j = j - 1) {
                    if (i == j) putIntLn("i");
                }
            }
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(10)),BinaryOp(">=",Id("j"),IntLiteral(0)),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),Id("j")),CallExpr(Id("putIntLn"),[StringLiteral("i")]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_statement_11(self):        
        input = """
        int main(){
            for (i = 0; i < 10; i = i + 1) {
                for (j = 10; j >= 0; j = j - 1) {
                    if (i == j) return 0;
                    else return 1;
                }
            }
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(BinaryOp("=",Id("j"),IntLiteral(10)),BinaryOp(">=",Id("j"),IntLiteral(0)),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),Id("j")),Return(IntLiteral(0)),Return(IntLiteral(1)))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_statement_12(self):        
        input = """
            int main(){
            for (i = 0; i < 10; i = i + 1){
                if (i == a % foo(2)[i]) break;
                else continue;
            }
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),BinaryOp("%",Id("a"),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),Id("i")))),Break(),Continue())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_statement_13(self):        
        input = """
        int i;
        int f() {
            return 200;
        }
        void main () {
            int main ;
            main = f();
            putIntLn (main);
            {
                int i;
                int main;
                int f;
                main = f = i = 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
                putIntLn(main);
        }    
        """
        expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("f"),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("main",IntType()),BinaryOp("=",Id("main"),CallExpr(Id("f"),[])),CallExpr(Id("putIntLn"),[Id("main")]),Block([VarDecl("i",IntType()),VarDecl("main",IntType()),VarDecl("f",IntType()),BinaryOp("=",Id("main"),BinaryOp("=",Id("f"),BinaryOp("=",Id("i"),IntLiteral(100)))),CallExpr(Id("putIntLn"),[Id("i")]),CallExpr(Id("putIntLn"),[Id("main")]),CallExpr(Id("putIntLn"),[Id("f")])]),CallExpr(Id("putIntLn"),[Id("main")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_all_1(self):        
        input = """
        int[] foo(boolean a, float b){}
        int main() {
            putIntLn(foo(a>=b,00.E2019)[10]);
        }
        """
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",BoolType()),VarDecl("b",FloatType())],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[ArrayCell(CallExpr(Id("foo"),[BinaryOp(">=",Id("a"),Id("b")),FloatLiteral(0.0)]),IntLiteral(10))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_all_2(self):        
        input = """
        /* this is a comment */ 
        void foo() {if (a==0) {b = a+c;}}
        """
        expect = str(Program([FuncDecl(Id("foo"),[],VoidType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(0)),Block([BinaryOp("=",Id("b"),BinaryOp("+",Id("a"),Id("c")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_all_3(self):        
        input = """
        int main() {
            foo(2)[3+x] = a[b[2]] +3;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_all_4(self):        
        input = """
        int main() {
            int a,b[10];
            a = b[1] = foo()[3] = x = 1 ;    
        }
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(10,IntType())),BinaryOp("=",Id("a"),BinaryOp("=",ArrayCell(Id("b"),IntLiteral(1)),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),BinaryOp("=",Id("x"),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_all_5(self):        
        input = """
        int main() {
            a[(123)];
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("a"),IntLiteral(123))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_all_6(self):        
        input = """
        int main() {
            (-12.25e-12);
        }   
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("-",FloatLiteral(1.225e-11))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_all_7(self):        
        input = """
        int main() {
            a = false;
            do {
                if (b) a; 
                continue;
            } while !a;
        }    
        """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BooleanLiteral(False)),Dowhile([Block([If(Id("b"),Id("a")),Continue()])],UnaryOp("!",Id("a")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    # def test_all_8(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,361))

    # def test_all_9(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,362))

    # def test_all_10(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,363))

    # def test_all_11(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,364))

    # def test_all_12(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,365))

    # def test_all_13(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,366))

    # def test_all_14(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,367))

    # def test_all_15(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,368))

    # def test_all_16(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,369))

    # def test_all_17(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,370))

    # def test_all_18(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,371))

    # def test_all_19(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,372))

    # def test_all_20(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,373))

    # def test_all_21(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,374))

    # def test_all_22(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,375))

    # def test_all_23(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,376))

    # def test_all_24(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,377))

    # def test_all_25(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,378))

    # def test_all_26(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,379))

    # def test_all_27(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,380))

    # def test_all_28(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,381))

    # def test_all_29(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,382))

    # def test_all_30(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,383))

    # def test_all_31(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,384))

    # def test_all_32(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,385))

    # def test_all_33(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,386))

    # def test_all_34(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,387))

    # def test_all_35(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,388))

    # def test_all_36(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,389))

    # def test_all_37(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,390))

    # def test_all_38(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,391))

    # def test_all_39(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,392))

    # def test_all_40(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,393))

    # def test_all_41(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,394))

    # def test_all_42(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,395))

    # def test_all_43(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,396))

    # def test_all_44(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,397))

    # def test_all_45(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,398))

    # def test_all_46(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,399))

    # def test_all_47(self):        
    #     input = """
            
    #     """
    #     expect = str(Program([]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,400))


    