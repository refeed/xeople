#!/usr/bin/env python
from __future__ import print_function

from lib.xeoplefile import parsefile
from lib.xeoplerandom import random_select, group_random_select
from lib.xeopleprint import print_individual, print_group

import optparse
import sys


def main():
    usage = '''
        ./main.py <people names file>

        Example: ./main.py people_names.txt

        To use the group mode use:

        ./main.py <people names file> --group <how many groups will be created>

        See README.md for more context.
        '''

    parser = optparse.OptionParser(usage=usage)
    parser.add_option('--group',
                      action='store',
                      help='Group mode, how many groups will be created')
    (options, args) = parser.parse_args()

    if len(args) == 0:
        print('You must specify a file name that contains people file names!')
        sys.exit(1)

    # Extract first argument to people_file
    people_file = args[0]

    # Parse file to get people names
    people_names = parsefile(people_file)

    if options.group is not None:
        groups = group_random_select(people_names, int(options.group))
        print_group(groups)
    else:
        selected_people = random_select(people_names)
        print_individual(selected_people)

if __name__ == '__main__':
    main()
