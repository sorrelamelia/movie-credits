# import requests
from typing import List
import re

"""
look up online movie database to check if its a movie

argument movie, expects a String
return Boolean
"""

non_movie = re.compile('".*"')  # pattern: "xxxx"
character_name = re.compile('\[.*\]', re.DOTALL)
movie_year = re.compile('\(.*\)|\(\?*\)')


# r = requests.get('http://www.omdbapi.com/?t=Sofies+verden')
# print(r.status_code)
# print(r.json())

def remove_empty(string):
    return [item for item in string if item]

def format(list):
    """
    Check if the actor has a first name (the last name is always given)
    Always assign the 3rd slot as movies
    if there is no first name assign it as None
    :param list: List of strings
    :return: List
    """

    # detectng if the name contains a (year)
    first_name = list[1]
    is_movie = movie_year.search(first_name)

    # split array
    # append to the first array
    # join the arrays

    if is_movie:
        split_a = list[0:1]
        split_b = list[2:]
        split_a.append(None)
        return (split_a + split_b) # new list
    else:
        return list # original list


def clean(tv: List):
    """
    The database has `""` for TV shows
    :param tv: list
    :return: new list
    """

    for item in tv:
        # item is a string of the whole row

        # skip "xxxx"
        unwanted = non_movie.search(item)
        if unwanted:  # skip line
            return

        # remove [xxxx]
        newline = character_name.sub("", item)
        string = newline.split('\t')
        newlist = remove_empty(string)

        # the list should at least contain (actor and movie)
        if len(newlist) > 2:
            return format(newlist)
