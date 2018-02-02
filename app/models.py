import random


class Pocker:
    cards = [
        'ch_2', 'ch_3', 'ch_4', 'ch_5', 'ch_6', 'ch_7', 'ch_8', 'ch_9', 'ch_10', 'ch_v', 'ch_q', 'ch_k', 'ch_a', 'ch_j',
        'bubi_2', 'bubi_3', 'bubi_4', 'bubi_5', 'bubi_6', 'bubi_7', 'bubi_8', 'bubi_9', 'bubi_10', 'bubi_v', 'bubi_q',
        'bubi_k', 'bubi_a', 'bubi_j',
        'vini_2', 'vini_3', 'vini_4', 'vini_5', 'vini_6', 'vini_7', 'vini_8', 'vini_9', 'vini_10', 'vini_v', 'vini_q',
        'vini_k', 'vini_a', 'vini_j',
        'kresti_2', 'kresti_3', 'kresti_4', 'kresti_5', 'kresti_6', 'kresti_7', 'kresti_8', 'kresti_9', 'kresti_10',
        'kresti_v', 'kresti_q', 'kresti_k', 'kresti_a', 'kresti_j'
    ]

    def __init__(self, players_ws_list):
        self.mixed_cards = random.choices(self.cards, k=len(self.cards))
        print(self.mixed_cards)
        self.players_ws_list = players_ws_list
        self.turns_num = 0
        self.game_finished = False

    def game_turn(self):
        pass


class Player:
    def __init__(self, name, points, ws):
        self.name = name
        self.points = points
        self.cards = []
        self.ws = ws
        self.money = 100

    def make_turn(self):
        pass
