'''
String Expansion 
The program must accept a string S as the input. 
The program must print the expanded string as shown in Example Input/Output section. 
Boundary Condition(s): 1 <= Length of S <= 100 

Input Format: The first line contains the string S. 
Output Format: The first line contains the expanded string shown in Example Input/Output section. 

Example Input/Output 1: 
Input: LEMON 
Output: LLELEMLEMOLEMON 

Explanation: LEMON is expanded as L LE LEM LEMO LEMON. 
Hence the output is LLELEMLEMOLEMON 

Example Input/Output 2: 
Input: gamer 
Output: ggagamgamegamer

'''

# program

a=input().strip()
b=len(a)+1
out=""
for i in range(1):
    for j in range(1,b):
        out+=a[i:j]
print(out)
