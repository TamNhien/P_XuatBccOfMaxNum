def bang_cuu_chuong(a, b):
    num = max(a, b)
    for i in range(1, 10):
        print(f"{num} x {i} = {num * i}")

num1 = int(input("Nhập số nguyên thứ nhất: "))
num2 = int(input("Nhập số nguyên thứ hai: "))
bang_cuu_chuong(num1, num2)

