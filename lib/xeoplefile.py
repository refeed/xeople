from __future__ import print_function


def parsefile(filepath):
    # type: (str) -> List
    peoplenames = []

    with open(filepath, 'r') as peoplefile:
        for line in peoplefile:
            stripped_newline = line.strip('\n')
            peoplenames.append(stripped_newline)

    return peoplenames
