"""
ABC is a right triangle,90 degree at B
Therefore, angle ABC = 90 degree.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle MBC (angle theta, as shown in the figure) in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints
0<AB<=100
0<BC<=100
Lengths AB and BC are natural numbers.

Output Format

Output angle MBC in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.

0<theta<90

Sample Input

10
10

Sample Output
45°
"""

import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)
res=round(math.degrees(math.acos(BC/hype)))
degree=chr(176)
print(res,degree, sep='')