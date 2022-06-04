import pandas as pd


def manipulate_data():
    # Create dataframe object
    melb_data = pd.read_csv("melb_data.csv")

    # Print out information about the dataframe object
    print(melb_data.describe())


if __name__ == "__main__":
    manipulate_data()
