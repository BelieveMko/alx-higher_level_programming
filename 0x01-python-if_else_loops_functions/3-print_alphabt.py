#!/usr/bin/python3

for asciichar in range(97, 123):

    if asciichar == 101 or asciichar == 113:
        pass

    else:
        print("{:c}" .format(asciichar), end="")
