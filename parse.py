# coding: utf-8
""" function used to parse the maze """
import sys


def parse(string_analyse):
    """ creation of the algorithm to format the structure """
    ret = []
    string_analyse = string_analyse[0:15]
    if len(string_analyse) == 15:
        pass
    else:
        sys.exit(-1)

    for character in string_analyse:
        if character == "x" or character == " " or character == "g" or\
                                                              character == "m":
            ret.append(character)
        else:
            sys.exit(-1)

    return ret


def call_parse():
    """ application of the algorithm to parse"""
    map_maze = []
    with open('maze.txt', "r") as fichier:
        for line in fichier:
            if not line:
                continue
            map_maze.append(parse(line))

    return map_maze

call_parse()
