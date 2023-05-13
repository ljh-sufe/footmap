
if __name__ == '__main__':
    with open("citiesBeenTo.txt") as f:
        a = f.readlines()
    a = [x.replace("\n", "").split("|") for x in a]

    import folium
    from geopy.geocoders import Nominatim

    geolocator = Nominatim(user_agent="mygeo")

    detail_list = []
    city_list = a
    strlist = []
    m = folium.Map()

    for city in city_list:
        detail = str(city[1])
        if city[2] != "":
            latitude = float(city[2])
            longitude = float(city[3])
            folium.Marker([latitude, longitude], popup="<i>" + detail + "</i>").add_to(m)
            str_ = city[0] + "|" + detail + "|" + str(latitude) + "|" + str(longitude) + "\n"
        else:
            try:
                location = geolocator.geocode(city[0])
                latitude = location.latitude
                longitude = location.longitude
                folium.Marker([latitude, longitude], popup="<i>" + detail + "</i>").add_to(m)
                str_ = city[0] + "|" + detail + "|" + str(latitude) + "|" + str(longitude) + "\n"
            except:
                print(city)
                str_ = city[0] + "|" + detail + "|" + "|" + "\n"
        strlist.append(str_)

    m.save("ljh.html")
    with open("citiesBeenTo.txt", "w") as f:
        for s in strlist:
            f.write(s)