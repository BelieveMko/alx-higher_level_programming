#!/usr/bin/python3

for mychar in range(97, 123):

    if mychar == 101 or mychar == 113:
        pass

    else:
        print("{:c}" .format(mychar), end="")
