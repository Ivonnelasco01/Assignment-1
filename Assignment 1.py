str1="IVONNE"

print_I=[[" "for i in range(6)]for j in range(7)]
print_V=[[" "for i in range(6)]for j in range(7)]
print_O=[[" "for i in range(6)]for j in range(7)]
print_N=[[" "for i in range(6)]for j in range(7)]
print_N=[[" "for i in range(6)]for j in range(7)]
print_E=[[" "for i in range(6)]for j in range(7)]
i=0
j=6

#code for I
for row in range(7):
    for col in range(6):
        if col==2 or ((row==0 or row==6)and col!=5):
            print_I[row][col]="*"

#code for V
for row in range(7):
    for col in range(6):
        if ((col==0 or col==4)and row<5) or (row-col==4 and row>4) or (row+col==8 and row>4):
            print_V[row][col]="*"

#code for O
for row in range(7):
    for col in range(6):
        if ((col==0 or col==5)and(row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<5)):
            print_O[row][col]="*"

#code for N
for row in range(7):
    for col in range(6):
        if (col==0 or col==5) or row==col:
            print_N[row][col]="*"

#code for N
for row in range(7):
    for col in range(6):
        if (col==0 or col==5) or row==col:
            print_N[row][col]="*"

#code for E
for row in range(7):
    for col in range(6):
        if col==0 or row==3 or row==0 or row==6:
            print_E[row][col]="*"

for i in range(7):
    for j in range(6):
        print(print_I[i][j],end=" ") 
    print(end="  ")       
    for j in range(6):
        print(print_V[i][j],end=" ") 
    print(end="  ")
    for j in range(6):
        print(print_O[i][j],end=" ") 
    print(end="  ")   
    for j in range(6):
        print(print_N[i][j],end=" ") 
    for j in range(6):
        print(print_N[i][j],end=" ") 
    print(end="  ")   
    for j in range(6):
        print(print_E[i][j],end=" ") 
    print(end="  ")       
    print()