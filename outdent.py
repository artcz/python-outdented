import sys

content = sys.stdin.read()
lines = content.splitlines()

counted = []
for l in lines:
    for i, c in enumerate(l):
        if not c.isspace():
            break

    counted.append((i, l))

max_indented = max(counted, key=lambda x: x[0])

for c, l in counted:
    print(' '*(max_indented[0]-c), l.strip(), sep='')
