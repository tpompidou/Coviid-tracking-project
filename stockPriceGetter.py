import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use('ggplot')
STOCKS = ['SNAP', 'EPOR', 'ATVI', 'NTDOY', 'FB', 'AAPL', 'DIS', 'NFLX']


def getStockData(name):  ## gets data
    start = dt.datetime(2020, 1, 15)
    end = dt.datetime.now()
    df = web.DataReader(name, 'yahoo', start, end)
    return df


def makeCSV(name, df):  ## data into csv
    df.to_csv(name + '.csv')


def readCSV():  ## read csv
    df = pd.read_csv(name + '.csv', parse_dates=True, index_col=0)
    return df


def graphCSV(df):  ##makes the graph
    df.plot()  ##specify what you want to display with ['']
    plt.show()


def main():
    for i in STOCKS:
        df = getStockData(i)
        makeCSV(i,df)

main()

