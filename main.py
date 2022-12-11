import random as rd


# CLASS

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []

    def __str__(self):
        return [self.hand[i] for i in range(len(self.hand))]

    def draw_card(self, n=1):
        colors = ['CLUB', 'DIAMOND', 'HEART', 'SPADE']

        for _ in range(n):
            value = rd.randint(1, 13)
            color = rd.randint(0, 3)

            c = Card(value, colors[color])
            self.hand.append(c)


class Card:
    def __init__(self, value: int, color: str) -> None:
        self.value = value
        self.color = color.upper()

        assert self.value in range(1, 14), f'{self.value} is not a valid value (1 to 13)'
        assert self.color in ['CLUB', 'DIAMOND', 'HEART', 'SPADE'], f'{self.color} is not a color'

    def __str__(self) -> str:
        return f"{self.value}:{self.color}"


# PROGRAMME

def new_player():
    name = str(input('name: '))
    return Player(name)


def show_hand(player: 'Player') -> str:
    msg = ''
    for v in player.hand:
        msg = msg + str(v) + '\n'
    return msg


if __name__ == '__main__':
    players = {}
    P1 = new_player()
    players.update({P1.name: P1.hand})

    P1.draw_card(3)
    print(show_hand(P1))
