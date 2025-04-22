def solution(mats, park):
    rows=len(park)
    cols=len(park[0])
    mats.sort(reverse=True)
    answer=0
    for answer in mats:
        for i in range(rows-answer+1):
            for j in range(cols-answer+1):
                can_place=True
                for x in range(i,i+answer):
                    for y in range(j,j+answer):
                        if park[x][y]!="-1":
                            can_place=False
                            break
                    if not can_place:
                        break
                if can_place:
                    return answer
    return -1