# Uses python3
from fractions import gcd
import sys

a,b = map(int,sys.stdin.readline().split())
#n = int(input())
#m = int(input())
#print(n)
#print(m)
print(gcd(a, b))
