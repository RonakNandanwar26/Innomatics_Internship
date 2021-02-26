n = int(input())
s = set(map(int, input().split()))

op = int(input())
for i in range(op):
    operation = input().split()

    if operation[0] == 'remove':
        if int(operation[1]) in s:
            s.remove(int(operation[1]))
    elif operation[0] == 'discard':
        s.discard(int(operation[1]))
    elif operation[0] == 'pop':
        s.pop()

add = 0
for i in s:
    add+=i

print(add)