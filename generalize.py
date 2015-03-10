import sys
import csv








#WHEN RUNNING: First arg is training rules.
def main():

    rules_file = sys.argv[1]
    rules_csv = open( rules_file )
    rules_reader = csv.DictReader(rules_csv) #Creates a dict from rows in rules_csv, using first row as keys



if __name__ == "__main__":
    main()
