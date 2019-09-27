/**
 * Student name:    Nguyễn Trung Tính
 * Student ID:      1713521
 */

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type

    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

                /************
                *   LEXER   *
                ************/

fragment Letter      : [a-zA-Z];

fragment Digit       : [0-9];

fragment Exponent    : [eE] SUB? Digit+ ;

fragment Underscore  : '_';

fragment Dot         : '.';

                /************
                * LITERALS  *
                ************/

INTLIT              : Digit+;
FLOATLIT            : ( Digit+ (Dot | Dot? Exponent) Digit* ) | ( Digit* Dot Digit+ ( | Exponent) );
BOOLEANLIT          : TRUE | FALSE; 
STRINGLIT           : '"' ( '\\' [btnfr"\\] | ~["\r\n\\] )* '"' { self.text = self.text[1:-1] };

                /************
                *  KEYWORDS *
                ************/

BOOLEANTYPE         : 'boolean';
BREAK               : 'break';
CONTINUE            : 'continue';
ELSE                : 'else';
FOR                 : 'for';
FLOATTYPE           : 'float';
IF                  : 'if';
INTTYPE             : 'int' ;
RETURN              : 'return';
VOIDTYPE            : 'void' ;
DO                  : 'do';
WHILE               : 'while';
TRUE                : 'true';
FALSE               : 'false';
STRINGTYPE          : 'string'; 

                /**************
                * IDENTIFIERS *
                **************/

ID : ( Underscore | Letter )( Underscore | Letter | Digit )*;

                /************
                * OPERATORS *
                ************/

ADD                 : '+';
SUB                 : '-';
MUL                 : '*';
DIV                 : '/';
NOT                 : '!';
MOD                 : '%';
OR                  : '||';
AND                 : '&&';
NEQ                 : '!=';
EQ                  : '==';
LESS                : '<';
GRATER              : '>';
LEQ                 : '<=';
GEQ                 : '>=';
ASSIGN              : '=';
   
                /*************
                * SEPARATORS *
                *************/

LP                  : '(';
RP                  : ')';
LB                  : '{';
RB                  : '}';
LSB                 : '[';
RSB                 : ']';
SEMI                : ';';
CM                  : ',';


                /************
                *  COMMENT  *
                ************/

BLOCK_COMMENT       : '/*' .*? '*/' -> skip;
LINE_COMMENT        : '//' ~[\r\n]* -> skip;
WS                  : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

                /************
                *   ERROR   *
                ************/

ILLEGAL_ESCAPE      : '"' ( '\\' [btnfr"\\] | ~[\\"\n\r])* ('\\' ~[btnfr"\\]) {self.text =  self.text.lstrip('"')};

UNCLOSE_STRING      : '"' ( '\\' [btnfr"\\] | ~[\r\n\\"] )*('\\')? { self.text = self.text.lstrip('"') };

ERROR_CHAR          : .;

                /************
                *  PARXER   *
                ************/   

program             : manydecls EOF;
manydecls           : decl (decl)* ;
decl                : variable_decl | function_decl ;
variable_decl       : primitive_type many_variables SEMI ;
primitive_type      : INTTYPE | FLOATTYPE | BOOLEANTYPE | STRINGTYPE ;
many_variables      : variable (CM variable)* ;
variable            : ID (LSB INTLIT RSB)? ;

function_decl       : func_type ID LP parameter_list RP block_statement ;
func_type           : primitive_type | VOIDTYPE | output_array_pointer_type ;
parameter_list      : (parameter_decl (CM parameter_decl)*)? ;
parameter_decl      : primitive_type ID (LSB RSB)? ;
var_stmt_list       : (var_stmt var_stmt*) ? ;
var_stmt            : variable_decl | statement ;

array                       : primitive_type ID LSB INTLIT RSB;
array_pointer_type          : input_array_pointer_type | output_array_pointer_type;
input_array_pointer_type    : primitive_type ID LSB RSB;
output_array_pointer_type   : primitive_type LSB RSB;

expr                : expr1 ASSIGN expr | expr1;
expr1               : expr1 OR expr2 | expr2;
expr2               : expr2 AND expr3 | expr3;
expr3               : expr4 (EQ | NEQ) expr4 | expr4;
expr4               : expr5 (LESS | LEQ | GRATER | GEQ) expr5 | expr5;
expr5               : expr5 (ADD | SUB) expr6 | expr6;
expr6               : expr6 (DIV | MUL | MOD) expr7 | expr7;
expr7               : (SUB | NOT) expr7 | expr8;
expr8               : expr9 LSB expr RSB | expr9;
expr9               : LP expr RP | operands;
operands            : literal | ID | func_call;
literal             : INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT;

func_call           : ID LP exprlist RP;
exprlist            : (expr (CM expr)*) ? ;

statement           : if_stmt 
                    | for_stmt 
                    | dowhile_stmt 
                    | break_stmt 
                    | continue_stmt 
                    | return_stmt 
                    | expr_stmt
                    | block_statement
                    ;
if_stmt             : IF LP expr RP statement (ELSE statement)?;

dowhile_stmt        : DO statement+ WHILE expr SEMI;

for_stmt            : FOR LP expr SEMI expr SEMI expr RP statement;

break_stmt          : BREAK SEMI;

continue_stmt       : CONTINUE SEMI;

return_stmt         : RETURN expr? SEMI;

expr_stmt           : expr SEMI;

block_statement     : LB var_stmt_list RB ;