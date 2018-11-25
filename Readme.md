![homecoming_proto](https://user-images.githubusercontent.com/32383404/48976490-17e9e800-f0cc-11e8-8b5e-9f447f116896.jpg)
---
#ABOUT 'HOMECOMING'
---
HOMECOMING은 6족 보행 인공지능 로봇입니다.

스파이더맨 홈커밍 영화를 보고 영감을 얻어 이름을 Homecoming이라고 지었습니다.
Inception V3를 사용하여 트레이닝 하였고,  11개의 feature를 분류할 수 있습니다.


총 5대의 라즈베리파이를 클러스터링하여 이용하였고, ROBOTIS의 AX-12A 18개를 사용하여 움직입니다.

와이파이를 기반으로 통신하고 모든 프로세서에 고정 IP를 할당하였습니다. 몸체는 3D프린트를 이용하여 직접 제작하였습니다.

동작영상 : 
<https://www.youtube.com/watch?v=UcIJf_XksNU>

세미나영상 : 
<https://www.youtube.com/watch?v=anG-nSqqEN4&t=780s>

- 제목은 MPS430을 이용한 마이크로마우스라고 되어있지만 내용은 홈커밍입니다.


---
#SYSTEM FLOW
![dataflow](https://user-images.githubusercontent.com/32383404/48976514-8333ba00-f0cc-11e8-914d-34705fa81ca6.JPG)

인식모델은 Google 社의 Inception V3를 Fine-tuning하여 사용하였고, 총 11개의 feature를 인식할 수 있도록 트레이닝 하였습니다. 데스크탑을 사용하여 트레이닝 하였고, 라즈베리파이 5대 모두에 tensorflow 1.0을 설치하여 트레이닝 완료된 모델을 올려 사용하였습니다.

총 5대의 라즈베리파이를 MPICH2를 사용하여 Parallel Computing할 수 있도록 하였습니다. NodeJS를 사용하여 간단한 홈페이지를 만들고 찾고 싶은 물체를 텍스트 형태로 입력하고 SEND 버튼을 누름과 동시에 로봇이 동작합니다.

    exec('mpiexec -f /home/pi/Desktop/pj/machinefile -n 5 python3 /home/pi/Desktop/pj/asdf.py',function(error, stout, stderr){});
 1번 노드는 서버를 관리, 영상 촬영을 담당하고 촬영한 사진을 2,3,4 노드에 각각 보내줍니다. 2,3,4 노드는 1번 노드로 부터 받은 영상을 미리 Inception v3를 통해 학습된 모델을 통해 유추를 하고 top-1의 레이블만 뽑아 5번 노드로 전달합니다. 5번 노드는 2,3,4번 노드로 부터 받은 top-1 값과 사용자가 최초에 홈페이지에 입력한 데이터를 비교하여 정답을 1번 노드로 전달하는 역할과 모터 제어를 담당합니다.

모터는 ROBOTIS의 AX-12A 18개를 사용하였고, 모터는 리튬이온 배터리 / 프로세서에는 5개의 리튬폴리머 배터리를 보호회로를 설계하여 장착하였습니다. 충전과 증폭을 위해 Adafruit 社의 PowerBoost를 사용하였습니다.

---


