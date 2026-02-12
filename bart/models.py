from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'bart'
    players_per_group = None
    num_rounds = 3
    max_pumps = 64
    pump_value = 0.05  # $0.05 per pump


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pumps = models.IntegerField(min=0, initial=0)
    popped = models.BooleanField(initial=False)
    round_earnings = models.CurrencyField(initial=0)

    def set_payoff(self):
        if self.popped:
            self.round_earnings = c(0)
        else:
            self.round_earnings = c(self.pumps * Constants.pump_value)

        # On the final round, sum up all round earnings as the payoff
        if self.round_number == Constants.num_rounds:
            self.payoff = sum(
                p.round_earnings for p in self.in_all_rounds()
            )
