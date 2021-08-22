import pytest

from models.sitter import Sitter
from models.sitters import Sitters


class TestSitters:
    @pytest.mark.parametrize(
        "original, normalized",
        (
            ("pablo@gmail.com", "pablo@gmail.com"),
            ("Pablo@Gmail.com", "pablo@gmail.com"),
        ),
    )
    def test__normalize_email(self, original, normalized):
        assert Sitters._normalize_email(original) == normalized

    def test_add_stay(self):
        sitters = Sitters()
        assert len(sitters.sitters) == 0  # empty of sitters for now

        sitters.add_stay("foo", "email1", 0)
        assert sitters._sitters["email1"].search_score == 0.34  # new sitter
        sitters.add_stay("bar", "email1", 0)
        assert (
            sitters._sitters["email1"].search_score == 0.3
        )  # sitter with email1 got updated
        sitters.add_stay("banana", "email2", 0)
        assert sitters._sitters["email2"].search_score == 0.52  # new sitter

        assert len(sitters.sitters) == 2
        all_names = [sitter.name for sitter in sitters.sitters]
        assert "foo", "banana" in all_names
        # bar has the same email as a previous sitter so this name shouldn't be in the list
        assert "bar" not in all_names

    def test_get_sitters_order(self):
        """
        Let's check that the sitters are returned in descending order by search_score and
        by alphabetical name in case of draw.
        The correct order by score should be email2, email4, email3 and email1.
        """
        # let's create an scenario of sitter and stays
        sitters = Sitters()
        sitters.add_stay("a", "email1", 1)
        sitters.add_stay("b", "email2", 5)
        sitters.add_stay("d", "email3", 4)
        sitters.add_stay("c", "email4", 4)

        internal_order = [sitter.email for sitter in list(sitters._sitters.values())]
        # internally the order is the same as the stays join the system
        assert internal_order == ["email1", "email2", "email3", "email4"]

        all_sitters = sitters.sitters

        # quick check about the type of sitters returned
        for sitter in sitters.sitters:
            assert isinstance(sitter, Sitter)

        assert len(all_sitters) == 4
        # sitters are returned from more score to less score,
        # and note that in case of draw between email3 and email4, email4 takes precedence
        # since name "c" is before name "d"
        assert (all_sitters[0].email, all_sitters[0].search_score) == ("email2", 0.67)
        assert (all_sitters[1].email, all_sitters[1].search_score) == ("email4", 0.57)
        assert (all_sitters[2].email, all_sitters[2].search_score) == ("email3", 0.57)
        assert (all_sitters[3].email, all_sitters[3].search_score) == ("email1", 0.27)
