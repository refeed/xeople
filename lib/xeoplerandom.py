from random import choice


def random_select(people_names):
    '''Select random str from list(str)'''
    # type: (List[str]) -> str
    selected_people = choice(people_names)
    return selected_people


def group_random_select(people_names, many_groups, many_people_in_group=None):
    # type (List[str], int) -> List[List[str]]
    # Divide people names into group

    # Count how many people will be grouped in each group
    if many_people_in_group is None:
        many_people_in_group = len(people_names) / many_groups

    # Count how many people that left
    people_left = len(people_names) % many_groups

    # Create list depends on how many groups are
    groups = []
    for i in range(many_groups):
        groups.append([])

    # Insert people_names into a group by random
    for i in range(len(groups)):
        for j in range(many_people_in_group):
            # Insert until many_people reached
            selected_people = choice(people_names)
            groups[i].append(selected_people)
            people_names.remove(selected_people)

        if not people_left == 0:
            people_left -= 1
            selected_people = choice(people_names)
            groups[i].append(selected_people)
            people_names.remove(selected_people)

    return groups
