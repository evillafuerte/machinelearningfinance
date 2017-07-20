import pandas as pd


def test_run():
    start_date = '2010-01-22'
    start_end = '2010-01-26'
    dates = pd.date_range(start_date, start_end)

    df1 = pd.DataFrame(index=dates)
    print df1


if __name__ == "__main__":
    test_run()
