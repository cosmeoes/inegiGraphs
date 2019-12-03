import csv
import matplotlib.pyplot as plt

years = []
deathsChihuahua = []
deathsSonora = []
statesDeaths = {}
with open('datos.csv', encoding="latin-1") as f:

    data = csv.DictReader(f)
    headers = data.fieldnames
    for row in data:
        years.append(row['Year']) 
        for state in headers[1:-1]:
            print(state)
            deaths =row[state].replace(',', '') 
            if deaths == '':
                deaths = '0'
            if not state in statesDeaths:
                statesDeaths[state] = []

            statesDeaths[state].append(int(deaths))

for state in statesDeaths:
    if state == 'Total':
        continue
    plt.plot(years, statesDeaths[state], label=state)

plt.xlabel('Años')
plt.ylabel('Homicidios')
plt.legend()
plt.show()
       
