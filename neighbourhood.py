import jellyfish
import sys

file = open(sys.argv[1])

proteins = file.readlines()

for p1 in proteins:
    for p2 in proteins:
        print(p1,p2,jellyfish.jaro_winkler(p1, p2))
