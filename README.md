# ProgLangProj
Project for Organization of Programming Languages

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
We tested the program with the input `2x^2+4x-5` but after repeated troubleshooting we were still unable to get it to parse correctly:
![image](https://user-images.githubusercontent.com/39973276/116422085-648dfc00-a80d-11eb-8eb6-7477060aa455.png)
