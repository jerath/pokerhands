Conventions:
EQU: = 
NEQ: !
ADJ: +

***Ignore data types used in examples. 

***Need some metric for suits

GENERATE RULES:
Input: a csv file with a header row https://www.kaggle.com/c/poker-rule-induction/data
Output: TBD by generalize rules. A file with stuff. Depends on properties of csv file.

Objective:
Read input from a file
Sorting the data based on different classes (perhaps a new file)
Counting the number of each class (to compute coverage later)
Generate all the (long form) rules that we will be using: =, !, +, suits (discuss with rule generalizer). 
Refine based on transitive equality and linear relationships
Ex. 1 1 1 2 3 -> (R1 = R2), (R1 = R3), (R3 + R4), (R4 + R5)
Note: Might be easier to generate = first, and then !. Entirely up to you.
Your end product is the minimum list of rules that exactly describes that hand.
Your output has the rules and the sorted classes.
Ex. [(R1 = R2), (R1 = R3), (R3 + R4), (R4 + R5)], class = 3 of a kind.

GENERALIZE RULES:
Input: <output from generating rules> YOU GET TO DECIDE WHAT IT LOOKS LIKE
Output: discuss with class evaluator

Objective:
Take each class one at a time and calculate coverage of rules.
Consider the count of =, !, +, suits (discuss with rule generator).
Consider: how… exactly... are you going to tell it to not do 100% coverage for class 0. Stop, at some point?

EVALUATE:
Input: some combination of tuples and dictionaries, maybe? discuss with rule generalizer, and a file of new tuples
Output: the evaluated class

Objective:
Take new tuples and evaluate them based on the rules.
Must be able to compute new rules 
Find the closest rule.


