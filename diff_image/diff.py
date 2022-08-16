import face_recognition
import cv2
import sqlite3
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# 人脸特征编码集合
known_face_encodings = []
# 人脸特征姓名集合
known_face_names = []


# 从数据库获取保存的人脸特征信息
def get_info():
    # 建立数据库链接对象
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    sql = "select * from face"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        # 返回的结果集为元组
        for row in results:
            name = row[0]
            encoding = row[1]
            dlist = encoding.strip(' ').split(',')
            # 将list中str转换为float
            dfloat = list(map(float, dlist))
            arr = np.array(dfloat)

            # 将从数据库获取出来的信息追加到集合中
            known_face_encodings.append(arr)
            known_face_names.append(name)

    except Exception as e:
        print(e)

        conn.close()


# 加载视频图像
def load_image():
    # 获得特征信息
    get_info()
    #用于画图
    cv2image = cv2.imread('img/kobe.jpeg')

    images = face_recognition.load_image_file("img/kobe.jpeg")
    face_locations = face_recognition.face_locations(images)
    # 返回128维人脸编码，即人脸特征
    face_encodings = face_recognition.face_encodings(images, face_locations)

    face_names = []

    # 将获得的人脸特征与数据库中的人脸特征集合进行比较，相同返回True，不一样返回False
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.1)

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            # print(name+'已存在')
            face_names.append(name)

            # 将捕捉到的人脸显示出来
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # 画框
                color_number = (255, 255, 255)
                fontpath = "/System/Library/Fonts/STHeiti Light.ttc"  #字体路径
                font = ImageFont.truetype(fontpath, 16)
                img_pil = Image.fromarray(cv2image)
                draw = ImageDraw.Draw(img_pil)
                draw.text((left, right), name, font=font, fill=color_number)
                image = np.array(img_pil)

                cv2.rectangle(image, (left, bottom), (right, top), color_number, 2)
                # cv2.imshow('image',image)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                cv2.imwrite('diff_face.jpg', image)



if __name__ == '__main__':
    load_image()
