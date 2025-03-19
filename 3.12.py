x,y=map(int,input("x,y 좌표를 입력하세요:").split())
dist=(x**2+y**2)**0.5
if dist <=5:
    print(x,',',y,"는 원의 내부에 있습니다.")
else:
    print(x,',',y,"는 원의 내부에 없습니다.")
