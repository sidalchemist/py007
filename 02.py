import folium
import pandas

data = pandas.read_csv("adat.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
nx = list(data["VOLCANX020"])
numb = list(data["NUMBER"])
name = list(data["NAME"])
loci = list(data["LOCATION"])
st = list(data["STATUS"])
ele = list(data["ELEV"])
typ = list(data["TYPE"])
frm = list(data["TIMEFRAME"])

map = folium.Map(location = [40, -100], zoom_start=6)
feat = folium.FeatureGroup(name="VOLCAN")

def colour_producer(elevation):
    if el>=3000:
        return "darkblue"
    elif 2500<el<=3000:
        return "red"
    elif 1800<el<=2500:
        return "gray"
    elif 1000<=el<=1800:
        return "green"
    else:
        return "beige"

for lt, ln, el, na, lo ,s, ty in zip(lat, lon, ele, name, loci, st, typ):
    feat.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"meter"+"\n"+"\n"+str(lo)+"\n"+str(na)+"\n"+str(s)+"\n"+str(ty), icon=folium.Icon(color=colour_producer(el))))
#feat.add_child(folium.Marker(location=[40.2, -99.1],popup="spot", icon=folium.Icon(color='green')))

feat1 = folium.FeatureGroup(name="Population")

feat1.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function = lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(feat)
map.add_child(feat1)
map.add_child(folium.LayerControl())
map.save("a12.html")
