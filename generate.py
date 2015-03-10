import sys
import csv

def equal( training_dict ):

    return 0

def adjacent( training_dict ):

    return 0


def generate( training_reader ):

    for line in training_reader:
        equal( line )
        adjacent( line )







#WHEN RUNNING: First arg is training file.
def main():

    training_file = sys.argv[1]
    training_csv = open( training_file )
    training_reader = csv.DictReader(training_csv) #Creates a dict from rows in csvfile, using first row as keys

    generate( training_reader )


if __name__ == "__main__":
    main()
