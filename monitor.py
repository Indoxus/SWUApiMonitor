import requests
import json
import time
import datetime
import arrow
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
		z = "-"
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

class Monitor:
	timestamp = 0
	station_name = ""
	departures = []
	stationid = 1111
	last_update = 0
	stopamount  = 5
	truestopamount = 0
	is_there_data = False
	def __init__(self, stationid,stopamount=5):
		self.stationid = stationid
		self.stopamount = stopamount
		self.update(force=True)
	
	def update(self, force = False):
		if not force:
			if time.time() - self.last_update  < 10:
				return
		try: 
			r = requests.get('https://api.swu.de/mobility/v1/stop/passage/Departures?StopNumber='+str(self.stationid)+'&Limit='+str(self.stopamount))
			self.last_update = time.time()
		except: 
			return
		jsun = r.json()
		try:
			self.station_name = jsun["StopPassage"]["StopCode"]
			data = jsun["StopPassage"]["DepartureData"]
		except:
			return
		formated  = []
		for i in range(n):
			try:
				temp = dict(data[i])
				formated.append([temp["DepartureDirectionText"],temp["DepartureCountdown"]])
			except:
				self.truestopamount = i
				break
			if i == n-1:
				self.truestopamount = i
		self.departures = formated[:]
		self.is_there_data = True

	def print_data(self):
		timepassed = int(time.time()-self.last_update)
		if not self.is_there_data:
			print("Abfahrten")
			print("")
			print("")
			print("no data")
			print("")
			print("")
			return
		print("Abfahrten " + self.station_name)
		print('{:%Y-%m-%d %H:%M:%S}'.format(arrow.get(self.last_update+2*60*60).datetime),"+",int(time.time()-self.last_update))
		if self.truestopamount == 0:
			print("")
			print("no data")
			print("")
			print("")
			return
		for f in self.departures:
			line = format_time(f[1]-timepassed) + " " + f[0]
			print(line[:22])
		for i in range(self.stopamount-self.truestopamount-1):
			print("")

	
mon = Monitor(stop,4)

while True:
	mon.update()
	mon.print_data()
	time.sleep(1)

#	print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))