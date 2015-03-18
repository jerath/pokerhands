####Conventions:
* EQU: = 
* NEQ: !
* ADJ: +

Files will be indented with ** 2 spaces **.

###Generate:
**Input:** a csv file of 5 card hands: each card has a suit and a rank, and each hand has a class.

Example: header and first three rows of train.csv
```
id,S1,C1,S2,C2,S3,C3,S4,C4,S5,C5
1,1,10,2,2,3,3,3,8,1,1
2,2,13,3,5,3,7,4,6,1,4
3,1,3,1,11,2,8,2,1,2,4
```
**Output:** a data structure containing the rules and classification for each hand.

**Objective:**
Generates rules based on adjacency, rank equivalence, and suits for each hand.

###Generalize:
**Input:** a data structure containing the rules and classification for each hand (the output from generate).

**Output:** a data structure containing general rules for each classification of hand (0-9)?

**Objective:**
* Take each class one at a time and calculate coverage of rules.
* Consider the count of =, !, +, suits.
* Consider: how… exactly... are you going to tell it to not do 100% coverage for class 0. Stop, at some point?

### Evaluate:
**Input:** a test file with unclassified hands and general classification rules for each hand (output of generate).

**Output:** a csv file with the ids and hands of newly classified tuples. Should look like the [sample submission](https://github.com/jerath/pokerhands/blob/master/sampleSubmission.csv).

**Objective:**
* Use the general rules to evaluate new tuples.
* Find the closest rule.


