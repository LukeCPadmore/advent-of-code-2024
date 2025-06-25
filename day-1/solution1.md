# Solution to day 1

## Part 1
- Read the input file and split it into lines.
- Use `bisect.isorted` to insert into ordered list
- Saw a solution on reddit that used `map(int, line.strip().split())` to convert each line to an integer more concisely.

## Part2
- Created two `Counter` objects to count the occurrences of each number in the list.
- Used `Counter` to multiply occurrences in first list by occurrences in second list.
