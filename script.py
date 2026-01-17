N, M, Q, cw, sw, hw, tw = map(int, input().split())
name = input()
if M <= 0 or cw <= 0 or sw <= 0 or hw <= 0 or tw <= 0:
    print("Во введённых данных ошибка")
else:
    rating = 0
    for i in range(M):
        a, b, c, d = map(int, input().split(','))
        rating = rating + a * cw + b * sw + c * hw + d *g tw
    if rating > Q:
        print("Во введённых данных ошибка")
    else:
        print(f"{name} {round(rating / Q * 100)}%")