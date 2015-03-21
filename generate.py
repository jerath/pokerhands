import sys
import csv
import fnmatch

"""
Dictionarys created by csv.DictReader for training file have the following format:
{'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '11', 'C4': '10'}
So Keys are: S1, S2, S3, S4, S5, C1, C2, C3, C4, C5 and hand (which is our class value)
"""

hands = {} #Dict of hand types, with list of rules for each hand of that type

"""
Takes a dictionary describing a hand, and the size of the hand.
Generates a list of card values that are the same.
Eg. Given: {'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '9', 'C4': '10'}
Will return: [(2, '=', 5)] 
This indicates card 2 is the same as card 5.
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
This indicates card 1 is adjacent to 2, 1 is adjacent to 3, 1 is adjacent to 5, 2 is adjacent to 4, and 4 is adjacent to 5
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
            if (training_dict['C'+str(card)] == training_dict['C'+str(next_card)]+1) or (training_dict['C'+str(card)] == training_dict['C'+str(next_card)]-1):
                #print ('Theres something here...')
                adj_set += [(card, '+', next_card)]
                num_adj += 1
            elif((training_dict['C'+str(card)]%12) == (training_dict['C'+str(next_card)]%12)) and (training_dict['C'+str(card)] != training_dict['C'+str(next_card)]):
                adj_set += [(card, '+', next_card)]
                num_adj += 1

    adj_set += [('a',num_adj)]

    return adj_set

"""
Takes a dictionary reader (reading from a csv file).
Generates rules based on simple assumptions for every hand, and adds them to a dictionary of hand rules.
"""
def generate( training_reader ):
    global hands

    for line in training_reader:
        num_cards = 0
        card = []

        #Turn all the values in line into integers
        for key in line:
            line[key] = int(line[key])
            card += [(key, line[key])]

            #Count number of cards in hand
            if fnmatch.fnmatch( key, 'C?'):
                num_cards += 1

        equ = equal_card( line, num_cards )
        same = equal_suit( line, num_cards )
        adj = adjacent_card( line, num_cards )

        #line['rules'] = same + adj #Not used

        #Add rules to respective hand classifications
        if str(line['hand']) not in hands.keys():
            hands[str(line['hand'])] = [equ+same+adj+card]
        else:
            hands[str(line['hand'])].append(equ+same+adj+card)

def generalize():
    global hands
    generalized_rules = {}

    for key in hands:
        # rules is the first hand in hands
        rules = hands[key][0]
        for hand in hands[key]:
            new_rules = rules
            for rule in rules:
                if rule not in hand:
                    new_rules.remove(rule)
            rules = new_rules
        generalized_rules[key] = rules

    print generalized_rules

def generate_test_training(training_list, mod_num):
    # use mod to split this list into a list of tests and 

    test_list = []
    train_list = []
    for index in range(len(training_list)):
        if index % 10 == mod_num:
            test_list.append(training_list[index])
        else:
            train_list.append(training_list[index])

    return test_list, train_list
    # training dictionaries go to generate and generalize



#WHEN RUNNING: First arg is training file.
def main():
    global hands

    training_file = sys.argv[1]
    training_csv = open( training_file )
    training_reader = csv.DictReader(training_csv) #Creates a dict from rows in csvfile, using first row as keys

    training_list = []
    for line in training_reader:
        training_list.append(line)

    for i in range(0,10):
        test_list, train_list = generate_test_training(training_list, i)

        generate( train_list )

        # print (hands)
        generalize()

        # evaluate test data

        # compare evaluation to actual hand

if __name__ == "__main__":
    main()
