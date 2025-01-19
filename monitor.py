import requests
import json
import time
import datetime
import sys

n = 5

if len(sys.argv)>1:
	stop = sys.argv[1]
else:
    stop = 1111

def invert_first_colum(array):
	out = []
	n = len(array)
	for i in range(n):
		out.append([array[n-1-i][0],array[i][1]])
	return out

def format_time(time):
	out = ""
	if time <0:
		time *= -1
		z+"-"
	else:
		z= " "
	minutes = time//60
	seconds = time%60
	if minutes < 10:
		out += z +str(minutes)
	else:
		out += str(minutes)
	out+=":"
	if seconds < 10:
		out += "0" +str(seconds)
	else:
		out += str(seconds)
	return out


while True:
	time.sleep(1)
	r = requests.get('https://api.swu.de/mobility/v1/stop/passage/Departures?StopNumber='+str(stop)+'&Limit='+str(n))
	jsun = r.json()
	blank=0
	#print(r.text)
	try:
		data = jsun["StopPassage"]["DepartureData"]
		#print(data)
	except:
		print("Abfahrten")
		print("")
		print("")
		print("no data")
		print("")
		print("")
		continue
	formated = []
	for i in range(n):
		try:
			temp = dict(data[i])
			#print(temp)
			formated.append([temp["DepartureDirectionText"],temp["DepartureCountdown"]])
		except:
			blank = n-1-i
			break
	
	print("Abfahrten")
	print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
	if blank == n-1:
		print("")
		print("no data")
		print("")
		print("")

	for f in formated:
		print(format_time(f[1]),f[0])
	for b in range(blank):
		print("")
