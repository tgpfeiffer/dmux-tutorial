#!/usr/bin/env python

import sys

# This program is an attempt at solving
#   https://projecteuler.net/problem=1
# for educational purposes.

if not len(sys.argv) == 2:
    sys.stderr.write("usage: %s <n>\n" % sys.argv[0])
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    sys.stderr.write("program argument must be an integer\n")
    sys.exit(1)

result = 0

for i in xrange(n):
    # can you spot the bug in this loop?
    if i % 3 == 0:
        result += i
    if i % 5 == 0:
        result += i

print result

