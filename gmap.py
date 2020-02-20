import googlemaps
from datetime import datetime
api_key='AIzaSyDEox3rQZmLwbppyK0zamYZ_l7Pa3FGl0U'
gmaps=googlemaps.Client(key=api_key)

origin="25.016716, 121.540441"
destination="25.014616, 121.534636"
now=datetime.now()
directions_result=gmaps.directions(origin,destination,mode="bicycling",avoid="ferries",departure_time=now)
instruction=[]
node=[]


for i in range(len(directions_result[0]['legs'][0]['steps'])):
    raw_data=directions_result[0]['legs'][0]['steps'][i]['html_instructions']
    if "Turn" in raw_data:
        index_1=raw_data.find("<b>")
        index_2=raw_data.find("</b>")
        index_3=raw_data.find("<b>",index_2)
        index_4=raw_data.find("</b>",index_3)
        instruction.append((raw_data[index_1+3:index_2],raw_data[index_3+3:index_4]))
    elif "Continue" in raw_data:
        index_1=raw_data.find("<b>")
        index_2=raw_data.find("</b>")
        instruction.append(("straight",raw_data[index_1+3:index_2]))
    # print(directions_result[0]['legs'][0]['steps'][i]['html_instructions'])
    if i==0:
        node.append((directions_result[0]['legs'][0]['steps'][i]['start_location']['lat'],directions_result[0]['legs'][0]['steps'][i]['start_location']['lng']))
        node.append((directions_result[0]['legs'][0]['steps'][i]['end_location']['lat'],directions_result[0]['legs'][0]['steps'][i]['end_location']['lng']))
    else:
        node.append((directions_result[0]['legs'][0]['steps'][i]['end_location']['lat'],directions_result[0]['legs'][0]['steps'][i]['end_location']['lng']))
    # print(directions_result[0]['legs'][0]['steps'][i]['start_location'])
    # print(directions_result[0]['legs'][0]['steps'][i]['end_location'])
for i in range(len(instruction)):
    print(instruction[i])
for i in range(len(node)):
    print(node[i])