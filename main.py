import random as rd


# CLASS

class Player:  # TODO: Remake the system so it's a single-player and not multiplayer
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.score = 0
        self.money = 50

        self.is_dealer = False

    def __str__(self):
        msg = ''
        for card in self.hand:
            msg += f"""
                {card}"""

        score = self.calculate_score()

        return f"""
        {self.name:_^20}:
        
        {score}
        money: ${self.money}

        hand: {msg}"""

    def draw_card(self, n=1):
        colors = ['CLUB', 'DIAMOND', 'HEART', 'SPADE']

        for _ in range(n):
            value = rd.randint(1, 13)
            color = rd.randint(0, 3)

            c = Card(value, colors[color])
            self.hand.append(c)

    def calculate_score(self):
        self.score = 0
        is_as = False

        for c in self.hand:
            self.score += c.value
            if c.value == 11:
                is_as = True

        if self.score > 21 and is_as:
            self.score -= 10

        return f'score: {self.score}'


class Card:  # TODO: Remake the visibility of cards
    def __init__(self, value: int, color: str) -> None:
        self.value = value
        self.color = color.upper()

        self.hidden = False

        figure = {
            1: 'AS',
            11: 'JACK',
            12: 'QUEEN',
            13: 'KING',
            14: 'AS',
        }

        if self.value in figure.keys():
            self.name = figure[self.value]
            if self.name == 'AS':
                self.value = 11
            else:
                self.value = 10

        assert self.value in range(1, 14), f'{self.value} is not a valid value (1 to 13)'
        assert self.color in ['CLUB', 'DIAMOND', 'HEART', 'SPADE'], f'{self.color} is not a color'

    def __str__(self) -> str:
        if not self.hidden:
            try:
                return f"{self.name}:{self.color}"
            except:
                return f"{self.value}:{self.color}"
        else:
            return "[Hidden Card]"

# FUNCTION


def new_player(name=None):
    if name is None:
        name = str(input('name: '))
    return Player(name)


def show_players(players: list):
    msg = ''
    for i, player in enumerate(players):
        msg = msg + f"""
        player_{i}: {player.name}"""
    return msg


def setup(players: list):
    # adding dealer to the game
    d = new_player('Dealer')
    d.is_dealer = True
    players.append(d)

    # adding players in the game
    nb_player = int(input('number of player: '))

    for _ in range(nb_player):
        temp = new_player()
        players.append(temp)

    # adding 2 card to everyone

    for p in players:
        p.draw_card(2)

# PROGRAMME


if __name__ == '__main__':
    players = []
    setup(players)

    for player in players:
        print(player)

# TODO: make a split system and a money system
