import matplotlib.pyplot as plt

region_dict = {
    "Akmola": {"Area": 146219, "Population": 737495},
    "Aktobe": {"Area": 300629, "Population": 757768},
    "Almaty": {"Area": 319, "Population": 1365632},
    "Almaty Region": {"Area": 223924, "Population": 1807894},
    "Astana": {"Area": 710, "Population": 613006},
    "Atyrau": {"Area": 118631, "Population": 510377},
    "Baikonur": {"Area": 57, "Population": 36175},
    "East Kazakhstan": {"Area": 283226, "Population": 1396593},
    "Jambyl": {"Area": 144264, "Population": 1022129},
    "Karaganda": {"Area": 427982, "Population": 1341700},
    "Kostanay": {"Area": 196001, "Population": 885570},
    "Kyzylorda": {"Area": 226019, "Population": 678794},
    "Mangystau": {"Area": 165642, "Population": 485392},
    "North Kazakhstan": {"Area": 97993, "Population": 596535},
    "Pavlodar": {"Area": 124800, "Population": 742475},
    "Shymkent": {"Area": 1170, "Population": 603499},
    "Turkistan": {"Area": 117249, "Population": 2469357},
    "West Kazakhstan": {"Area": 151339, "Population": 598880}
}

regions = list(region_dict.keys())
areas = list(area["Area"] for area in region_dict.values())
populations = list(population["Population"] for population in region_dict.values())

plot1, axis1 = plt.subplots(figsize=(8, 6))
axis1.plot(regions, areas, label="region area")
axis1.set_title("area by region")
axis1.set_ylabel("area")
plt.xticks(rotation=90)
plt.show()


plot2, axis2 = plt.subplots(figsize=(8, 6))
explode = [0.1] * len(regions)
axis2.pie(populations, labels=regions, explode=explode, autopct='%1.1f%%', startangle=90)
axis2.axis('equal')
plt.show()
