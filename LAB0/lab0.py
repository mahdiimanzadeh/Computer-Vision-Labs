def mul(A, B):
    """
    Returns the product of the matrix A by the matrix B.
    Returns the empty list [] if the matrix dimensions
    are not consistent for multiplication.
    """
    LA = len(A)   # تعداد سطرهای A
    LB = len(B)   # تعداد سطرهای B
    CB = len(B[0])  # تعداد ستون‌های B

    if len(A[0]) != LB:  # بررسی ابعاد ماتریس
        return []  # در صورت ناسازگاری ابعاد، مقدار خالی برمی‌گردد.

    # ایجاد ماتریس نتیجه با مقدار اولیه صفر
    final = [[0 for _ in range(CB)] for _ in range(LA)]

    # انجام ضرب ماتریسی
    for i in range(LA):  # پیمایش سطرهای A
        for j in range(CB):  # پیمایش ستون‌های B
            for k in range(LB):  # ضرب سطری A در ستونی B
                final[i][j] += A[i][k] * B[k][j]

    return final  # بازگرداندن ماتریس نهایی


# تعریف ماتریس‌ها
A = [[1, 0, 0],
     [0, 0, 3],
     [0, 2, 0]]

B = [[1, 1],
     [0, 0.5],
     [2, 1.0/3.0]]

C = [[1, 0, 0],
     [0, 0, 0.5],
     [0, 1.0/3.0, 0]]

# اجرای تابع ضرب ماتریس
print("A × B =", mul(A, B))
print("B × A =", mul(B, A))
print("A × C =", mul(A, C))
