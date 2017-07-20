import pandas as pd


def test_run():
    start_date = '2017-04-22'
    start_end = '2017-04-26'
    dates = pd.date_range(start_date, start_end)

    df1 = pd.DataFrame(index=dates)

    #read SPY in a temporary dataframe
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True)

    #Join the two dataframes using Dataframe.join()
    df1 = df1.join(dfSPY)
    print df1

if __name__ == "__main__":
    test_run()
