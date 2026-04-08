# Union — all elements from both

A = {1, 2, 3}

B = {3, 4, 5}

u = A.union(B)
# print(u)


# Intersection — only shared elements

A = {1, 2, 3}

B = {0, 4, 5}

i = A.intersection(B)
# print(i)

# Differences - just A theke setha bath jabe
# jetha A ar B er modde common

A = {1, 2, 3}

B = {3, 4, 5}

d = A.difference(B)

# print(d)


# Symmetric difference — jetha common jay setha badh jabe baki sob thakbe

A = {1, 2, 3}

B = {3, 4, 5}

s = A.symmetric_difference(B)
print(s)