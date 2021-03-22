d={"name":"vidhya", "age":28, "place":"coimbatore", "id": 50}
#print(d)
d["age"]= 30
d["id"]=49
print(d)
studname=d["name"]
print(studname)
place=d.get("place")
print(place)
id=d.get("id")
print(id)