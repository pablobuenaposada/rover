import argparse

from csv_utils.csv_utils import read_csv, write_csv
from models.sitters import Sitters

DEFAULT_INPUT_FILENAME = "reviews.csv"
INPUT_COLUMNS = ("sitter_email", "rating", "sitter")
DEFAULT_OUTPUT_FILENAME = "sitters.csv"
OUTPUT_COLUMNS = ["email", "name", "profile_score", "ratings_score", "search_score"]


def main(input, output):
    df = read_csv(input, INPUT_COLUMNS)

    sitters = Sitters()
    for row in df.itertuples():
        sitters.add_stay(row.sitter, row.sitter_email, row.rating)

    write_csv(sitters, output, OUTPUT_COLUMNS)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=DEFAULT_INPUT_FILENAME)
    parser.add_argument("--output", default=DEFAULT_OUTPUT_FILENAME)
    args = parser.parse_args()
    main(args.input, args.output)
