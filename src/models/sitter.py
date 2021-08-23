import re
from dataclasses import dataclass, field
from statistics import mean
from typing import List

from numpy import average

MAX_SCORE = 5
ALPHABET_SIZE = 26
NUM_DECIMALS = 2


def _count_distinct_letter_occurrences(string):
    """Count how many different letters there are in a string"""
    return len(set(re.sub("[^a-zA-Z]+", "", string).lower()))


def _calculate_profile_score(name):
    """
    The profile score is 5 times the fraction of the English alphabet
    comprised by the distinct letters.
    """
    return round(
        _count_distinct_letter_occurrences(name) * MAX_SCORE / ALPHABET_SIZE,
        NUM_DECIMALS,
    )


def _calculate_ratings_score(ratings):
    """
    The ratings score is the average of their stay ratings.
    """
    return round(mean(ratings), NUM_DECIMALS)


def _calculate_search_score(profile_score, ratings):
    """
    When a sitter has no stays, their search score is equal to the profile score.
    When a sitter has 10 or more stays, their search score is equal to the ratings score.
    When a sitter has between 1 and 9 stays is a weighted average of
    the profile score and ratings.
    """
    if len(ratings) >= 10:
        # more than 9 ratings then this score is the same as rating score
        return _calculate_ratings_score(ratings)
    # else weighted average calculation
    return round(
        average(
            [profile_score] + ratings,
            weights=[1 - (len(ratings) * 0.1)] + len(ratings) * [0.1],
        ),
        2,
    )


@dataclass
class Sitter:
    name: str
    email: str
    profile_score: int = 0
    ratings_score: float = 0
    search_score: float = 0
    _ratings: List[int] = field(default_factory=list)

    def __post_init__(self):
        self.profile_score = _calculate_profile_score(self.name)
        self.search_score = _calculate_search_score(self.profile_score, self._ratings)

    def add_stay(self, rating):
        self._ratings.append(rating)
        self.ratings_score = _calculate_ratings_score(self._ratings)
        self.search_score = _calculate_search_score(self.profile_score, self._ratings)
