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



Modified Grammar
![Modified grammar](https://user-images.githubusercontent.com/39973276/116420382-ebda7000-a80b-11eb-9c06-0888cf1072c3.jpg)

# Program and Testing
![image](https://user-images.githubusercontent.com/39973276/116469022-9a4bd880-a83f-11eb-8367-ab2e9e422a4a.png)
To run, we simply enter a valid quadratic equation, like the ones below, then the program will display its roots.
We tested the program with these inputs and you are able to see the output in the screenshot above:
- `+2x^2+4x-4` (valid input)
- `-5x^2-3+17` (invalid input, displays error)
- `-5x^2-3x+17` (valid input)
