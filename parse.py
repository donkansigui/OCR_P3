s1 = "xxxxxxxxxxxxxxx"
s2 = "xg   x        x"
s3 = "xxxx xx xxxx  x"
s4 = "x  x    xx   xx"
s5 = "xx  xxxx  xx  x"
s6 = "xxx    x x  x x"
s7 = "x   x         x"
s8 = "x xxxxxxx  xxxx"
s9 = "x    x        x"
s10 = "xxx xx xx xx  x"
s11 = "xx  x  x   x xx"
s12 = "x        x    x"
s13 = "x xxx x xx xxxx"
s14 = "x     x  x   mx"
s15 = "xxxxxxxxxxxxxxx"

def parse(s):
    """ creation of the algorithm to format the structure """
    ret = []

    s = s[0:15]
    if len(s) == 15 :
        pass

    else:
        print("len error")
        sys.exit(-1)

    for character in s:

        if character == "x" or character ==" " or character == "g" or character == "m":
            ret.append(character)
        else:
            print("character error")
            sys.exit(-1)

    return ret
# fonction parsing
def call_parse():
    """ application of the algorithm """

    map = []
    map.append(parse(s1))
    map.append(parse(s2))
    map.append(parse(s3))
    map.append(parse(s4))
    map.append(parse(s5))
    map.append(parse(s6))
    map.append(parse(s7))
    map.append(parse(s8))
    map.append(parse(s9))
    map.append(parse(s10))
    map.append(parse(s11))
    map.append(parse(s12))
    map.append(parse(s13))
    map.append(parse(s14))
    map.append(parse(s15))
    return map
