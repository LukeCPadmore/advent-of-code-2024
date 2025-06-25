import sys

def load_reports():
    # Read in file line by line and convert to int
    reports = [list(map(int,line.strip().split())) for line in sys.stdin]
    return reports

def is_safe(levels):
    # Get differences
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    # Check differences monotonic
    same_sign = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    # Check differences between 1 and 3
    valid_magnitude = all(1 <= abs(d) <= 3 for d in diffs)
    return same_sign and valid_magnitude

def part1(reports):
    return sum(is_safe(report) for report in reports)

def is_safe_loo(levels):
    # Run is_safe while leaving and index out each time
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True
    return False


def part2(reports):
    return sum(is_safe_loo(report) for report in reports)

if __name__ == '__main__':
    reports = load_reports()
    print(part1(reports))
    print(part2(reports))