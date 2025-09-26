#Read an integer n, from user. 
# Without using any string method print the following : 123...n.  
# "....." represents the consecutive values in between.

n = int(input())
for i in range(1,n+1):
    print(i,end='')
