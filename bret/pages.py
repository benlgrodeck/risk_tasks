from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Play(Page):
    form_model = 'player'
    form_fields = ['boxes_collected', 'bomb_hit']

    def vars_for_template(self):
        return {
            'num_boxes': Constants.num_boxes,
            'points_per_box': Constants.points_per_box,
            'bomb_location': self.player.bomb_location,
        }

    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):
    def vars_for_template(self):
        return {
            'bomb_location': self.player.bomb_location,
            'bomb_hit': self.player.bomb_hit,
            'boxes_collected': self.player.boxes_collected,
            'earnings': self.player.earnings,
            'points_per_box': Constants.points_per_box,
        }


page_sequence = [
    Instructions,
    Play,
    Results,
]
