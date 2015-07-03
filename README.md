###Overview
This project is a hand-rolled Python classifier for learning and classifying poker hands for the [Poker Rule Induction Kaggle competition](https://www.kaggle.com/c/poker-rule-induction).

At the height of its glory, our classifier peaked at 99.8% accuracy, and debuted on the Kaggle leaderboard at #37 out of 117 entries. Unfortunately, that remaining 0.2% is forever beyond our reach; without heavy feature engineering, the "sometimes wrap, sometimes not" characteristic of Aces in straights make it impossible to push our algorithm to 100%. You can read more about that in the Challenges section of our report.

###Our approach
1. Generate a set of observations about card rank and suits for each hand in the training set.
  * Example: In a training hand, we can observe cards 1 and 2 have a consecutive rank; cards 4 and 5 have the same suit; cards 2, 3, and 4 have the same rank... etc
1. Use these observations to generalize a set of rules that are true for all hands of each class in the training set.
  * Example: The only rule for the pair class is that two cards in the hand must have the same rank.
1. Evaluate the training set against these rules.
  * Example: Which is the most specific rule set that applies to each hand (4 of a kind being more specific than a pair)?

### More information
For technical details and process, check out the [ report](https://github.com/jerath/pokerhands/blob/master/PokerHandReport.pdf).

For a concise summary, check out the [ slide-deck](https://github.com/jerath/pokerhands/blob/master/PokerHandSlides.pdf).

Or of course, jump straight to the code.

##### Contributors: [Jessica Thomas](https://github.com/jerath), [Alan Dodge](https://github.com/Smesworld), and Spencer McEwan.
