credits = [4.0, 3.0, 2.0, 4.0, 3.0]   # 各门课的学分
points  = [3.5, 4.0, 2.8, 3.2, 3.0]   # 对应的绩点

total = 0.0
for c, p in zip(credits, points):
    total = total + c * p

gpa = total / sum(credits)
print("你的加权 GPA 是：", gpa)