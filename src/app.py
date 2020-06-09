print("----------------------------------")
print()
print("STARTING")

print("    IMPORTS")
import sys
import requests
import json
print("done")


#parsing args
#format python /app/app.py <latitude> <longitude>
if len(sys.argv) == 3:
    lat = sys.argv[1]
    lng = sys.argv[2]
else:
    #default lat/lng = LYON
    lat = 45.75
    lng = 4.85

#API key
parameters = {"token": "e9xxxxxxxxxxxxxxxxxxxxxxx"} #get your own key for this API here: https://aqicn.org/data-platform/token/

print("    API REQUEST")
response = requests.get("https://api.waqi.info/feed/geo:"+str(lat)+";"+str(lng)+"/", params=parameters)

print("Status: ", response.status_code)
print()
print("Content trace: ")
print(response.content)
print()


print("    TREATING RESULT")
data = response.json()

city = data["data"]["city"]["name"]
vals = data["data"]["iaqi"]

valstr = ""

for val in vals:
    valstr += str(val) + ": " + str(vals[val]["v"]) + " ; "


print("    WRITING OUTPUT FILE")
# produce a result file in /scone
with open("/scone/my-result.txt", "w+") as result_file:
    s = "Polution information for the position "+city
    s += "\n pollutants: " + valstr
    result_file.write(s)


print("ALL DONE")
print()
print("----------------------------------")