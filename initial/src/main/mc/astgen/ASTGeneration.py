from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import*

class ASTGeneration(MCVisitor):

    # Visit a AST tree produced by MCParser #program.
    def visitProgram(self,ctx:MCParser.ProgramContext):
        # program : manydecls EOF;
        return Program(self.visit(ctx.manydecls()))


    # Visit a AST tree produced by MCParser #manydecls.
    def visitManydecls(self, ctx:MCParser.ManydeclsContext):
        # manydecls : decl+;
        return [i for x in ctx.decl() for i in self.visit(x)]


    # Visit a AST tree produced by MCParser #decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        # decl : variable_decl | function_decl ;
        return self.visit(ctx.variable_decl()) if ctx.variable_decl() else self.visit(ctx.function_decl())


    # Visit a AST tree produced by MCParser #variable_decl.
    def visitVariable_decl(self, ctx:MCParser.Variable_declContext):
        # variable_decl : primitive_type many_variables SEMI ;
        primitiveType = self.visit(ctx.primitive_type())
        manyVar = self.visit(ctx.many_variables())
        return [VarDecl(var[0],ArrayType(var[1],primitiveType)) if isinstance(var,list) else VarDecl(var,primitiveType) for var in manyVar]
       

    # Visit a AST tree produced by MCParser #many_variables.
    def visitMany_variables(self, ctx:MCParser.Many_variablesContext):
        # many_variables : variable (CM variable)* ;
        return [self.visit(x) for x in ctx.variable()]


    # Visit a AST tree produced by MCParser #variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        # variable : ID | array ;
        return ctx.ID().getText() if ctx.ID() else self.visit(ctx.array())

    
    # Visit a AST tree produced by MCParser #array.
    def visitArray(self, ctx:MCParser.ArrayContext):
        # array : ID LSB INTLIT RSB;
        return [ctx.ID().getText(), int(ctx.INTLIT().getText())]


    # Visit a AST tree produced by MCParser #primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        # primitive_type : INTTYPE | FLOATTYPE | BOOLEANTYPE | STRINGTYPE ;
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLEANTYPE():
            return BoolType()
        elif ctx.STRINGTYPE():
            return StringType()


    # Visit a AST tree produced by MCParser #function_decl.
    def visitFunction_decl(self, ctx:MCParser.Function_declContext):
        # function_decl : func_type ID LP parameter_list RP block_statement ;
        return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.parameter_list()),self.visit(ctx.func_type()),self.visit(ctx.block_statement()))]


    # Visit a AST tree produced by MCParser #func_type.
    def visitFunc_type(self, ctx:MCParser.Func_typeContext):
        # func_type : primitive_type | VOIDTYPE | output_array_pointer_type ;
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.VOIDTYPE():
            return VoidType()
        else:
            return self.visit(ctx.output_array_pointer_type())


    # Visit a AST tree produced by MCParser #parameter_list.
    def visitParameter_list(self, ctx:MCParser.Parameter_listContext):
        # parameter_list : (parameter_decl (CM parameter_decl)*)? ;
        return [self.visit(x) for x in ctx.parameter_decl()]


    # Visit a AST tree produced by MCParser #parameter_decl.
    def visitParameter_decl(self, ctx:MCParser.Parameter_declContext):
        # parameter_decl : primitive_type ID | input_array_pointer_type ;
        return VarDecl(ctx.ID().getText(),self.visit(ctx.primitive_type())) if ctx.ID() else self.visit(ctx.input_array_pointer_type())


    # Visit a AST tree produced by MCParser #array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        # array_pointer_type : input_array_pointer_type | output_array_pointer_type;
        return self.visit(ctx.input_array_pointer_type()) if ctx.input_array_pointer_type() else self.visit(ctx.output_array_pointer_type())


    # Visit a AST tree produced by MCParser #input_array_pointer_type.
    def visitInput_array_pointer_type(self, ctx:MCParser.Input_array_pointer_typeContext):
        # input_array_pointer_type : primitive_type ID LSB RSB;
        return VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.primitive_type())))


    # Visit a AST tree produced by MCParser #output_array_pointer_type.
    def visitOutput_array_pointer_type(self, ctx:MCParser.Output_array_pointer_typeContext):
        # output_array_pointer_type : primitive_type LSB RSB;
        return ArrayPointerType(self.visit(ctx.primitive_type()))


    # Visit a AST tree produced by MCParser #expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        # expr : expr1 ASSIGN expr | expr1;
        return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.expr1()),self.visit(ctx.expr())) if ctx.getChildCount() == 3 else self.visit(ctx.expr1())


    # Visit a AST tree produced by MCParser #expr1.
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        # expr1 : expr1 OR expr2 | expr2;
        return BinaryOp(ctx.OR().getText(),self.visit(ctx.expr1()),self.visit(ctx.expr2())) if ctx.getChildCount() == 3 else self.visit(ctx.expr2())


    # Visit a AST tree produced by MCParser #expr2.
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        # expr2 : expr2 AND expr3 | expr3;
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3())) if ctx.getChildCount() == 3 else self.visit(ctx.expr3())


    # Visit a AST tree produced by MCParser #expr3.
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        # expr3 : expr4 (EQ | NEQ) expr4 | expr4;
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr4(0)),self.visit(ctx.expr4(1)))
        else:
            return self.visit(ctx.expr4(0))


    # Visit a AST tree produced by MCParser #expr4.
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        # expr4 : expr5 (LESS | LEQ | GRATER | GEQ) expr5 | expr5;
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr5(0)),self.visit(ctx.expr5(1)))
        else:
            return self.visit(ctx.expr5(0))


    # Visit a AST tree produced by MCParser #expr5.
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        # expr5 : expr5 (ADD | SUB) expr6 | expr6;
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr5()),self.visit(ctx.expr6()))            
        else:
            return self.visit(ctx.expr6())


    # Visit a AST tree produced by MCParser #expr6.
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        # expr6 : expr6 (DIV | MUL | MOD) expr7 | expr7;
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr6()),self.visit(ctx.expr7()))
        else:
            return self.visit(ctx.expr7())


    # Visit a AST tree produced by MCParser #expr7.
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        # expr7 : (SUB | NOT) expr7 | expr8;
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.expr7()))
        else:
            return self.visit(ctx.expr8())


    # Visit a AST tree produced by MCParser #expr8.
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        # expr8 : expr9 LSB expr RSB | expr9;
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.expr9()),self.visit(ctx.expr()))
        else:
            return self.visit(ctx.expr9())


    # Visit a AST tree produced by MCParser #expr9.
    def visitExpr9(self, ctx:MCParser.Expr9Context):
        # expr9 : LP expr RP | operands;
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.operands())


    # Visit a AST tree produced by MCParser #operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        # operands : literal | ID | func_call;
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.func_call())


    # Visit a AST tree produced by MCParser #literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        # literal : INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT;
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(ctx.BOOLEANLIT().getText())


    # Visit a AST tree produced by MCParser #func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        # func_call : ID LP exprlist RP;
        return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.exprlist()))


    # Visit a AST tree produced by MCParser #exprlist.
    def visitExprlist(self, ctx:MCParser.ExprlistContext):
        # exprlist : (expr (CM expr)*) ? ;
        return [self.visit(x) for x in ctx.expr()]


    # Visit a AST tree produced by MCParser #statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        # statement : if_stmt 
        #           | for_stmt 
        #           | dowhile_stmt 
        #           | break_stmt 
        #           | continue_stmt 
        #           | return_stmt 
        #           | expr_stmt
        #           | block_statement
        return self.visit(ctx.getChild(0))


    # Visit a AST tree produced by MCParser #if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        # if_stmt : IF LP expr RP statement (ELSE statement)?;
        return If(self.visit(ctx.expr()),self.visit(ctx.statement(0))) if ctx.getChildCount() == 5 else If(self.visit(ctx.expr()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))


    # Visit a AST tree produced by MCParser #dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MCParser.Dowhile_stmtContext):
        # dowhile_stmt : DO statement+ WHILE expr SEMI;
        return Dowhile([self.visit(x) for x in ctx.statement()],self.visit(ctx.expr()))


    # Visit a AST tree produced by MCParser #for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        # for_stmt : FOR LP expr SEMI expr SEMI expr RP statement;
        return For(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)),self.visit(ctx.expr(2)),self.visit(ctx.statement()))


    # Visit a AST tree produced by MCParser #break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        # break_stmt : BREAK SEMI;
        return Break()


    # Visit a AST tree produced by MCParser #continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        # continue_stmt : CONTINUE SEMI;
        return Continue()


    # Visit a AST tree produced by MCParser #return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        # return_stmt : RETURN expr? SEMI;
        return Return(self.visit(ctx.expr())) if ctx.expr() else Return()


    # Visit a AST tree produced by MCParser #expr_stmt.
    def visitExpr_stmt(self, ctx:MCParser.Expr_stmtContext):
        # expr_stmt : expr SEMI;
        return self.visit(ctx.expr())


    # Visit a AST tree produced by MCParser #block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        # block_statement : LB var_stmt_list RB ;
        return Block(self.visit(ctx.var_stmt_list()))


    # Visit a AST tree produced by MCParser #var_stmt_list.
    def visitVar_stmt_list(self, ctx:MCParser.Var_stmt_listContext):
        # var_stmt_list : var_stmt* ;        
        return [i for x in ctx.var_stmt() for i in self.visit(x)] 


    # Visit a AST tree produced by MCParser #var_stmt.
    def visitVar_stmt(self, ctx:MCParser.Var_stmtContext):
        # var_stmt : variable_decl | statement ;
        return self.visit(ctx.variable_decl()) if ctx.variable_decl() else [self.visit(ctx.statement())]