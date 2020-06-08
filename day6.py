# Enter your code here. Read input from STDIN. Print output to STDOUT


t = int(input())
s = ""
s_odd = ""
s_even = ""
s2 = ""
matrix = []

for i in range(t):
    s_odd = ""
    s_even = ""
    s = input()
    for j in range(0,len(s),2):
        s_even += s[j] 
    for k in range(1,len(s),2):
        s_odd += s[k]
    s2 = s_even + " " + s_odd
    matrix.append(s2)

for i in range(t):
    print(matrix[i])
