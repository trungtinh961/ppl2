# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#manydecls.
    def visitManydecls(self, ctx:MCParser.ManydeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable_decl.
    def visitVariable_decl(self, ctx:MCParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#many_variables.
    def visitMany_variables(self, ctx:MCParser.Many_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_decl.
    def visitFunction_decl(self, ctx:MCParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_type.
    def visitFunc_type(self, ctx:MCParser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter_list.
    def visitParameter_list(self, ctx:MCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#parameter_decl.
    def visitParameter_decl(self, ctx:MCParser.Parameter_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_stmt_list.
    def visitVar_stmt_list(self, ctx:MCParser.Var_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_stmt.
    def visitVar_stmt(self, ctx:MCParser.Var_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array.
    def visitArray(self, ctx:MCParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#input_array_pointer_type.
    def visitInput_array_pointer_type(self, ctx:MCParser.Input_array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#output_array_pointer_type.
    def visitOutput_array_pointer_type(self, ctx:MCParser.Output_array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr1.
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr2.
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr3.
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr4.
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr5.
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr6.
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr7.
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr8.
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr9.
    def visitExpr9(self, ctx:MCParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exprlist.
    def visitExprlist(self, ctx:MCParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MCParser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_stmt.
    def visitExpr_stmt(self, ctx:MCParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return self.visitChildren(ctx)



del MCParser