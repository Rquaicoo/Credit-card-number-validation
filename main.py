# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
if __name__ == '__main__':
    a = []
    N = int(input())
    for _ in range(N):
        cc_number = str(input())
        a.append(cc_number)
stat = []

status = 'Invalid'
for x in range(len(a)):
    if re.match(r"(4|5|6)\d{3}-\d{4}-\d{4}-\d{4}|(4|5|6)\d{13}", a[x]) and len(a[x].replace('-',''))==16:
        status = 'Valid'
        
    else:
        status = "Invalid"
    a[x]=a[x].replace('-','')
    for b in range(len(a[x])-3):
        y = a[x][b]
        if a[x][b+1] == y and ((a[x][b+2] == y) and (a[x][b+3] == y)):
            status = 'Invalid'
    stat.append(status)
 

for status in stat:
    print(status)
            
     
