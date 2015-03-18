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
def equal( training_dict, hand_size ):
    same_set = []

    #For each card in the hand
    for card in range(1,hand_size):
        #Look at the rest of the cards in the hand
        for next_card in range(card+1,hand_size+1):
            #print (card, next_card)

            #If the current card is the same as the next card, add them to the list
            if training_dict['C'+str(card)] == training_dict['C'+str(next_card)]:
                same_set += [(card, '=', next_card)]

    return same_set

"""
Takes a dictionary describing a hand, and the size of the hand.
Generates a list of card values that are adjacent.

Eg. Given: {'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '9', 'C4': '10'}
Will return: [(1, '+', 2), (1, '+', 3), (1, '+', 5) (2, '+', 4), (4, '+', 5)] 
This indicates card 1 is adjacent to 2, 1 is adjacent to 3, 1 is adjacent to 5, 2 is adjacent to 4, and 4 is adjacent to 5

"""
def adjacent( training_dict, hand_size ):
    adj_set = []

    #For each card in the hand
    for card in range(1,hand_size):
        #Look at the rest of the cards in the hand
        for next_card in range(card+1,hand_size+1):
            #print (card, next_card)

            #If the current card is one greater or one less than the next card, add them to the list
            if (training_dict['C'+str(card)] == training_dict['C'+str(next_card)]+1) or (training_dict['C'+str(card)] == training_dict['C'+str(next_card)]-1):
                #print ('Theres something here...')
                adj_set += [(card, '+', next_card)]

    return adj_set

"""
Takes a dictionary reader (reading from a csv file).
Generates rules based on simple assumptions for every hand, and adds them to a dictionary of hand rules.

"""
def generate( training_reader ):
    global hands

    for line in training_reader:
        num_cards = 0

        #Turn all the values in line into integers
        for key in line:
            line[key] = int(line[key])

            #Count number of cards in hand
            if fnmatch.fnmatch( key, 'C?'):
                num_cards += 1

        same = equal( line, num_cards )
        adj = adjacent( line, num_cards )

        line['rules'] = same + adj

        #Add rules to respective hand classifications
        if str(line['hand']) not in hands.keys():
            hands[str(line['hand'])] = [same+adj]
        else:
            hands[str(line['hand'])].append(same+adj)

#WHEN RUNNING: First arg is training file.
def main():
    global hands

    training_file = sys.argv[1]
    training_csv = open( training_file )
    training_reader = csv.DictReader(training_csv) #Creates a dict from rows in csvfile, using first row as keys

    generate( training_reader )

    print hands

if __name__ == "__main__":
    main()
