so_nhan_vien = int(input("Nhập số lượng nhân viên: "))

for i in range(1, so_nhan_vien + 1):

    print(f"\n===== Nhân viên thứ {i} =====")

    ten = input("Nhập tên nhân viên: ")

    ngay_lam = int(input("Nhập số ngày làm việc (0 -> 22): "))

    if ngay_lam < 0 or ngay_lam > 22:
        print("Dữ liệu không hợp lệ")
        continue

    if ngay_lam == 0:
        print(f"{ten} nghỉ toàn bộ tháng")

    print("Biểu đồ ngày làm việc:")

    for j in range(1):
        for k in range(ngay_lam):
            print("*", end="")
        print()

    if ngay_lam >= 18:
        print("Đánh giá: Làm việc chăm chỉ")
    elif ngay_lam < 10:
        print("Đánh giá: Làm việc ít")
    else:
        print("Đánh giá: Làm việc bình thường")