
#this concept is Slicing Lists and Strings in python3
t=int(input().strip())
for i in range(0,t):
    s=str(input())
    even,odd=s[::2],s[1::2]
    print(even,odd)
