a,b,c=map(int,input("세 복권번호를 입력하시오 :").split())
correct=0
if a==2 or a==3 or a==9 :
    correct +=1
if b==2 or b==3 or b==9 :
   correct +=1
if c==2 or c==3 or c==9 :
    correct +=1
if correct==3:
    print('상금 1억원')
if correct==2:
    print('상금 1천만원')
if correct==1:
    print('상금 1만원')
if correct==0:
    print('다음 기회에')