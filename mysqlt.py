#coding=utf-8
import MySQLdb
import time
import led
import cat
le=led.led()
ca=cat.cat()
i=1
while True:
	time.sleep(1)
	dtime=list(time.localtime())
	try:
		conn=MySQLdb.connect(host='10.0.0.3',port=3306,user='iot',passwd='sintianadmin',db='iot',)
		cur=conn.cursor()
		data=cur.execute("select * from dirverlist order by system_id")
		info=cur.fetchmany(data)
		i=i+1
		for ii in info:
			pass
		# print ("lightness is %s" % ii[3])
		if dtime[3]>20 and dtime[3]>6:
			print("this time is: %s min %s sec" % (dtime[4],dtime[5]))
			ca.run(dtime[4],dtime[5])
		# openstr=list(str(dtime[5]))
		# if openstr[0] in ['1','2','3']:
		if dtime[5]>1 and dtime[5]<40:
			right_state=le.light(int(ii[3]))
			left_state=le.left(0)
			print ("left is %s , Lightness is %s " % (left_state,ii[3]))
		else:
			left_state=le.left(int(ii[3]))
			print ("right is %s , Lightness is %s " % (right_state,ii[3]))
			right_state=le.light(0)
		cur.close()
		conn.close()
	except MySQLdb.Error,e: 
		print "database time out!"