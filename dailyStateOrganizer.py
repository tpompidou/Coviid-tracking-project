import csv, json, gspread

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# from google.oauth2.service_account import Credentials
#
# scope = ['https://docs.google.com/spreadsheets/d/1im8fKf4Tc73BiQ1-EAZy8n6OE9DMwM9cPM58nrXB2c0/edit#gid=0',
#          'https://www.googleapis.com/auth/drive']
#
# credentials = Credentials.from_service_account_file(
#     'file://C:/Users/tpomp/Downloads/ace-crossbar-275019-c10bb3acd7fb.json', scopes=scope)
#
# gc = gspread.authorize(credentials)

def getState(data, state):  # done
    jsonFilter = [x for x in data if x['state'] == state]
    return jsonFilter

def getUS():
    with open('historicalDataUS.JSON') as f:
        data = json.load(f)
    return data
def getJSON():  # done
    with open('historicalData.JSON') as f:
        data = json.load(f)
    return data


def extractData(data):  # done
    inner = data
    date = []
    state = []
    positive = []
    recovered = []
    death = []
    for p in inner:
        a = str(p['date'])
        d = a[4:6] + "/" + a[6:] + "/" + a[:4]
        date.append(d)
        state.append(p['state'])
        positive.append(p['positive'])
        try:
            recovered.append(p['recovered'])
            death.append(p['death'])
        except KeyError:
            death.append(0)
            recovered.append(0)
    return date, state, positive, death, recovered

def extractDataUS(data):  # done
    inner = data
    date = []
    positive = []
    recovered = []
    death = []
    for p in inner:
        a = str(p['date'])
        d = a[4:6] + "/" + a[6:] + "/" + a[:4]
        date.append(d)
        positive.append(p['positive'])
        try:
            recovered.append(p['recovered'])
            death.append(p['death'])
        except KeyError:
            death.append(0)
            recovered.append(0)
    return date, positive, death, recovered

def dataParse(date, state, positive, death, recovered):
    csvData = [[]]
    for i in range(len(date)):
        csvData[i].append(state[i])
        csvData[i].append(date[i])
        csvData[i].append(positive[i])
        csvData[i].append(death[i])
        csvData[i].append(recovered[i])
        csvData.append([])
    return csvData

def dataParseUS(date, positive, death, recovered):
    csvData = [[]]
    for i in range(len(date)):
        csvData[i].append(date[i])
        csvData[i].append(positive[i])
        csvData[i].append(death[i])
        csvData[i].append(recovered[i])
        csvData.append([])
    return csvData

def storeCSV(csvData, state):
    name = "coronaData\historicalData" + state + '.csv'
    with open(name, 'w', newline='')as csvfile:
        write = csv.writer(csvfile)
        write.writerow(['State', 'Date', 'Positive', 'Death', 'recovered'])
        for p in csvData:
            write.writerow(p)
    return name

def storeCSVUSA(csvData):
    name = "coronaData\historicalDataUSA.csv"
    with open(name, 'w', newline='')as csvfile:
        write = csv.writer(csvfile)
        write.writerow(['Date', 'Positive', 'Death', 'recovered'])
        for p in csvData:
            write.writerow(p)
    return name

# def pushToSheets:
#     return ''


def main():
    JSON = getJSON()
    for i in range(len(STATES)):
        data = getState(JSON, STATES[i])
        date, state, positive, death, recovered = extractData(data)
        data = dataParse(date, state, positive, death, recovered)
        storeCSV(data, STATES[i])
    data=getUS()
    date, positive, death, recovered = extractDataUS(data)
    data = dataParseUS(date, positive, death, recovered)
    storeCSVUSA(data)


main()
