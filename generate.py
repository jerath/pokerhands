import sys
import csv
import fnmatch

"""
Dictionarys created by csc.DictReader for training file have the following format:
{'S3': '2', 'S2': '4', 'S1': '4', 'S5': '4', 'S4': '1', 'C3': '7', 'C2': '9', 'C1': '8', 'hand': '4', 'C5': '11', 'C4': '10'}
So Keys are: S1, S2, S3, S4, S5, C1, C2, C3, C4, C5 and hand (which is our class value)
"""

hands = {} #Dict of hand types, with list of rules for each hand of that type

def equal( training_dict, hand_size ):
    same_set = []

    for card in range(1,hand_size):
        for next_card in range(card+1,hand_size+1):
            #print (card, next_card)
            if training_dict['C'+str(card)] == training_dict['C'+str(next_card)]:
                #print ('Theres something here...')
                same_set += [(card, '=', next_card)]

    return same_set

def adjacent( training_dict, hand_size ):
    adj_set = []

    for card in range(1,hand_size):
        for next_card in range(card+1,hand_size+1):
            #print (card, next_card)
            if (training_dict['C'+str(card)] == training_dict['C'+str(next_card)]+1) or (training_dict['C'+str(card)] == training_dict['C'+str(next_card)]-1):
                #print ('Theres something here...')
                adj_set += [(card, '+', next_card)]

    return adj_set


def generate( training_reader ):
    global hands

    for line in training_reader:
        num_cards = 0

        for key in line:
            line[key] = int(line[key])

            if fnmatch.fnmatch( key, 'C?'):
                num_cards += 1

        same = equal( line, num_cards )
        adj = adjacent( line, num_cards )

        line['rules'] = same + adj

        #print line
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
