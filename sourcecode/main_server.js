#nodejs ���� ��ũ��Ʈ
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
		#������� ���� data�� post ������ �ش簪�� �ؽ�Ʈ������ ���丮�� �����ϰ�, MPICH2�� ���� 5���� ��������� ���μ������� ����ó���� �����Ѵ�.
	});
	res.sendfile('hc.html',{root:__dirname});
});

server.listen(1234,function(){
	console.log('running well');
});
#���� ����������� static IP �� 192.168.0.103�� 1234 ��Ʈ�� ���������� ������ �� �ֵ��� ����.