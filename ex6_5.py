import random
# 大样本次数
times = 1000*1000
# 统计生日相同的次数
count = 0
for i in range(times):
    # 创建列表类型，存储23个人的生日在当年的某一天
    lis = []
    for j in range(23):
        lis.append(random.randint(1,365))
    # 利用集合的无重复性，转换为集合类型存储
    items = set(lis)
    if len(items) != len(lis):
        count += 1
print("至少两人生日相同的概率：{:.2f}%".format(count/times*100))
