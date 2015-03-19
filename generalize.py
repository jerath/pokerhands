# this file is tabbed with 2 spaces.
# if you edit it, make sure your tabs are spaces, not just tab-width two spaces.
# otherwise we'll spend forever trying to hunt down and fix indentation bugs :(

# Objective:
# take each hand one at a time and calculate the coverage of rules.
# consider the count of + and = and determine what all hands have in common.
# output the rule set for each type of hand. (ie, what makes a pair?)

import sys
import csv

# a file containing a dictionary of every rule ever.
import every_rule_ever


# this is removed from main so we don't have to think about exactly 
# where the rules will come from.
def get_rules():
  return every_rule_ever.rules


#WHEN RUNNING: First arg is training rules.
def main():

  rules = get_rules()

  # TASK:
  # for each set of rules, find the common theme. 100% coverage.
  # number of adjacencies?
  # number of rank equals?
  # number of suit equals?
  # presence of certain cards?

  # how can the rules be collapsed.
  # the key is the hand
  for key in rules:
    if key is '1':
      # rules[key] is the list of all rules associated with that hand
      for rule_set in rules[key]:
        
        print rule_set

  # rules_file = sys.argv[1]
  # rules_csv = open( rules_file )
  # rules_reader = csv.DictReader(rules_csv) #Creates a dict from rows in rules_csv, using first row as keys



if __name__ == "__main__":
  main()





2