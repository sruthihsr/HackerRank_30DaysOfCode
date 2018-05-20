import sys
n =int(input())
new_dict ={}
for i in range(n):
    name,number=input().split(' ')
    new_dict[name]=number

while True:             # Loop continuously
    name = input() #get the inpu
    if name == "":       # If it is a blank line...
        break 
    if(name in new_dict.keys()):
        op=name+'='+new_dict[name]
        print(op.strip())
    else:
        print('Not found')# ...break the loop
