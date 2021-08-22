import re
from dataclasses import dataclass, field
from statistics import mean
from typing import List

from numpy import average

MAX_SCORE = 5
ALPHABET_SIZE = 26
NUM_DECIMALS = 2


def _count_distinct_letter_occurrences(string):
    return len(set(re.sub("[^a-zA-Z]+", "", string).lower()))


def _calculate_profile_score(name):
    return round(
        _count_distinct_letter_occurrences(name) * MAX_SCORE / ALPHABET_SIZE,
        NUM_DECIMALS,
    )


def _calculate_ratings_score(ratings):
    return round(mean(ratings), NUM_DECIMALS)


def _calculate_search_score(profile_score, ratings):
    if len(ratings) >= 10:
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
