import tempfile

import pandas as pd

from main import OUTPUT_COLUMNS, main


class TestMain:
    FIXTURES_PATH = "src/tests/fixtures/"

    def test_main(self):
        """Execute the main behaviour with a predefined csv and check the resultant csv"""
        with tempfile.NamedTemporaryFile() as temp:
            main(self.FIXTURES_PATH+"reviews.csv", temp.name)
            result_df = pd.read_csv(temp.name, usecols=OUTPUT_COLUMNS)

            # check that the columns are ones we expect
            assert list(result_df.columns.values) == OUTPUT_COLUMNS
            # check that number of sitters is the one we expect
            assert len(result_df.index) == 100
            # make sure that no repeated email/sitters are found
            emails = result_df["email"].tolist()
            assert len(emails) == len(set(emails))
            # check that rows are sorted by descending search_score
            search_scores = result_df["search_score"].tolist()
            assert search_scores == sorted(search_scores, reverse=True)
