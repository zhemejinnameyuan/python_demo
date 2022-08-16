import face_recognition
import sqlite3


# 加载图像及获取人脸特征
def load_image(input_image, input_name):
    # 加载本地图像文件到一个numpy ndarray类型的对象上
    image = face_recognition.load_image_file(input_image)

    # 返回图像中每一个面的128维人脸编码
    # 图像中可能存在多张人脸，取下标为0的人脸编码，表示识别出来的最清晰的人脸
    image_face_encoding = face_recognition.face_encodings(image)[0]

    # 将numpy array类型转化为列表
    encoding__array_list = image_face_encoding.tolist()

    # 将列表里的元素转化为字符串
    encoding_str_list = [str(i) for i in encoding__array_list]

    # 拼接列表里的字符串
    encoding_str = ','.join(encoding_str_list)

    # 将人脸特征编码存进数据库
    save_encoding(encoding_str, input_name)


# 人脸特征信息保存
def save_encoding(encoding_str, name):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    insert_sql = "insert into face(name,encoding) values('"+name+"','"+encoding_str+"')"
    try:
        cursor.execute(insert_sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    load_image("img/kobe.jpeg", "科比")
    load_image("img/liudehua.png", "刘德华")
    load_image("img/zhangxueyou.jpeg", "张学友")
