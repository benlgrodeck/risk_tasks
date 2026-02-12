from otree.api import Currency as c, currency_range, expect, Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield 'bart/Instructions'

        yield 'bart/Play', dict(pumps=5, popped=False)

        if self.round_number == Constants.num_rounds:
            yield 'bart/Results'
