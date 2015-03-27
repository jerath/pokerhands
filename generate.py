import sys
import csv
import fnmatch

"""
Dictionarys created by csv.DictReader for training file have the following format:
{'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '11', 'C4': '10'}
So Keys are: S1, S2, S3, S4, S5, C1, C2, C3, C4, C5 and hand (which is our class value)
"""

"""
Takes a dictionary describing a hand, and the size of the hand.
Generates a list of card values that are the same and different.
Eg. Given: {'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '9', 'C4': '10'}
Will return: [(2, '=', 5)] 
'=' = same value
'!' = different value
'e' = number of equal cards (includes duplicate counting)
"""
def equal_card( training_dict, hand_size ):
    same_set = []
    num_equ = 0

    #For each card in the hand
    for card in range(1,hand_size):
        #Look at the rest of the cards in the hand
        for next_card in range(card+1,hand_size+1):
            #print (card, next_card)

            #If the current card is the same as the next card, add them to the list
            if training_dict['C'+str(card)] == training_dict['C'+str(next_card)]:
                same_set += [(card, '=', next_card)]
                num_equ += 1
            else:
            	same_set += [(card, '!', next_card)]
            	
    same_set += [('e', num_equ)]

    return same_set

"""
Takes a dictionary describing a hand, and the size of the hand.
Generates a list containing the max, min, and avg card values. Assumes cards can not have a negative value.
Eg. Given: {'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '9', 'C4': '10'}
Will return: [('m', 10), ('n', 7), ('v', 8.6)] 
'm' = max
'n' = min
'v' = average
"""
def maxmin_card( training_dict, hand_size ):
    cur_max = -1
    cur_min = -1
    num_avg = 0
    
    for card in range(1,hand_size+1):
        if cur_max == -1:
            cur_max = training_dict['C'+str(card)]
        if cur_min == -1:
            cur_min = training_dict['C'+str(card)]
        if training_dict['C'+str(card)] > cur_max:
            cur_max = training_dict['C'+str(card)]
        if training_dict['C'+str(card)] < cur_min:
            cur_min = training_dict['C'+str(card)]

        num_avg += training_dict['C'+str(card)]

    num_avg = num_avg / hand_size

    return [('n', cur_min),('m', cur_max), ('v', num_avg)]

"""
Takes a dictionary describing a hand, and the size of the hand.
Generates a list of card suits that are the same and those that are differnent.
Eg. Given: {'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '9', 'C4': '10'}
Will return: [(2, '=', 5)] 
'#' = same suit
'%' = different suit
's' = number of same suit (includes duplicate counting)
"""
def equal_suit( training_dict, hand_size ):
    same_suit = []
    num_equ = 0

    #For each card in the hand
    for card in range(1,hand_size):
        #Look at the rest of the cards in the hand
        for next_card in range(card+1,hand_size+1):
            #print (card, next_card)

            #If the current card is the same as the next card, add them to the list
            if training_dict['S'+str(card)] == training_dict['S'+str(next_card)]:
                same_suit += [(card, '#', next_card)]
                num_equ += 1
            else:
            	same_suit += [(card, '%', next_card)]
            	
    same_suit += [('s', num_equ)]

    return same_suit

"""
Takes a dictionary describing a hand, and the size of the hand.
Generates a list of card values that are adjacent.
Eg. Given: {'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '9', 'C4': '10'}
Will return: [(1, '+', 2), (1, '+', 3), (1, '+', 5) (2, '+', 4), (4, '+', 5)] 
'+' = Adjacent ( +/- 1 from each other)
'a' = Number adjacent
"""
def adjacent_card( training_dict, hand_size ):
    adj_set = []
    num_adj = 0

    #For each card in the hand
    for card in range(1,hand_size):
        #Look at the rest of the cards in the hand
        for next_card in range(card+1,hand_size+1):
            #print (card, next_card)

            #If the current card is one greater or one less than the next card, add them to the list
            if (training_dict['C'+str(card)] == (training_dict['C'+str(next_card)]+1)) or (training_dict['C'+str(card)] == (training_dict['C'+str(next_card)]-1)):
                #print ('Theres something here...')
                adj_set += [(card, '+', next_card)]
                num_adj += 1
            elif((training_dict['C'+str(card)]%12) == (training_dict['C'+str(next_card)]%12)) and (training_dict['C'+str(card)] != training_dict['C'+str(next_card)]):
                adj_set += [(card, '+', next_card)]
                num_adj += 1

    adj_set += [('a',num_adj)]

    return adj_set

