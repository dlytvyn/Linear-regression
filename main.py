import pandas as pd

from linear_regression_class import LinearRegression
from args_parser import args_parser


def main(args):
    try:
        file = pd.read_csv('data.csv', delimiter=',')
        print(file)
        linear_regression = LinearRegression(file, args)
        linear_regression.coefs()
        linear_regression.plot()
    except Exception as e:
        exit(e)


if __name__ == "__main__":
    args = args_parser()
    main(args)
