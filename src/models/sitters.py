from models.sitter import Sitter


class Sitters:
    """
    All sitters would be stored in a dictionary where the key would be sitter's email and the value
    would be a Sitter instance
    """

    def __init__(self):
        self._sitters = {}

    @staticmethod
    def _normalize_email(name):
        """Get rid of not important things from the email"""
        return name.lower()

    def add_stay(self, name, email, rating):
        normalized_email = self._normalize_email(email)
        if normalized_email in self._sitters:
            # if the sitter is in place then only update it
            self._sitters[normalized_email].add_stay(rating)
        else:  # if it's not, add the sitter and then update its first scores
            self._sitters[normalized_email] = Sitter(name, normalized_email)
            self._sitters[normalized_email].add_stay(rating)

    @property
    def get_sitters(self):
        return sorted(
            list(self._sitters.values()), key=lambda x: (-x.search_score, x.name)
        )
