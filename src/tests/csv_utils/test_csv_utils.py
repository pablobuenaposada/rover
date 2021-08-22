import tempfile
from pathlib import Path

import pandas as pd
from pandas.core.frame import DataFrame

from csv_utils.csv_utils import read_csv, write_csv
from models.sitters import Sitters


class TestCsvUtils:
    FIXTURES_PATH = Path("src/tests/fixtures/")

    def test_read_csv(self):
        """Check that the pandas dataframe returned is the one we expect"""
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
        df = read_csv(
            self.FIXTURES_PATH / "test_valid.csv", ("sitter_email", "rating", "sitter")
        )  # PABLO

        assert isinstance(df, DataFrame)
        assert df.equals(expected_df)

    def test_write_csv(self):
        """check that the csv generated contains what we expect"""
        stay = ["Lauren B.", "user4739@gmail.com", 5]
        expected_content = "email,name,profile_score,ratings_score,search_score\nuser4739@gmail.com,Lauren B.,1.35,5,1.72\n"

        sitters = Sitters()
        sitters.add_stay(*stay)
        with tempfile.NamedTemporaryFile() as temp:
            write_csv(
                sitters,
                temp.name,
                ["email", "name", "profile_score", "ratings_score", "search_score"],
            )
            assert open(temp.name).read() == expected_content
