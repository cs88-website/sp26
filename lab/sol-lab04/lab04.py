def over_nine_thousand(original_list):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> over_nine_thousand(original_list)
    >>> original_list
    [9001, 9002, 9003, 9004, 9005]
    """
    index = 0
    while index < len(original_list):
        original_list[index] += 9000
        index += 1

# Alternate solution using map
def over_nine_thousand(original_list):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> over_nine_thousand(original_list)
    >>> original_list
    [9001, 9002, 9003, 9004, 9005]
    """
    original_list[:] = map(lambda x: x + 9000, original_list)


def group_by(s: list[int], fn) -> dict[int, list[int]]:
    """Return a dictionary of lists that together contain the elements of s.
    The key for each list is the value that fn returns when called on any of the
    values of that list.

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for x in s:
        key = fn(x)
        if key in grouped:
            grouped[key].append(x)
        else:
            grouped[key] = [x]
    return grouped



def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {
    ...     "bob": "Team A",
    ...     "barnum": "Team B",
    ...     "beatrice": "Team C",
    ...     "bernice": "Team B",
    ...     "ben": "Team D",
    ...     "belle": "Team A",
    ...     "bill": "Team B",
    ...     "bernie": "Team B",
    ...     "baxter": "Team A"
    ... }
    >>> player_dict = common_players(full_roster)
    >>> type(player_dict) == dict
    True
    >>> for key, val in sorted(player_dict.items()):
    ...     print(key, list(sorted(val)))
    Team A ['baxter', 'belle', 'bob']
    Team B ['barnum', 'bernice', 'bernie', 'bill']
    Team C ['beatrice']
    Team D ['ben']
    """
    result_dict = {}
    for player in roster:
        team = roster[player]
        if team in result_dict:
            result_dict[team] += [player]
        else:
            result_dict[team] = [player]
    return result_dict

