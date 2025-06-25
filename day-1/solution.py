import sys
def solution():
    total1 = total2 = 0 
    for line in sys.stdin: # Read from stdin
        num1, num2 = line.strip().split() # strip input and split
        num1, num2 = int(num1), int(num2)
        total1 += num1
        total2 += num2
    
    return abs(total1 - total2)

if __name__ == "__main__":
    print(solution())