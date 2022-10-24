import csv
import sys


def main():
    usage = "Usage: python dna.py data.csv sequence.txt"

    # Check the command-line input
    if len(sys.argv) != 3:
        print(usage)
        exit(1)
    
    # Save filenames
    csvFile = sys.argv[1]
    txtFile = sys.argv[2]

    # Check the filename extensions
    if csvFile[len(csvFile) - 3:] != "csv" or txtFile[len(txtFile) - 3:] != "txt":
        print(usage)
        exit(1)
    
    # Read database file into a variable
    with open(csvFile) as db:
        reader = csv.reader(db)
        data = list(reader)
    
    # Read DNA sequence file into a variable
    with open(txtFile) as seq:
        sequence = seq.read()
    
    result = []
    subs = data[0][1:len(data)]

    # Find longest match of each STR in DNA sequence
    for sub in subs:
        result.append([sub, longestMatch(sequence, sub)])
    
    candidates = []
    for candidate in data[1:]:
        candidates.append([candidate[0], 0])

    # Check database for matching profiles
    for x, z in enumerate(result):
        for q, s in enumerate(data[1:]):
            if z[1] == int(s[x + 1]):
                candidates[q][1] += 1
    
    found = False
    
    # Print if the candidate is found
    for search in candidates:
        if len(result) == search[1]:
            found = True
            print(search[0])
    
    if not found:
        print("No match")
    
    exit(0)


def longestMatch(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize count of consecutive runs and the length of the subsequence
    lined, long = 0, len(subsequence)

    # Check for a subsequence match in a "substring" (a subset of characters) within sequence
    # If a match, move substring to next potential match in sequence
    # Continue moving substring and checking for matches until out of consecutive matches
    for x in enumerate(sequence):

        # If there is a match in the substring
        if sequence[x[0]:x[0] + long] == subsequence:
            z, line = x[0], 1

            while sequence[z:z + long] == sequence[z + long:z + long * 2]:
                # Adjust substring start and end
                z += long
                line += 1
            
            # Update most consecutive matches found
            if line > lined:
                lined = line
    
    # After checking for runs at each character in seqeuence
    # Return longest run found
    return lined


if __name__ == "__main__":
    main()