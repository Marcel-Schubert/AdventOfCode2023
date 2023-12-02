import requests
import os
from argparse import ArgumentParser
from configparser import ConfigParser

configparser = ConfigParser()
configparser.read("config.ini")

YEAR = configparser.getint("Basic", "Year")
COOKIE = configparser.get("Basic", "Cookie")

argparser = ArgumentParser()
argparser.add_argument(
    "day", type=int, help="download the input file for this day")
args = argparser.parse_args()


def get_url(day: int, year: int = YEAR) -> str:
    return f"https://adventofcode.com/{year}/day/{day}/input"


def download(day: int, year: int = YEAR):
    url = get_url(day, year)
    response = requests.get(url, cookies={"session": COOKIE})
    print(f"Downloading from {url} using cookie {COOKIE}.")
    if response.status_code != 200:
        print("Could not download input file. GET request with status code:",
              response.status_code)
        return
    os.makedirs("input", exist_ok=True)
    with open(f"input/day{day:02d}.txt", "wb") as f:
        f.write(response.content)
        print(f"Downloaded to {f.name}")


if __name__ == "__main__":
    download(args.day)
