'''
Symmetric or Not
The program must accept a binary matrix of size RxC as input.
The program must print H if the matrix is horizontally symmetric,
V if the matrix is vertically symmetric or S if the matrix is symmetric
(both horizontally and vertically). Else the program must print -1 as the output.
Boundary Condition(s): 3 <= R, C <= 30
Input Format: The first line contains the value of R and C separated by a space.
The next R lines contain C elements of the binary matrix separated by space(s).
Output Format: The first line contains either 'H' or 'V' or 'S' or '-1'.

Example Input/Output 1:
Input:
3 3
1 0 1
0 1 0
1 0 1
Output: S
Explanation: In the given binary matrix, first row is equal to the last row and
the second row is equal to the second last row(middle row). Similarly,
first column is equal to the third column and the second column is equal to the second last column(middle column).
Hence, S is printed.

Example Input/Output 2:
Input:
4 4
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
Output: -1
Explanation: In the binary matrix, first row is not equal to the
last row and the second row is not equal to the second last row.
Similarly, first column is not equal to the last column and the
second column is not equal to the second last column. Hence, -1 is printed.

Example Input/Output 3:
Input:
4 4
1 0 0 1
0 0 0 0
1 1 1 1
1 1 1 1
Output:V
Explanation: In the given binary matrix, first column is equal to
the last column and the second column is equal to the second last column.
Hence, V is printed.
Example Input/Output 4:
Input:
4 4
1 0 1 0
0 0 1 1
0 0 1 1
1 0 1 0
Output: H
Explanation: In the given binary matrix, first row is equal to the last row and
the second row is equal to the second last row. Hence, H is printed.
'''

#Program

a,b=map(int,input().split())
c=[list(map(int, input().split())) for i in range(a)] 

h, v=0,0 

if(c[::-1]==c):
    h=1 

d=[]

for i in range(a):
    t=[] 
    for j in range(b):
        t.append(c[j][i]) 
    d.append(t)

if(d==d[::-1]):
    v=1 

if v==1 and h==1:
    print('S')
elif v==1:
    print('V') 
elif h==1:
    print('H') 
else:
    print(-1)
    
