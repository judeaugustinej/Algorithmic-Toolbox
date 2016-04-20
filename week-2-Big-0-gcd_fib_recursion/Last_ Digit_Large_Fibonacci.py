# Uses python3
num = int(input())

fib_list = [0,1]
a = fib_list[0]
b = fib_list[1]

for i in range(2, num+1):
    a, b = b, a+b
    #fib_list.insert(i, b)

#print(fib_list)
if num == 0:

    print(0)
else:
    #print(str(fib_list[-1])[-1])
    print(str(b)[-1])
    #print(b)


"""
# Uses python3
num = int(input())
a = 0
b = 1

for i in range(2, num+1):
    
    a, b = b, a+b    
b1 = str(b)
print(b1[-1])
"""
