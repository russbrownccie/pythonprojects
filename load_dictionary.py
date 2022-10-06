"""Load a text file as a list
Arguments: -text - File Name (and directory path if needed)

Exceptions: IO Error if filename not found

Returns: A list of all the words in a text file in lower case

Requires - import sys

"""

import sys


def load(file):
    """Open a text file and return a list of all lowercase strings"""

    try:
        with open(file) as in_file:
            temp_list = in_file.readlines()
            word_list = [item.lower().strip("\n") for item in temp_list]
        return word_list

    except IOError:
        print(f"Error opening {file}.  Terminating program", file=sys.stderr)
        sys.exit(1)
