import string

import pytest

from models.sitter import (
    Sitter,
    _calculate_profile_score,
    _calculate_ratings_score,
    _calculate_search_score,
    _count_distinct_letter_occurrences,
)


class TestModel:
    def test_init(self):
        sitter = Sitter("Pablo", "pablo@gmail.com")
        assert sitter.name == "Pablo"
        assert sitter.email == "pablo@gmail.com"
        assert sitter.profile_score == 0.96
        assert sitter.ratings == []
        assert sitter.ratings_score == 0
        assert sitter.search_score == 0.96

    @pytest.mark.parametrize(
        "ratings, expected_search_score",
        (
            ([], 0.38),
            ([0], 0.34),
            ([5], 0.84),
            ([5, 5], 1.3),
        ),
    )
    def test_add_stay(self, ratings, expected_search_score):
        sitter = Sitter("foo", "bar")
        for rating in ratings:
            sitter.add_stay(rating)
        assert sitter.search_score == expected_search_score

    @pytest.mark.parametrize(
        "name, expected_occurrences",
        (
            ("", 0),
            ("Leilani R", 6),
            ("Leilani R.", 6),
            ("Leilani Rñ", 6),
            ("Leilani R1", 6),
        ),
    )
    def test_count_distinct_letter_occurrences(self, name, expected_occurrences):
        assert _count_distinct_letter_occurrences(name) == expected_occurrences

    @pytest.mark.parametrize(
        "name, expected_profile_score",
        (
            ("Leilani R.", 1.15),
            ("", 0),
            (string.ascii_lowercase[:13], 2.5),
            (string.ascii_lowercase, 5),
        ),
    )
    def test__calculate_profile_score(self, name, expected_profile_score):
        assert _calculate_profile_score(name) == expected_profile_score

    @pytest.mark.parametrize(
        "ratings, expected_rating_score",
        (
            ([1], 1),
            ([1, 2, 3], 2),
            ([1, 2, 3, 4], 2.5),
            ([1, 0, 0], 0.33),
        ),
    )
    def test__calculate_ratings_score(self, ratings, expected_rating_score):
        assert _calculate_ratings_score(ratings) == expected_rating_score

    @pytest.mark.parametrize(
        "ratings, profile_score, expected_search_score",
        (
            ([], 2.5, 2.5),
            ([5], 2.5, 2.75),
            ([5, 5], 2.5, 3),
            ([5, 5, 5], 2.5, 3.25),
            ([5, 5, 5, 5], 2.5, 3.5),
            ([5, 5, 5, 5, 5], 2.5, 3.75),
            ([5, 5, 5, 5, 5, 5], 2.5, 4),
            ([5, 5, 5, 5, 5, 5, 5], 2.5, 4.25),
            ([5, 5, 5, 5, 5, 5, 5, 5], 2.5, 4.5),
            ([5, 5, 5, 5, 5, 5, 5, 5, 5], 2.5, 4.75),
            ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 2.5, 5),
            ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 2.5, 5),
            ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 2.5, 5),
        ),
    )
    def test__calculate_search_score(
        self, ratings, profile_score, expected_search_score
    ):
        assert _calculate_search_score(profile_score, ratings) == expected_search_score
