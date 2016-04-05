# Uses python3
import sys

def compute(n):
    c1 = n // 10
    r1 = n % 10
    c2 = r1 // 5
    r2 = r1 % 5
    return c1 + c2,r2

def get_change(n):
    #write your code here
    change = 0
    if 0< n < 5:
        return n
    elif n == 5 or n == 10:
        return 1
    elif 5 < n < 10:
        return 1 + n -5
    if n > 10:
        change, rem = compute(n)
        #print(change, rem)
        while rem > 10:
            change, _ = compute(rem)
            change += change
            #print(change)
        if 0< rem < 5:
            change = change + rem
        elif 5 < rem < 10:
            change = change + 1 + rem -5

        return change

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(get_change(n))
