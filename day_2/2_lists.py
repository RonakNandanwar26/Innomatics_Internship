"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example
N=4
append 1 Append 1 to the list,arr=[1].
append 2 Append 2 to the list,arr=[1,2].
insert 3 1 Insert 3 at index 1, arr=[1,3,2]
print  print the array

output:
[1,3,2]

Input Format

The first line contains an integer, , denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line
"""

if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        operation = input().split()
        if operation[0] == 'insert':
            lst.insert(int(operation[1]),int(operation[2]))
        elif operation[0] == 'print':
            print(lst)
        elif operation[0] == 'remove':
            if int(operation[1]) in lst:
                lst.remove(int(operation[1]))
        elif operation[0] == 'append':
            lst.append(int(operation[1]))
        elif operation[0] == 'sort':
            lst = sorted(lst)
        elif operation[0] == 'pop':
            lst.pop()
        elif operation[0] == 'reverse':
            lst.reverse()