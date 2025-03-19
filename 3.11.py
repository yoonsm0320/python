winnig_numbers= [2,3,9]
a,b,c=map(int,input("세 복권번호를 입력하시오 :").split())
matched_count=(a in winnig_numbers)+(b in winnig_numbers)+(c in winnig_numbers)
if matched_count==3:
    print("상금 1억원")
if matched_count==2:
    print("상금 1천만원")
if matched_count==1:
    print("상금 1만원")
if matched_count==0:
    print("다음 기회에")
