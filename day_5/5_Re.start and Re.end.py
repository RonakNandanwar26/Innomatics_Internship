"""
Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format

The first line contains the string S.
The second line contains the string k.

Constraints
0<len(S)<100
0<len(k)<len(S)

Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa
Sample Output

(0, 1)
(1, 2)
(4, 5)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n, m = input(), input()
matches = re.finditer(r'(?=(' + m + '))', n)

anymatch = False
for match in matches:
    anymatch = True
    print((match.start(1), match.end(1) - 1))

if anymatch == False:
    print((-1, -1))
