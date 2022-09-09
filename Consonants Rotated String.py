'''

Consonants Rotated String 
The program must accept the value of a string S and an integer N as input. 
The program must rotate the consonants (anti-clockwise direction) in the string by N times. 
Finally, the program must print the rotated string as the output. 
Boundary Condition(s): 
2 <= Length of String S <= 1000 
1 <= N <= 50 
Input Format: The first line contains the value S and value of N separated by a space. 
Output Format: The first line contains the rotated string. 

Example Input/Output 1: 
Input: aabaajaaks 2 
Output: aakaasaabj 

Example Input/Output 2: 
Input: helloworld 5 
Output: ledhololwr


'''

# program

a,n=map(str, input().split()) 
n=int(n) 
b="aeiou" 
c=[i for i in a if i not in b] 
while(n):
    t=c[0] 
    c=c[1:] 
    c.append(t)
    n-=1 
k=0
for i in a: 
    if i not in b:
        print(c[k], end='')
        k+=1 
    else:
        print(i,end='')
