# coding: utf8
import sys
from functools32 import lru_cache


def transListToPath(listObj):
    return listObj[0] + ":/" + "/".join(listObj[1:])


@lru_cache(maxsize=1)
def getDefaultPath():
    platformName = sys.platform.lower()
    if platformName.startswith("linux"):
        return u"/"
    if platformName.startswith("win"):
        return u"C"


if __name__ == '__main__':
    import os
    #print os.listdir("D:/")
    #print transListToPath(["D", "test", "aa"])
    print "/file/C".split("/")
