import os
from picamera import PiCamera
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
c_count = 0
i = 1
x = 0
#picamera ����
camera = PiCamera()
camera.resolution =(640,480)
camera.framerate = 10
#ī�޶��� ��ġ����
camera.hflip = True
camera.vflip = True

sense.show_message("WAIT")

sleep(5)

while 1:
    if((os.path.isfile("/home/pi/Desktop/pj/angle%d.txt"%x)) and (c_count == x)):
        if(i==7):
            break
        camera.start_preview()
        camera.annotate_text='3'
        sense.show_letter("3")
        sleep(1)
        camera.annotate_text='2'
        sense.show_letter("2")
        sleep(1)
        camera.annotate_text='1'
        sense.show_letter("1")
        sleep(1)
        sense.clear()
        camera.annotate_text=''
        camera.capture('/home/pi/Desktop/pj/image%d.jpg'%i)
        with open("/home/pi/Desktop/done%d.txt"%i,"w") as f:
            f.write("nothing")
        if(i ==1 or i == 4):
            os.system("scp -r /home/pi/Desktop/pj/image%d.jpg 192.168.0.108:/home/pi/Desktop/pj"%i)            
        elif i ==2 or  i ==5:
            os.system("scp -r /home/pi/Desktop/pj/image%d.jpg 192.168.0.106:/home/pi/Desktop/pj"%i)
        elif i ==3 or  i ==6:
            os.system("scp -r /home/pi/Desktop/pj/image%d.jpg 192.168.0.107:/home/pi/Desktop/pj"%i)
        if(i==1):
            os.system("scp -r /home/pi/Desktop/pj/data.txt 192.168.0.109:/home/pi/Desktop/pj")
        os.system("scp -r /home/pi/Desktop/done%d.txt 192.168.0.109:/home/pi/Desktop"%i)
        i = i+1
        x = x+1
        c_count = c_count+1
        camera.stop_preview()
    	#�ݺ����� �����ϸ鼭, �ش� ���丮�� ������ �ִ��� üũ�ϰ�, ������ ip�� ������ scp�Ѵ�.    
    if(c_count == 6):
        sense.show_message("WAIT")
        sleep(1)
        while 1:
            if(os.path.isfile("/home/pi/Desktop/pj/ans.txt")):
                os.system("python3 /home/pi/Desktop/pj/bri.py")
                break
        sleep(30)
        break
	#6���� ������ ��� ������, bridge�� ���� ���� ��ũ��Ʈ�� �����ϰ�, opencv ��ũ��Ʈ�� �����Ѵ�.
