# Organization of Programming Languages Final Project

# Work Distribution
Joshua created the alphabet, language, and lexer. James worked primarily on the grammar and parser.

# Alphabet 
{var: Variable name [a-z][A-Z], num: Integer [0-9][0-9]*, op: operators [+ | - | ^]}

# Language
Input will have no spaces and follow this format exactly: {op}{num}{op}{var}{op}{num}{var}{op}{num} 
Assuming the terms are in order

# Grammar
[Link to initial grammar](https://github.com/JC2615/ProgLangProj/files/6392494/grammar.pdf) 



Modified Grammar:
```
<expr>        -> <term2>  <term1>  <term0>
<term2>       ->  <sign>  <number>  <variable>  <karat>  <two>
<term1>       ->  <sign>  <number>  <variable>  <term1a>
<term1a>      ->  <karat>  <one> |  𝛆
<term0>       ->  <sign>  <number>  <term0a>
<term0a>      ->  <variable>  <karat>  <zero> | 𝛆
<sign>        ->  “+” | “-”
<number>      ->  <number> <number> | <number> 𝛆 | “0” | “1” | “2” | “3” | “4” | “5” | “6” | “7” | “8” | “9”
<variable>    -> “x”
<karat>       ->  “^”
<two>         ->  “2”
<one>         ->  “1”
<zero>        ->  “0”
```

# Parse Tree
Here is an example of the parse tree that would be created if we gave the input `+2x^2+4x - 4 `
![image](https://user-images.githubusercontent.com/39973276/116474269-4b557180-a846-11eb-9ea4-8c0fffa2c370.png)


# Program and Testing
![image](https://user-images.githubusercontent.com/39973276/116469022-9a4bd880-a83f-11eb-8367-ab2e9e422a4a.png)
To run, we simply enter a valid quadratic equation, like the ones below, then the program will display its roots.
We tested the program with these inputs and you are able to see the output in the screenshot above:
- `+2x^2+4x-4` (valid input)
- `-5x^2-3+17` (invalid input, displays error)
- `-5x^2-3x+17` (valid input)
