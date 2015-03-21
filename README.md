####Conventions:
* CARDEQU: = 
* CARDNEQ: !
* CARDADJ: +
* SUITEQU: #
* SUITNEQ: %

Files will be indented with **4 spaces**.

See contest details [here](https://www.kaggle.com/c/poker-rule-induction).

###Generate:
**Input:** a csv file of 5 card hands: each card has a suit and a rank, and each hand has a class.

Example: header and first three rows of train.csv
```
S1,C1,S2,C2,S3,C3,S4,C4,S5,C5,hand
4,9,2,1,2,2,4,7,2,8,0
1,4,3,6,1,12,3,11,2,7,0
1,11,4,1,3,7,4,11,2,1,2
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
**Input:** a [test file](https://raw.githubusercontent.com/jerath/pokerhands/master/test.csv) with unclassified hands and general classification rules for each hand (output of generate).

**Output:** a csv file with the ids and hands of newly classified tuples. Should look like the [sample submission](https://raw.githubusercontent.com/jerath/pokerhands/master/sampleSubmission.csv).

**Objective:**
* Use the general rules to evaluate new tuples.
* Find the closest rule.

Hand classification:
```
0: Nothing in hand; not a recognized poker hand 
1: One pair; one pair of equal ranks within five cards
2: Two pairs; two pairs of equal ranks within five cards
3: Three of a kind; three equal ranks within five cards
4: Straight; five cards, sequentially ranked with no gaps
5: Flush; five cards with the same suit
6: Full house; pair + different rank three of a kind
7: Four of a kind; four equal ranks within five cards
8: Straight flush; straight + flush
9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush
```

