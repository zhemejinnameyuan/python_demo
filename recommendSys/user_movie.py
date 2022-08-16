
from math import *


content = []
with open('data/data.csv') as fp:
    content = fp.readlines()


data = {}
for line in content[1:-1]:
    line = line.strip().split(',')
    if not line[0] in data.keys():
        data[line[0]] = {line[3]:line[1]}
    else:
        data[line[0]][line[3]] = line[1]


def Euclidean(user1, user2):
    # 取出两位用户评论过的电影和评分
    user1_data = data[user1]
    user2_data = data[user2]
    distance = 0
    # 找到两位用户都评论过的电影，并计算欧式距离
    for key in user1_data.keys():
        if key in user2_data.keys():
            # 注意，distance越大表示两者越相似
            distance += pow(float(user1_data[key]) - float(user2_data[key]), 2)

    return 1 / (1 + sqrt(distance))  # 这里返回值越小，相似度越大


# 计算某个用户与其他用户的相似度
def top10_simliar(userID):
    res = []
    for userid in data.keys():
        # 排除与自己计算相似度
        if not userid == userID:
            simliar = Euclidean(userID, userid)
            res.append((userid, simliar))
    # 按照评分排序
    res.sort(key=lambda x: x[1])
    return res[:10]


def recommend(user):
    # 相似度最高的用户
    top_sim_user = top10_simliar(user)[0][0]
    # 相似度最高的用户的观影记录
    items = data[top_sim_user]
    recommendations = []
    # 筛选出该用户未观看的电影并添加到列表中
    for item in items.keys():
        if item not in data[user].keys():
            recommendations.append((item, items[item]))
    recommendations.sort(key=lambda val: val[1], reverse=True)  # 按照评分排序
    # 返回评分最高的10部电影
    return recommendations[:10]

Recommendations = recommend("1")
print(Recommendations)
