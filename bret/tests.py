from otree.api import Currency as c, currency_range, expect, Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield 'bret/Instructions'
        yield 'bret/Play', dict(boxes_collected=10, bomb_hit=False)
        yield 'bret/Results'
