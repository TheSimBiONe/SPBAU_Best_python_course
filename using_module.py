import my_class as mc


# a = Permutation([4, 3, 1, 2, 6, 7, 5])

transpositions = []
for i in range(1, 11):
    for j in range(1, 11):
        if i != j:
            transpositions.append(mc.Permutation([i, j]))

first = transpositions[1]
for transposition in transpositions[2:]:
    first = transposition * first

print(first)
