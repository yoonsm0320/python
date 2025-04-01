num = int(input("숫자를 입력하세요: "))
for i in range(1, num + 1):  
    for j in range(num - i): 
        print(" ", end="")
    for k in range(i): 
        print("*", end="")
    print()  