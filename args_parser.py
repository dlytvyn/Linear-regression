import argparse
from sklearn.linear_model import LinearRegression


def args_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-lr',
                        dest='learning_rate',
                        type=float,
                        default=0.7)
    parser.add_argument('-a',
                        dest='accuracy',
                        type=float,
                        default=0.0000001)
    parser.add_argument('-p',
                        dest='',
                        type=float,
                        default=0.7)
    args = parser.parse_args()
    return args
