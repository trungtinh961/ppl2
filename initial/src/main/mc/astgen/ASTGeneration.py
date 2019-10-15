from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import*

class ASTGeneration(MCVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(self.visit(ctx.manydecls()))


    # Visit a parse tree produced by MCParser#manydecls.
    def visitManydecls(self, ctx:MCParser.ManydeclsContext):
        return [i for x in ctx.decl() for i in self.visit(x)]


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visit(ctx.variable_decl()) if ctx.variable_decl() else self.visit(ctx.function_decl())


    # Visit a parse tree produced by MCParser#variable_decl.
    def visitVariable_decl(self, ctx:MCParser.Variable_declContext):
        primitiveType = self.visit(ctx.primitive_type())
        manyVar = self.visit(ctx.many_variables())
        return [VarDecl(var,primitiveType) if len(var)==1 else VarDecl(var[0],ArrayType(var[1],primitiveType)) for var in manyVar]
       

    # Visit a parse tree produced by MCParser#many_variables.
    def visitMany_variables(self, ctx:MCParser.Many_variablesContext):
        return [self.visit(x) for x in ctx.variable()]


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return ctx.ID().getText() if ctx.ID() else self.visit(ctx.array())

    
    # Visit a parse tree produced by MCParser#array.
    def visitArray(self, ctx:MCParser.ArrayContext):
        return [ctx.ID().getText(), int(ctx.INTLIT().getText())]


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLEANTYPE():
            return BoolType()
        elif ctx.STRINGTYPE():
            return StringType()


    # Visit a parse tree produced by MCParser#function_decl.
    def visitFunction_decl(self, ctx:MCParser.Function_declContext):
        return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.parameter_list()),self.visit(ctx.func_type()),self.visit(ctx.block_statement()))]


    # Visit a parse tree produced by MCParser#func_type.
    def visitFunc_type(self, ctx:MCParser.Func_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.VOIDTYPE():
            return VoidType()
        else:
            return self.visit(ctx.output_array_pointer_type())


    # Visit a parse tree produced by MCParser#parameter_list.
    def visitParameter_list(self, ctx:MCParser.Parameter_listContext):
        return [self.visit(x) for x in ctx.parameter_decl()]


    # Visit a parse tree produced by MCParser#parameter_decl.
    def visitParameter_decl(self, ctx:MCParser.Parameter_declContext):
        return (self.visit(ctx.primitive_type()) + Id(ctx.ID().getText())) if ctx.ID() else self.visit(ctx.input_array_pointer_type())


    # Visit a parse tree produced by MCParser#var_stmt_list.
    def visitVar_stmt_list(self, ctx:MCParser.Var_stmt_listContext):
        return [self.visit(x) for x in ctx.var_stmt()]


    # Visit a parse tree produced by MCParser#var_stmt.
    def visitVar_stmt(self, ctx:MCParser.Var_stmtContext):
        return self.visit(ctx.variable_decl()) if ctx.variable_decl() else self.visit(ctx.statement())


    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        return self.visit(ctx.input_array_pointer_type()) if ctx.input_array_pointer_type() else self.visit(ctx.output_array_pointer_type())


    # Visit a parse tree produced by MCParser#input_array_pointer_type.
    def visitInput_array_pointer_type(self, ctx:MCParser.Input_array_pointer_typeContext):
        return ArrayPointerType(ctx.primitive_type()) + Id(ctx.ID().getText())


    # Visit a parse tree produced by MCParser#output_array_pointer_type.
    def visitOutput_array_pointer_type(self, ctx:MCParser.Output_array_pointer_typeContext):
        return ArrayPointerType(ctx.primitive_type())


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.expr1()),self.visit(ctx.expr())) if ctx.getChildCount() == 3 else self.visit(ctx.expr1())


    # Visit a parse tree produced by MCParser#expr1.
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        return BinaryOp(ctx.OR().getText(),self.visit(ctx.expr1()),self.visit(ctx.expr2())) if ctx.getChildCount() == 3 else self.visit(ctx.expr2())


    # Visit a parse tree produced by MCParser#expr2.
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3())) if ctx.getChildCount() == 3 else self.visit(ctx.expr3())


    # Visit a parse tree produced by MCParser#expr3.
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        if ctx.getChildCount() == 3:
            if ctx.EQ():
                return BinaryOp(ctx.EQ().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr4()))
            else:
                return BinaryOp(ctx.NEQ().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())


    # Visit a parse tree produced by MCParser#expr4.
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        if ctx.getChildCount() == 3:
            if ctx.LESS():
                return BinaryOp(ctx.LESS().getText(),self.visit(ctx.expr5()),self.visit(ctx.expr5()))
            elif ctx.LEQ():
                return BinaryOp(ctx.LEQ().getText(),self.visit(ctx.expr5()),self.visit(ctx.expr5()))
            elif ctx.GRATER():
                return BinaryOp(ctx.GRATER().getText(),self.visit(ctx.expr5()),self.visit(ctx.expr5()))
            elif ctx.GEQ():
                return BinaryOp(ctx.GEQ().getText(),self.visit(ctx.expr5()),self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())


    # Visit a parse tree produced by MCParser#expr5.
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        if ctx.getChildCount() == 3:
            if ctx.ADD():
                return BinaryOp(ctx.ADD().getText(),self.visit(ctx.expr5()),self.visit(ctx.expr6()))
            else:
                return BinaryOp(ctx.SUB().getText(),self.visit(ctx.expr5()),self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr6())


    # Visit a parse tree produced by MCParser#expr6.
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        if ctx.getChildCount() == 3:
            if ctx.DIV():
                return BinaryOp(ctx.EQ().getText(),self.visit(ctx.expr6()),self.visit(ctx.expr7()))
            elif ctx.MUL():
                return BinaryOp(ctx.MUL().getText(),self.visit(ctx.expr6()),self.visit(ctx.expr7()))
            else:
                return BinaryOp(ctx.MOD().getText(),self.visit(ctx.expr6()),self.visit(ctx.expr7()))
        else:
            return self.visit(ctx.expr7())


    # Visit a parse tree produced by MCParser#expr7.
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        if ctx.getChildCount() == 2:
            if ctx.SUB():
                return UnaryOp(ctx.SUB().getText(),self.visit(ctx.expr7()))
            else:
                return UnaryOp(ctx.NOT().getText(),self.visit(ctx.expr7()))
        else:
            return self.visit(ctx.expr8())


    # Visit a parse tree produced by MCParser#expr8.
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.expr9()),self.visit(ctx.expr()))
        else:
            return self.visit(ctx.expr9())


    # Visit a parse tree produced by MCParser#expr9.
    def visitExpr9(self, ctx:MCParser.Expr9Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.operands())


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.func_call())


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT())
        elif ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT())
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(ctx.BOOLEANLIT())


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.exprlist()))


    # Visit a parse tree produced by MCParser#exprlist.
    def visitExprlist(self, ctx:MCParser.ExprlistContext):
        return [self.visit(x) for x in ctx.expr()]


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return If(self.visit(ctx.expr()),self.visit(ctx.statement())) if ctx.getChildCount() == 5 else If(self.visit(ctx.expr()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))


    # Visit a parse tree produced by MCParser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MCParser.Dowhile_stmtContext):
        return Dowhile([self.visit(x) for x in ctx.statement()],self.visit(ctx.expr()))


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return For(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)),self.visit(ctx.expr(2)),self.visit(ctx.statement()))


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return Return(self.visit(ctx.expr())) if ctx.expr() else Return()


    # Visit a parse tree produced by MCParser#expr_stmt.
    def visitExpr_stmt(self, ctx:MCParser.Expr_stmtContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return Block(self.visit(ctx.var_stmt_list()))
