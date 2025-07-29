import requests
#contents = requests.get("https://api.swu.de/mobility/v1/route/attributes/BaseData?StopNumber=1255&Limit=1")
#print(contents.content)
contents = requests.get("https://api.swu.de/mobility/v1/stop/passage/Departures?StopNumber=1255&Limit=2")
print(contents.content)
#{"StopNumber":1255,"StopCode":"EBST","StopName":"Eselsbergsteige","StopPointNumber":2,"StopPointCode":125502,"PlatformName":"A","StopPointName":"Eselsbergsteige Steig A"},

array = [1,2,3,4,5,6]
array2 = array[:]
print(id(array),id(array2))
print(len("18:22 Wissenschaftsstadt"))