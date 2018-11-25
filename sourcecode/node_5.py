import os
import serial
from time import sleep
ser = serial.Serial("/dev/ttyACM0", 9600)
count = 1
#아두이노와 시리얼통신 설정
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
# 반복문을 실행하며, 아두이노와 시리얼 통신을 진행한다. 데이터 손실을 줄이기 위한, 체크섬 기능으로 1~6까지의 숫자를 보내고,
# 모터제어를 실행한뒤, 보낸 숫자와 같은 숫자를 리턴받고, 0을 아두이노로 다시 보낸다. 그 후 0을 다시 리턴받으면, angle과 done
# 텍스트 파일을 저장하고, 1번 노드로 scp하여 처리를 완료했다는 의미를 가지도록 알고리즘을 설계했다.
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
# 6방향의 제어를 마치고, eval1~6.txt파일을 받으면, 1번 노드의 웹페이지로부터 최초로 입력받은 data값과 분석한 label의 값들을 비교하고, 
# 정답에 해당되는 값을 다시 메인 1번 노드로 보낸다. 그 후 프로세스 과정에서 발생한 모든 데이터값을 지워 초기화한다. 