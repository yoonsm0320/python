def resident_registration_number(number):
    year=int(number[:2])
    month=number[2:4]
    day=number[4:6]
    if year>50:
        full_year=year+1900
    else:
        full_year=year+2000
    return f"{full_year}년 {month}월 {day}일"
print(resident_registration_number('511010'))
print(resident_registration_number('491010'))