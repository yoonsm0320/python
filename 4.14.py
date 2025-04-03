n=int(input("정수를 입력하세요:"))
if n==n[::-1]:
    print(f"{n}는 거꾸로 정수입니다.")
else:
    print(f"{n}는 거꾸로 정수가 아닙니다.")