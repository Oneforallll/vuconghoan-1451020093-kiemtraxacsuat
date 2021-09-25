print("Moi ban nhap vao 1 so nguyen duong: ")
while True:
    x = int(input())
    if x<0:
        print("Nhap sai, moi ban nhap lai:")
    else:
        break

tongCacChuSo = 0
tg = x
while True:
    du = tg%10
    tg = int(tg/10)
    tongCacChuSo += du
    if tg==0:
        break
print("Tong cac chu so cua so", x, "la:", tongCacChuSo)