#����ó���� ���� �۵��ϰ� �̹��� �м��� ������ 2,3,4 �� ����� ���� ��ũ��Ʈ
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
#�ݺ����� �����ϸ�, 1�� ���� ���� scp�� �̹��� ������ �ش� ���丮�� �����Ҷ����� Ȯ���ϰ�, �̹��� ������ ������
#evaluation ��ũ��Ʈ�� �����Ͽ�, �̹��� �м��� �����ϰ� �����Ǵ� label�� �ؽ�Ʈ������ 5�� ����� �ּҷ� scp�Ѵ�.