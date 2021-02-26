"""
Given the names and grades for each student in a class of  students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
 order their names alphabetically and print each name on a new line.

Example
records = [['chi',20.0],['beta',50],['alpha',50]]

The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0.
 There are two students with that score: ['beta','alpha']. Ordered alphabetically,
  the names are printed as:

alpha
beta

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints
2<=N<=5
There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in.
If there are multiple students, order their names alphabetically and
print each one on a new line.
"""

if __name__ == '__main__':
    lst = []
    d = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())

        lst.append([name, score])
        d[name] = score

    grade = []
    for i in lst:
        grade.append(i[1])

    grade = sorted(list(set(grade)))
    second_lowest = grade[1]
    names = []
    for k,v in d.items():
        if v == second_lowest:
            names.append(k)
    names.sort()
    for i in names:
        print(i)