"""
Takes a list of dictionaries from training file.
Generates rules based on simple assumptions for every hand, and adds them to a dictionary of hand rules.
"""
def generate( training_reader ):

    hands = {}

    for line in training_reader:
        num_cards = 0
        card = []

        #Turn all the values in line into integers
        for key in line:
            line[key] = int(line[key])
            
            # get rid of the hand key
            if key != 'hand':
                card += [(key, line[key])]

            #Count number of cards in hand
            if fnmatch.fnmatch( key, 'C?'):
                num_cards += 1

        equ = equal_card( line, num_cards ) #Same and different values
        maxmin_num = maxmin_card( line, num_cards ) #Max, min and avg
        same = equal_suit( line, num_cards ) #Same and differnt suits
        adj = adjacent_card( line, num_cards ) #Adjacent cards

        #line['rules'] = same + adj #Not used

        #Add rules to respective hand classifications
        if str(line['hand']) not in hands.keys():
            hands[str(line['hand'])] = [equ+maxmin_num+same+adj+card]
        else:
            hands[str(line['hand'])].append(equ+maxmin_num+same+adj+card)
    return hands 

"""
Takes a dictionary of hand classes, which refer to lists of rules for indevidual hands.
For each class, for each hand in that class, compairs rule by rule and eliminates all rules that are not common to both.
Produces a minimum list of rules required to identify a hand classification with 100% coverage.
"""
def generalize( hands ):

    generalized_rules = {}

    for key in hands:
        print ('Hand : ' + key + ' Number: ' + str(len(hands[key])))
        # rules is the first hand in hands
        rules = hands[key][0]
        #print ('BASE HAND: ' +  str(hands[key][0]))
        for hand in hands[key]:
            #print ('TEST HAND: ' + str(hand))
            #print ('RULE HAND: ' + str(rules))
            
            new_rules = list(rules)
            for rule in rules:
                #print ('Looking at: ' + str(rule) )
                if rule not in hand:
                    new_rules.remove(rule)

            rules = list(new_rules)

        generalized_rules[key] = rules

    return generalized_rules

"""
Takes a list of hands to be classified, and the rules generated in training.
Generates rules for each hand to be classified and attempts to classify them using the rules.

-1: Could not classify.
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
"""
def classify( test_list, rules ):
    # test_list is a list of hand dicts
    # rules is a rules dictionary with key = hand class, value = list of rules
    count = 0
    classified = []
    # generate a rule for each thing in test list
    for hand in test_list:
        num_cards = 0
        card = []
        count += 1

        #Turn all the values in line into integers
        for key in hand:
            hand[key] = int(hand[key])
            
            # get rid of the hand key
            if key != 'hand':
                card += [(key, hand[key])]

            #Count number of cards in hand
            if fnmatch.fnmatch( key, 'C?'):
                num_cards += 1

        equ = equal_card( hand, num_cards )
        maxmin_num = maxmin_card( hand, num_cards )
        same = equal_suit( hand, num_cards )
        adj = adjacent_card( hand, num_cards )

        hand_rules = equ + maxmin_num + same + adj + card

        # for the rules for each hand
        # rule is key

        classification = '-1'

        for key in rules:

            new_rules = []
            for rule in rules[key]:
                if rule in hand_rules:
                    new_rules += [rule]

            #print 'hand ', hand_rules
            #print 'new ',new_rules
            #print 'old ',rules[key]

            if new_rules == rules[key]:
                #print 'WE MADE IT'
                if classification == '-1':
                    classification = key
                else:
                    if len(rules[key]) > len(rules[classification]):
                        classification = key

            # go through the list of rules for a hand
        
        classified += [{ 'id':count, 'class':classification}]

            # take the intersect.
            # if the intersect == the rule that we came up with for the hand class
            # then this is the rule.


    return classified
    # classify the hand based on the rules

    # for each rule in rules, take the intersection of the rules of the test hand and the rule.

    # the one it matches that has the most rules is the hand we choose..
    # add unclassified component? 

    # evaluate?

