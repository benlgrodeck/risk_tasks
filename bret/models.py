from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'bret'
    players_per_group = None
    num_rounds = 1
    num_boxes = 25  # 5x5 grid
    points_per_box = 10


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.bomb_location = random.randint(1, Constants.num_boxes)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    boxes_collected = models.IntegerField(min=0, initial=0)
    bomb_location = models.IntegerField()
    bomb_hit = models.BooleanField(initial=False)
    earnings = models.IntegerField(initial=0)

    def set_payoff(self):
        if self.bomb_hit:
            self.earnings = 0
        else:
            self.earnings = self.boxes_collected * Constants.points_per_box
        self.payoff = c(self.earnings)
