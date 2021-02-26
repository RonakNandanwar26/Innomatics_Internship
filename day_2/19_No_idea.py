"""
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i belongs to A, you add 1 to your happiness. If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints
1<=n<=100000
1<=m<=100000
1<=Any integer in the input<=1000000000

Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format
Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT

happiness = 0

a = list(map(int, input().split()))
n = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

for i in n:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)