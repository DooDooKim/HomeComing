#nodejs 서버 스크립트
var express = require('express'),
	http = require('http'),
	app = express(),
	server = http.createServer(app);
var bodyParser = require('body-parser');
var fs = require('fs');
var exec = require('child_process').exec;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));

app.get('',function(req,res){
	res.sendfile('hc.html',{root:__dirname});
});

app.post('',function(req,res){
	var data = req.body.data;
	console.log(data)
	fs.writeFile('/home/pi/Desktop/pj/data.txt',data,function(err){
		if(err) throw err;
		exec('mpiexec -f /home/pi/Desktop/pj/machinefile -n 5 python3 /home/pi/Desktop/pj/asdf.py',function(error, stout, stderr){});
		console.log('writed complete')
		#웹페이즈를 통해 data를 post 받으면 해당값을 텍스트파일을 디렉토리에 저장하고, MPICH2를 통해 5대의 라즈베리파이 프로세스위에 병렬처리를 실행한다.
	});
	res.sendfile('hc.html',{root:__dirname});
});

server.listen(1234,function(){
	console.log('running well');
});
#메인 라즈베리파이의 static IP 인 192.168.0.103의 1234 포트로 웹페이지를 접속할 수 있도록 설정.