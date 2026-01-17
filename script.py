N, M, Q, cw, sw, hw, tw = map(int, input().split())
top_1_name = ''
top_2_name = ''
top_3_name = ''
top_1_abs = -1
top_2_abs = -1
top_3_abs = -1
min_rating_abs = Q + 1
sum_rating = 0

if N < 3 or M <= 0 or cw <= 0 or sw <= 0 or hw <= 0 or tw <= 0:
    print("Во введённых данных ошибка")
else:
    for i in range(N):
        curr_name = input()
        curr_rating = 0
        for j in range(M):
            a, b, c, d = map(int, input().split(","))
            curr_rating = curr_rating + a * cw + b * sw + c * hw + d * tw
        sum_rating += curr_rating
        if curr_rating < min_rating_abs:
            min_rating_abs = curr_rating
        if curr_rating > top_1_abs:
            top_3_abs = top_2_abs
            top_3_name = top_2_name
            top_2_abs = top_1_abs
            top_2_name = top_1_name
            top_1_abs = curr_rating
            top_1_name = curr_name
        elif curr_rating > top_2_abs:
            top_3_abs = top_2_abs
            top_3_name = top_2_name
            top_2_abs = curr_rating
            top_2_name = curr_name
        elif curr_rating > top_3_abs:
            top_3_abs = curr_rating
            top_3_name = curr_name
    top_1_round = round(top_1_abs / Q * 100)
    top_2_round = round(top_2_abs / Q * 100)
    top_3_round = round(top_3_abs / Q * 100)
    min_round = round(min_rating_abs / Q * 100)
    average_round = round(sum_rating / Q / N * 100)
    if top_1_abs > Q:
        print("Во введённых данных ошибка")
    else:
        print(f"{top_1_round} {average_round} {min_round}")
        print(f"{top_1_name} {top_1_round}%")
        print(f"{top_2_name} {top_2_round}%")
        print(f"{top_3_name} {top_3_round}%")
        if average_round <= 50:
            print("Курс усваивается плохо")
        else:
            print("Курс усваивается хорошо")
