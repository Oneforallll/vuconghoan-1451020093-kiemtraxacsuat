print("Moi ban nhap vao 1 so nguyen duong: ")
while True:
    x = int(input())
    if x<0:
        print("Nhap sai, moi ban nhap lai:")
    else:
        break

giaithua = 1;
for i in range(1,x+1):
    giaithua=giaithua * i;
print("Giai thừa của", x, "là",giaithua)