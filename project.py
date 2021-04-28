from ply import lex, yacc
import cmath as math

''' 
expr : term2 term1 term0
term2 : SIGN NUMBER VARIABLE CARAT 2
term1 : SIGN NUMBER VARIABLE term1a
term1a : CARAT 1 | empty
term0 : SIGN NUMBER term0a
term0a : VARIABLE CARAT 0 | empty
'''

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'VARIABLE',
    'PLUS',
    'MINUS',
    'CARAT',
    'SIGN'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_VARIABLE = r'[a-zA-Z]'
t_CARAT = r'\^'
t_SIGN = r'-|\+'

# A regular expression rule with some action code


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
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
    '''expr : term2 term1 term0'''
    print(f'Solution 1 : {quad["sol1"]}')
    print(f'Solution 2 : {quad["sol2"]}')

def p_expr_term2(t):
    '''term2 : SIGN NUMBER VARIABLE CARAT NUMBER'''

    if (t[5] == 2):
        if (t[1] == '+'):
            quad['a'] = t[2]
        elif(t[1] == '-'):
            quad['a'] = t[2] * -1
    else:
        #throw some error?
        quad['a'] = -1
    
def p_expr_term1a(t):
    '''term1a : CARAT NUMBER
            | empty'''

    if (t[1] == '^'):
        if(t[2] == '1'):
            pass
    else:
        #error?
        pass
        #quad['b'] = -1

def p_expr_term1(t):
    '''term1 : SIGN NUMBER VARIABLE term1a'''
    
    if (t[1] == '+'):
        quad['b'] = t[2]
    elif(t[1] == '-'):
        quad['b'] = t[2] * -1
    elif(t[1] == ''):
        quad['b'] = 0
    else:
        #throw some error?
        quad['b'] = -1

def p_expr_term0a(t):
    '''term0a : VARIABLE CARAT NUMBER
            | empty '''

    if (t[1] == 'x'):
        if(t[3] == '0'):
            pass
    else:
        #error?
        pass
        #quad['c'] = -1
    
def p_expr_term0(t):
    '''term0 : SIGN NUMBER term0a'''
    
    if (t[1] == '+'):
        quad['c'] = t[2]
    elif(t[1] == '-'):
        quad['c'] = t[2] * -1
    elif (t[1] == ''):
        quad['c'] = 0
    else:
        #throw some error?
        quad['c'] = -1

    a = quad['a']
    b = quad['b']
    c = quad['c']

    quad['sol1'] = (-b - math.sqrt((b**2) - (4 * a * c)) / (2 * a))
    quad['sol2'] = (-b + math.sqrt((b**2) - (4 * a * c)) / (2 * a))

def p_error(t):
    print(f"Syntax error at '{t.value}'")
    print(t)

def p_empty(t):
    'empty :'
    pass

parser = yacc.yacc()

while True:
    try:
        w = input('>')
    except EOFError:
        break
    parser.parse(w)