#병렬처리를 통해 작동하고 이미지 분석을 실행할 2,3,4 번 노드의 메인 스크립트
import os
from time import sleep
im_count = 1
while 1:
    if((os.path.isfile("/home/pi/Desktop/pj/image1.jpg")) & (im_count == 1)):
        os.system("python3 /home/pi/Desktop/pj/eval1.py")
        im_count = 2
    if((os.path.isfile("/home/pi/Desktop/pj/image4.jpg")) & (im_count == 2)):
        os.system("python3 /home/pi/Desktop/pj/eval2.py")
        im_count = 3
    if(im_count == 3):
        os.system("scp -r /home/pi/Desktop/pj/eval1.txt 192.168.0.109:/home/pi/Desktop/pj")
        os.system("scp -r /home/pi/Desktop/pj/eval4.txt 192.168.0.109:/home/pi/Desktop/pj")
        sleep(5)
        os.system("sudo rm /home/pi/Desktop/pj/image1.jpg")
        os.system("sudo rm /home/pi/Desktop/pj/image4.jpg")
        os.system("sudo rm /home/pi/Desktop/pj/eval1.txt")
        os.system("sudo rm /home/pi/Desktop/pj/eval4.txt")
        sleep(10)
        break
#반복문을 실행하며, 1번 노드로 부터 scp로 이미지 파일이 해당 디렉토리에 존자할때까지 확인하고, 이미지 파일이 들어오면
#evaluation 스크립트를 실행하여, 이미지 분석을 진행하고 생성되는 label의 텍스트파일을 5번 노드의 주소로 scp한다.