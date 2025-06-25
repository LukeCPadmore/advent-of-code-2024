import sys
import bisect
from collections import Counter

def isort():
    l1, l2 = [], []
    for line in sys.stdin: # Read from stdin
        num1, num2 = list(map(int,line.strip().split())) # Strip line and convert to int

        bisect.insort(l1,num1)
        bisect.insort(l2,num2)
    
    return l1,l2

def part1():
    l1,l2 = isort()
    total = sum(abs(item1 - item2) for item1, item2 in zip(l1,l2))

    return total

def part2():
    l1,l2 = isort()
    c1 = Counter(l1)
    c2 = Counter(l2)
    total = sum(key * c1[key] * c2.get(key,0) for key in c1.keys())
    return total


if __name__ == "__main__":
    print(part1())
    print(part2())
    isort()