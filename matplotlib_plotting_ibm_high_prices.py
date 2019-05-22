import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    print(df['High'])
    df['High'].plot()
    plt.title("IBM High Prices")
    plt.ylabel("High Prices")
    plt.show()  # deve ser chamada para ver os plots

if __name__ == "__main__":
    test_run()