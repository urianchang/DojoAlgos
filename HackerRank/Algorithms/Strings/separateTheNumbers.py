"""
Separate the Numbers:

A numeric string, s, is beautiful if it can be split into a sequence of two
or more positive integers, a[1]...a[n], satisfying the following conditions:
    1. a[i] - a[i-1] = 1 for any 1 < i <= n
    2. No a[i] contains a leading zero.
    3. The contents of the sequence cannot be rearranged.

You must perform 'q' queries, where each query consists of some string s. For
each query, print whether or not the string is beautiful on a new line. If it's
beautiful, print 'YES x', where x is the first number of the increasing sequence
(if there are multiple such values of x, choose the smallest); otherwise,
print 'NO' instead.

Constraints:
    * 1 <= q <= 10
    * 1 <= abs(s) <= 32
    * Each character in s is a decimal digit from 0 to 9 (inclusive)
"""

for _ in xrange(int(raw_input().strip())):
    num = raw_input().strip()
    if len(num) <= 1:
        print "NO"
    else:
        # Select starting number from inputted string
        isBeautiful = False
        for i in xrange(1, (len(num)//2)+1):
            n = cur_n = int(num[:i])
            test_string = num[:i]
            # Create test string with the selected starting number
            while len(test_string) < len(num):
                cur_n += 1
                test_string += str(cur_n)
            if test_string == num:
                isBeautiful = True
                break
        print "YES {}".format(n) if isBeautiful else "NO"

"""
Input:
7
1234
91011
99100
101103
010203
13
1

Output:
YES 1
YES 9
YES 99
NO
NO
NO
NO
"""
