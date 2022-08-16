import pandas as pd

source_data = pd.read_csv('data/user_friends.dat', sep='\t')
lists = source_data.values.tolist()

usersList = {}
for line in lists:
    if line[0] not in usersList.keys():
        usersList[line[0]] = [line[1]]
    else:
        usersList[line[0]].append(line[1])


def recommend(uid):
    """
    可能认识的人
    :param uid:
    :return:
    """
    if uid not in usersList.keys():
        return False
    res = {}
    # 取出自己的好友，遍历获取
    firend_list = usersList[uid]
    for firend_id in firend_list:
        for firend_reation_id in usersList[firend_id]:
            if firend_reation_id == uid or firend_reation_id in firend_list:
                continue
            if firend_reation_id in res.keys():
                res[firend_reation_id] = res[firend_reation_id] + 1
            else:
                res[firend_reation_id] = 1
    res = sorted(res.items(), key=lambda v: v[1], reverse=True)
    return res[:50]


input_uid = int(input("请输入用户ID:\n"))
print("用户ID:{uid}".format(uid=input_uid))
recommend_list = recommend(input_uid)

if recommend_list is False:
    print("不存在用户")
else:
    print("可能认识的人:")
    for item in recommend_list:
        print("用户ID:{uid},共同好友:{num}".format(uid=item[0], num=item[1]))
