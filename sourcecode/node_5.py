import os
import serial
from time import sleep
ser = serial.Serial("/dev/ttyACM0", 9600)
count = 1
#�Ƶ��̳�� �ø������ ����
while(1):
    if(os.path.isfile("/home/pi/Desktop/pj/data.txt")):
        while(1):
            if((count ==1) and (os.path.isfile("/home/pi/Desktop/done1.txt"))):
                ser.write("1".encode())
                ans = ser.read().decode()
                if(ans == '1'):
                    ser.write("0".encode())
                    chec = ser.read().decode()
                    if(chec == '0'):
                        with open("/home/pi/Desktop/pj/angle1.txt","w") as f:
                            f.write(ans)
                        os.system("scp -r /home/pi/Desktop/pj/angle1.txt 192.168.0.103:/home/pi/Desktop/pj")
                    count = count +1
            elif((count ==2) and (os.path.isfile("/home/pi/Desktop/done2.txt"))):
                ser.write("2".encode())
                ans = ser.read().decode()
                if(ans == '2'):
                    ser.write("0".encode())
                    chec = ser.read().decode()
                    if(chec == '0'):
                        with open("/home/pi/Desktop/pj/angle2.txt","w") as f:
                            f.write(ans)
                        os.system("scp -r /home/pi/Desktop/pj/angle2.txt 192.168.0.103:/home/pi/Desktop/pj")
                    count = count +1
            elif((count ==3) and (os.path.isfile("/home/pi/Desktop/done3.txt"))):
                ser.write("3".encode())
                ans = ser.read().decode()
                if(ans == '3'):
                    ser.write("0".encode())
                    chec = ser.read().decode()
                    if(chec == '0'):
                        with open("/home/pi/Desktop/pj/angle3.txt","w") as f:
                            f.write(ans)
                        os.system("scp -r /home/pi/Desktop/pj/angle3.txt 192.168.0.103:/home/pi/Desktop/pj")
                    count = count +1
            elif((count ==4) and (os.path.isfile("/home/pi/Desktop/done4.txt"))):
                ser.write("4".encode())
                ans = ser.read().decode()
                if(ans == '4'):
                    ser.write("0".encode())
                    chec = ser.read().decode()
                    if(chec == '0'):
                        with open("/home/pi/Desktop/pj/angle4.txt","w") as f:
                            f.write(ans)
                        os.system("scp -r /home/pi/Desktop/pj/angle4.txt 192.168.0.103:/home/pi/Desktop/pj")
                    count = count +1
            elif((count ==5) and (os.path.isfile("/home/pi/Desktop/done5.txt"))):
                ser.write("5".encode())
                ans = ser.read().decode()
                if(ans == '5'):
                    ser.write("0".encode())
                    chec = ser.read().decode()
                    if(chec == '0'):
                        with open("/home/pi/Desktop/pj/angle5.txt","w") as f:
                            f.write(ans)
                        os.system("scp -r /home/pi/Desktop/pj/angle5.txt 192.168.0.103:/home/pi/Desktop/pj")
                    count = count +1
            elif((count ==6) and (os.path.isfile("/home/pi/Desktop/done6.txt"))):
                ser.write("6".encode())
                ans = ser.read().decode()
                if(ans == '6'):
                    ser.write("0".encode())
                    chec = ser.read().decode()
                    if(chec == '0'):
                        with open("/home/pi/Desktop/pj/angle6.txt","w") as f:
                            f.write(ans)
                        os.system("scp -r /home/pi/Desktop/pj/angle6.txt 192.168.0.103:/home/pi/Desktop/pj")
                    count = count +1
            elif(count ==7):
                break
# �ݺ����� �����ϸ�, �Ƶ��̳�� �ø��� ����� �����Ѵ�. ������ �ս��� ���̱� ����, üũ�� ������� 1~6������ ���ڸ� ������,
# ������� �����ѵ�, ���� ���ڿ� ���� ���ڸ� ���Ϲް�, 0�� �Ƶ��̳�� �ٽ� ������. �� �� 0�� �ٽ� ���Ϲ�����, angle�� done
# �ؽ�Ʈ ������ �����ϰ�, 1�� ���� scp�Ͽ� ó���� �Ϸ��ߴٴ� �ǹ̸� �������� �˰����� �����ߴ�.
    if(os.path.isfile("/home/pi/Desktop/pj/eval6.txt")):
        for e in range(1,7):
            with open("/home/pi/Desktop/pj/eval%d.txt"%e,'r') as f:
                val = f.read()
            with open("/home/pi/Desktop/pj/data.txt",'r') as f:
                inp = f.read()
            if(val == inp):
                with open("/home/pi/Desktop/pj/ans.txt",'w') as f:
                    f.write(str(e))
            os.system("sudo rm /home/pi/Desktop/pj/eval%d.txt"%e)
            os.system("sudo rm /home/pi/Desktop/pj/angle%d.txt"%e)
            os.system("sudo rm /home/pi/Desktop/done%d.txt"%e)
        os.system("sudo rm /home/pi/Desktop/pj/data.txt")
        os.system("scp -r /home/pi/Desktop/pj/ans.txt 192.168.0.103:/home/pi/Desktop/pj")
        os.system("sudo rm /home/pi/Desktop/pj/ans.txt")
        sleep(5)
        break
# 6������ ��� ��ġ��, eval1~6.txt������ ������, 1�� ����� ���������κ��� ���ʷ� �Է¹��� data���� �м��� label�� ������ ���ϰ�, 
# ���信 �ش�Ǵ� ���� �ٽ� ���� 1�� ���� ������. �� �� ���μ��� �������� �߻��� ��� �����Ͱ��� ���� �ʱ�ȭ�Ѵ�. 