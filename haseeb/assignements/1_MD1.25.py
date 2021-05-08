from hashlib import md5
import string
from random import shuffle, choice, randint
import itertools
# list(itertools.permutations([1, 2, 3]))


def md125(s):  # this is the hash function you'll use
    return md5(s.encode()).hexdigest()[:8]


def generate_md125_collisions():
    seen = {}
    i = 0
    while True:
        check = f"nakamoto{i}"
        md = md125(check)

        if md in seen:
            return (check,seen[md])
        
        seen[md] = check
        i += 1 
        


print(generate_md125_collisions())


#iterate threough pairs
