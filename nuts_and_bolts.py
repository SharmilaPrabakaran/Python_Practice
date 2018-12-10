import os
import sys

def solve(nuts,bolts):
 nbmatch=[]
 b = set(bolts)

 for i in nuts:
    if i in b:
        nbmatch.append(str(i)+" "+str(i))

 return nbmatch


if __name__ == "__main__":
    f = sys.stdout

    nuts_count = int(input())

    nuts = []

    for _ in range(nuts_count):
        nuts_item = int(input())
        nuts.append(nuts_item)

    bolts_count = int(input())

    bolts = []

    for _ in range(bolts_count):
        bolts_item = int(input())
        bolts.append(bolts_item)

    res = solve(nuts, bolts)

    f.write('\n'.join(res))
    f.write('\n')

    f.close()