def evaluate( classification, test_list):
    num_right = 0
    num_wrong = 0
    
    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0
    s0 = s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = 0

    for i in range(0,len(test_list)):

        if int(test_list[i]['hand']) == 0:
            s0 += 1
        if int(test_list[i]['hand']) == 1:
            s1 += 1
        if int(test_list[i]['hand']) == 2:
            s2 += 1
        if int(test_list[i]['hand']) == 3:
            s3 += 1
        if int(test_list[i]['hand']) == 4:
            s4 += 1
        if int(test_list[i]['hand']) == 5:
            s5 += 1
        if int(test_list[i]['hand']) == 6:
            s6 += 1
        if int(test_list[i]['hand']) == 7:
            s7 += 1
        if int(test_list[i]['hand']) == 8:
            s8 += 1
        if int(test_list[i]['hand']) == 9:
            s9 += 1


        #print 'test ', test_list[i]['hand'], ' class ', classification[i]['class']

        if int(test_list[i]['hand']) == int(classification[i]['class']):
            if int(test_list[i]['hand']) == 0:
                c0 += 1
            if int(test_list[i]['hand']) == 1:
                c1 += 1
            if int(test_list[i]['hand']) == 2:
                c2 += 1
            if int(test_list[i]['hand']) == 3:
                c3 += 1
            if int(test_list[i]['hand']) == 4:
                c4 += 1
            if int(test_list[i]['hand']) == 5:
                c5 += 1
            if int(test_list[i]['hand']) == 6:
                c6 += 1
            if int(test_list[i]['hand']) == 7:
                c7 += 1
            if int(test_list[i]['hand']) == 8:
                c8 += 1
            if int(test_list[i]['hand']) == 9:
                c9 += 1
            num_right += 1
        else:
            num_wrong += 1
            #print (test_list[i])
            #print ('Expect: ' + str(test_list[i]['hand']) + ' Produced: ' + str(classification[i]['class']))

    print ('0: Right: ' + str(c0) + ' out of: ' + str(s0))
    print ('1: Right: ' + str(c1) + ' out of: ' + str(s1))
    print ('2: Right: ' + str(c2) + ' out of: ' + str(s2))
    print ('3: Right: ' + str(c3) + ' out of: ' + str(s3))
    print ('4: Right: ' + str(c4) + ' out of: ' + str(s4))
    print ('5: Right: ' + str(c5) + ' out of: ' + str(s5))
    print ('6: Right: ' + str(c6) + ' out of: ' + str(s6))
    print ('7: Right: ' + str(c7) + ' out of: ' + str(s7))
    print ('8: Right: ' + str(c8) + ' out of: ' + str(s8))
    print ('9: Right: ' + str(c9) + ' out of: ' + str(s9))

    return num_right, num_wrong

"""
Takes a list of dictinaries, corresponding to hands in the training file and a current mod_num (number to split on)
Separates out 1/10th of the training data as classified testing data.
Returns as list of training hands and a list of testing hands.
"""
def generate_test_training(training_list, mod_num):
    # use mod to split this list into a list of tests and 

    test_list = []
    train_list = []

    # every ith line goes to a test list, the rest to a training set
    for index in range(len(training_list)):
        if index %10 == mod_num:
            test_list.append(training_list[index])
        else:
            train_list.append(training_list[index])

    return test_list, train_list
    # training dictionaries go to generate and generalize

#WHEN RUNNING: First arg is training file.
def main():

    training_file = sys.argv[1]
    training_csv = open( training_file )
    training_reader = csv.DictReader(training_csv) #Creates a dict from rows in csvfile, using first row as keys

    training_list = []
    for line in training_reader:
        training_list.append(line)

    # divide training file into 10 parts
    for i in range(0,10):
        test_list, train_list = generate_test_training(training_list, i)
        
        hands = generate( train_list )

        # print (hands)
        rules = generalize( hands )

        # evaluate test data
        #print (' ++++++++++++++++++++ ', i , ' ++++++++++++++ ')
        #print (rules) 
        # compare evaluation to actual hand

        classification = classify(test_list, rules)
        right, wrong = evaluate(classification, test_list)

        print ('Right = ', right, ' Wrong = ', wrong)

if __name__ == "__main__":
    main()
