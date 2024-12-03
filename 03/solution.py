# first star
import re

with open("input.txt", "r") as f:
    chars = f.read()

mul_expr = r"mul\(\d+,\d+\)"
matches = re.findall(mul_expr, chars)

mult_total = 0
for m in matches:
    m1, m2 = m[4:-1].split(",")
    mult_total += int(m1) * int(m2)

print(mult_total)


# second star
cond_expr = r"do\(\)|don\'t\(\)"
matches = re.findall("|".join([mul_expr, cond_expr]), chars)
print(matches)

mult_total = 0
enabled = True
for m in matches:
    if m.startswith("don't"):
        enabled = False
    elif m.startswith("do"):
        enabled = True
    elif enabled:
        m1, m2 = m[4:-1].split(",")
        mult_total += int(m1) * int(m2)

print(mult_total)
