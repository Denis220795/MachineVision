__author__ = 'Denis'

import numpy


def main():
    f = readfile()
    l = []
    for line in f:
        l.append([int(x) for x in line.split()])
    matrix = numpy.matrix(l)
    print getholes(matrix)


def readfile():
    return open("../resources/image2.txt")


def getholes(matrix):
    eCounter = 0;
    iCounter = 0;
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    for row in range(rows - 1):
        for column in range(columns - 1):
            matrix2 = matrix[row:row + 2, column:column + 2]
            if hasEAngles(matrix2) is True:
                eCounter += 1
            if hasIAngles(matrix2) is True:
                iCounter += 1
    return float(eCounter - iCounter) / 4


def hasEAngles(matrix2x2):
    counter = 0
    for x in numpy.nditer(matrix2x2):
        if x == 1:
            counter += 1
    if counter == 3:
        return True
    else:
        return False


def hasIAngles(matrix2x2):
    counter = 0
    for x in numpy.nditer(matrix2x2):
        if x == 0:
            counter += 1
    if counter == 3:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
