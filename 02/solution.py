# first star
with open("input.txt", "r") as f:
    reports = [[int(level) for level in l.strip().split(" ")] for l in f.readlines()]


def is_safe(report: list[int]) -> bool:
    is_increasing = None
    for i in range(0, len(report) - 1):
        dist = report[i + 1] - report[i]

        if abs(dist) < 1 or abs(dist) > 3:
            return False

        if is_increasing is None:
            if dist > 0:
                is_increasing = True
            elif dist < 0:
                is_increasing = False
        elif (is_increasing and dist < 0) or (not is_increasing and dist > 0):
            return False

    return True


total_safe = sum([is_safe(r) for r in reports])
print(total_safe)


# second star
total_safe_dampened = sum([any([is_safe(r[:i] + r[i+1:]) for i in range(0, len(r))]) for r in reports])
print(total_safe_dampened)
