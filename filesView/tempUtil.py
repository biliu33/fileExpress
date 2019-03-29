# coding: utf8


def transListToPath(listObj):
    return listObj[0] + ":/" + "/".join(listObj[1:])


if __name__ == '__main__':
    import os
    print os.listdir("D:/")
    print transListToPath(["D", "test", "aa"])