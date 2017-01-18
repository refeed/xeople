from __future__ import print_function
from random import choice


class ShellColors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


INDIVIDUAL_PATTERNS = ['Here is the lucky people who get selected: %s',
                       'Result: %s',
                       'The lucky people is: %s']


def print_individual(people_name):
    # type: (str) -> None
    selected_pattern = choice(INDIVIDUAL_PATTERNS)
    output = selected_pattern % (people_name,)
    print(ShellColors.OKGREEN + output + ShellColors.ENDC)


def print_group(groups):
    # type: (List[List[str]]) -> None
    output = ""

    for group_number in range(len(groups)):
        output += (ShellColors.WARNING + "========\nGROUP %d\n========\n" %
                   (group_number + 1,) + ShellColors.ENDC)

        # List all people name in the group
        people_number = 1  # Used to give number before the name of the people
        for people_name in groups[group_number]:
            output += "%d. %s\n" % (people_number, people_name,)
            people_number += 1

        # Add a newline
        output += "\n"

    print(output)
