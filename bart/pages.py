from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Play(Page):
    form_model = 'player'
    form_fields = ['pumps', 'popped']

    def vars_for_template(self):
        total_banked = sum(
            p.round_earnings for p in self.player.in_previous_rounds()
        )
        return {
            'max_pumps': Constants.max_pumps,
            'pump_value': Constants.pump_value,
            'total_banked': total_banked,
        }

    def before_next_page(self):
        self.player.set_payoff()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        all_rounds = self.player.in_all_rounds()
        rounds_data = []
        for p in all_rounds:
            rounds_data.append({
                'round': p.round_number,
                'pumps': p.pumps,
                'popped': p.popped,
                'earnings': p.round_earnings,
            })
        total = sum(p.round_earnings for p in all_rounds)
        return {
            'rounds_data': rounds_data,
            'total_earnings': total,
        }


page_sequence = [
    Instructions,
    Play,
    Results,
]
