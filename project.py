from ply import lex, yacc
import cmath as math

# List of token names.   This is always required
tokens = (
    'ZERO',
    'ONE',
    'TWO',
    'NUMBER',
    'VARIABLE',
    'PLUS',
    'MINUS',
    'CARAT', 
    'SIGN'
)

# Regular expression rules for simple tokens
t_ZERO = r'0'
t_ONE = r'1'
t_TWO = r'2'
t_PLUS = r'\+'
t_MINUS = r'-'
t_VARIABLE = r'[a-zA-Z]'
t_CARAT = r'\^'
t_SIGN = r'\+|-'

# A regular expression rule with some action code

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
# data = '''
# 2x^2+4x - 5 %
# '''

# Give the lexer some input
# lexer.input(data)

# for tok in lexer:
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)

quad={}



def p_expr(t):
    '''expr : term2 term1 term0
    '''
    print(f'Solution 1 : {quad["sol1"]}')
    print(f'Solution 2 : {quad["sol2"]}')

def p_expr_term21(t):
    '''term21 : VARIABLE CARAT TWO
            | MINUS VARIABLE CARAT TWO
            | PLUS VARIABLE CARAT TWO'''
    
    if (t[1] == '-'):
        quad['a'] = -1
    else:
        quad['a'] = 1

    
def p_expr_term2(t):
    '''term2 : PLUS NUMBER VARIABLE CARAT TWO
            | MINUS NUMBER VARIABLE CARAT TWO
            | NUMBER VARIABLE CARAT TWO
            | term21'''
    
    if (t[1] == '+'):
        quad['a'] = t[2]
    elif(t[1] == '-'):
        quad['a'] = t[2] * -1
    else:
        quad['a'] = t[1]

def p_expr_term11(t):
    '''term11 : CARAT ONE
            | empty
            '''
    
    if (t[1].type == 'CARAT' and t[2].type == 'ONE'):
        pass

def p_expr_term13(t):
    '''term13 : NUMBER VARIABLE
            | VARIABLE
            '''
    
    if (t[1].type == 'NUMBER'):
        quad['b'] = t[1]
    else:
        quad['b'] = 1

def p_expr_term14(t):
    '''term14 : MINUS VARIABLE
            | PLUS VARIABLE
            '''
    
    if (t[1] == '-'):
        quad['b'] = -1
    else:
        quad['b'] = 1

def p_expr_term1(t):
    '''term1 : PLUS NUMBER VARIABLE term11
            | MINUS NUMBER VARIABLE term11
            | term13
            | term14
            | empty'''
    
    if (t[1] == '+'):
        quad['b'] = t[2]
    elif(t[1] == '-'):
        quad['b'] = t[2] - 2 * t[2]
    else:
        quad['b'] = 0

def p_expr_term0(t):
    '''term0 : PLUS NUMBER VARIABLE CARAT ZERO
            | MINUS NUMBER VARIABLE CARAT ZERO
            | PLUS NUMBER
            | MINUS NUMBER
            | empty'''
    
    if (t[1] == '+'):
        quad['c'] = t[2]
    elif(t[1] == '-'):
        quad['c'] = t[2] - 2 * t[2]
    else:
        quad['c'] = 0

    a = quad['a']
    b = quad['b']
    c = quad['c']

    quad['sol1'] = (-b - math.sqrt((b**2) - (4 * a * c)) / (2 * a))
    quad['sol2'] = (-b + math.sqrt((b**2) - (4 * a * c)) / (2 * a))

def p_empty(t):
     'empty :'
     pass

def p_error(t):
    print(f"Syntax error at '{t.value}'")
    print(t)

parser = yacc.yacc()

while True:
    try:
        w = input('>')
    except EOFError:
        break
    parser.parse(w)