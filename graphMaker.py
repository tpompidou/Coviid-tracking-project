import matplotlib.pyplot as plt
import numpy as np
import dailyStateOrganizer
import stockPriceGetter
import csv


def getData(state):
    date = []
    positive = []
    recovered = []
    death = []
    with open('coronaData\historicalData' + state + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for row in csv_reader:
            try:
                if lineCount >= 0:
                    date.append(row[0])
                    positive.append(row[1])
                    recovered.append(row[2])
                    death.append(row[3])
                lineCount += 1
            except(IndexError):
                break
    return date, positive, recovered, death


def plot(date, data, a):
    plt.plot(date, data, a)
    plt.show()

def interface:
    print()


def main():
    date, positive, recovered, death = getData('USA')
    plot(date, positive, recovered)

main()
