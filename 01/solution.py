# first star
with open("input.txt", "r") as f:
    pairs = [l.strip().split("   ") for l in f.readlines()]

left = [int(l) for l, r in pairs]
right = [int(r) for l, r in pairs]

distances = [abs(l - r) for l, r in zip(sorted(left), sorted(right))]

total_distance = sum(distances)
print(total_distance)

# second star
lookup = {}
for r in sorted(right):
    if r in lookup:
        lookup[r] += 1
    else:
        lookup[r] = 1

similarities = [l * lookup.get(l, 0) for l in left]
total_similarities = sum(similarities)
print(total_similarities)
