import tempfile
from pathlib import Path

import pandas as pd
import pytest
from pandas.core.frame import DataFrame
from pandas.errors import EmptyDataError

from csv_utils.csv_utils import read_csv, write_csv
from models.sitters import Sitters

INPUT_COLUMNS = ("sitter_email", "rating", "sitter")
OUTPUT_COLUMNS = ["email", "name", "profile_score", "ratings_score", "search_score"]
FIXTURES_PATH = Path("src/tests/fixtures/")


class TestCsvUtils:
    def test_read_valid_csv(self):
        """Check that the pandas dataframe returned is the one we expect"""
        fixture = FIXTURES_PATH / "valid.csv"
        expected_df = pd.DataFrame(
            {
                "rating": [5, 2, 3],
                "sitter": ["Lauren B.", "Sharon H.", "Lauren"],
                "sitter_email": [
                    "user4739@gmail.com",
                    "user7582@yahoo.com",
                    "user4739@gmail.com",
                ],
            }
        )
        df = read_csv(fixture, INPUT_COLUMNS)

        assert isinstance(df, DataFrame)
        assert df.equals(expected_df)

    def test_write_csv(self):
        """Check that the csv generated contains what we expect"""
        stay = ["Lauren B.", "user4739@gmail.com", 5]
        expected_content = (
            "email,name,profile_score,ratings_score,search_score\n"
            "user4739@gmail.com,Lauren B.,1.35,5,1.72\n"
        )

        sitters = Sitters()
        sitters.add_stay(*stay)
        with tempfile.NamedTemporaryFile() as temp:
            write_csv(sitters.sitters, temp.name, OUTPUT_COLUMNS)
            assert open(temp.name).read() == expected_content

    @pytest.mark.parametrize(
        "fixture, exception",
        (
            ("empty.csv", EmptyDataError),
            ("no_header.csv", ValueError),
            ("non_existent.csv", FileNotFoundError),
        ),
    )
    def test_read_csv_exceptions(self, fixture, exception):
        fixture = FIXTURES_PATH / fixture
        with pytest.raises(exception):
            read_csv(fixture, INPUT_COLUMNS)

    @pytest.mark.parametrize(
        "objects, output_filename, exception",
        (
            ("foo", None, ValueError),
            (None, Path("non_existent_folder/test.csv"), FileNotFoundError),
        ),
    )
    def test_write_csv_exceptions(self, objects, output_filename, exception):
        with pytest.raises(exception):
            write_csv(objects, output_filename, OUTPUT_COLUMNS)
