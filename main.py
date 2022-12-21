import argparse
from loguru import logger


def main(args):
    logger.info("Hello World")


def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config.json', help='config file path')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main(load_args())
