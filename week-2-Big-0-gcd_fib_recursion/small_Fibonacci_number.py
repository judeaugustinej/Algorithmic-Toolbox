# Uses python3
num = int(input())

fib_list = [0,1]
a = fib_list[0]
b = fib_list[1]

for i in range(2, num+1):
    a, b = b, a+b    
    fib_list.insert(i, b)

#print(fib_list)
if num == 0:
   
    print(fib_list[0])
else:
    print(fib_list[-1])
