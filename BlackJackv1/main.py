import random as rd
from time import sleep

# CLASS


class Player:
    """
    Class for making Player object (for Dealer to)
    """
    def __init__(self, name):
        self.name = name
        self.hand = []

        self.money = 50
        self.amount = 0

        self.is_dealer = False

    def __str__(self):
        if not self.is_dealer:
            return f"""
{self.name:_<20}:

    score: {self.get_score()}
    money: {self.money}
    bet: {self.amount}

    hand: {self.show_hand()}
        """

        else:
            return f"""
{self.name:_<20}:

    score: {self.get_score()}

    hand: {self.show_hand()}
        """

    def bet(self):
        while True:
            self.amount = int(input("amount of the bet: "))
            if self.amount <= self.money:
                self.money -= self.amount
                break

    def draw_card(self, n=1):
        print(f"{self.name} draw a card!")
        colors = ['CLUB', 'DIAMOND', 'HEART', 'SPADE']

        for _ in range(n):
            value = rd.randint(1, 14)
            color = rd.randint(0, 3)

            self.hand.append(Card(value, colors[color]))

    def show_hand(self):
        msg = ''
        for card in self.hand:
            msg += f"""
            {card}"""
        return msg

    def get_score(self):
        score = 0
        is_as = 0

        for card in self.hand:
            score += card.value
            try:
                if card.name == 'AS':
                    is_as = True  # TODO: set so if there are multiple AS's it can use them as one
            except:
                continue

        while is_as > 0 and score > 21:
            score -= 10
            is_as -= 1

        return score

    def is_busted(self):
        score = self.get_score()

        if score > 21:
            return True
        else:
            return False


class Card:
    """
    Class for making Card object (value and color) with black jake rules
    """
    def __init__(self, value: int, color: str) -> None:
        self.value = value
        self.color = color.upper()

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
        try:
            return f"{self.name}:{self.color}"
        except:
            return f"{self.value}:{self.color}"


# PROGRAMME

if __name__ == '__main__':
    # setup
    dealer, player = Player("Dealer"), Player("Samuel")  # Player(str(input("name: ")))
    dealer.is_dealer = True

    while player.money > 0:
        # start of game
        # step 1: bet phase
        player.bet()

        # step 2: drawing phase
        dealer.draw_card()
        player.draw_card(2)

        # step 3: looking at our score and hand
        print(dealer)
        print(player)

        # start of player turn
        while True:
            if player.is_busted():
                print(f"{player.name} is Busted!")
                break

            question = str(input("draw a card ?[y/n]:"))
            # TODO: set double down
            # TODO: set split

            if question == 'y':
                player.draw_card()
            elif question == 'n':
                break
            else:
                continue

            print(player)

        # start of dealer turn
        dealer.draw_card()
        print(dealer)
        while not player.is_busted():
            sleep(2)
            if dealer.is_busted():
                print(f"{dealer.name} is Busted!")
                break

            if dealer.get_score() < player.get_score():
                dealer.draw_card()
                print(dealer)
                continue
            else:
                break

        # Who win
        amount = player.amount
        if player.is_busted() or player.get_score() < dealer.get_score():
            print(f"{dealer.name} win")
        elif dealer.is_busted() or dealer.get_score() < player.get_score():
            print(f"{player.name} win {amount * 2}")
            player.money += amount * 2
        else:
            # TODO: Push = take back the bet
            # TODO: Draw = take back half of it
            print(f"Push, nobody win, receive {amount // 2}")
            player.money += amount // 2

        player.hand = []
        dealer.hand = []

        print(player)

    print(f"{player.name} lose because he's out of money")

