import random


class Cards:
    def __init__(self):
        self.suits = ['♥️', '♦️', '♣️', '♠️']
        self.nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [suit + num for suit in self.suits for num in self.nums]

    def draw(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card


class Player:
    def __init__(self):
        self.player_cards = []
        self.blook = False

    def score(self):
        score = 0
        for card in self.player_cards:
            if card[2] in ['J', 'Q', 'K']:
                score += 10
            elif card[2] == 'A' and score < 11:
                score += 11
            elif card[2] == 'A':
                score += 1
            else:
                score += int(card[2:])
        return score


class Game:
    def __init__(self):
        self.player = Player()
        self.computer = Player()
        self.cards = Cards()

    def start(self):
        self.player.player_cards.append(self.cards.draw())
        self.player.player_cards.append(self.cards.draw())
        self.computer.player_cards.append(self.cards.draw())
        self.computer.player_cards.append(self.cards.draw())
        print(f'玩家的牌: {self.player.player_cards}')
        print(f'玩家的点数: {self.player.score()}')
        while True:
            if self.player.score() == 21:
                print('玩家 Blackjack!')
                break
            if self.player.score() > 21:
                print(f'玩家爆牌!')
                self.player.blook = True
                break
            print('是否继续抽牌?(y/n)')
            choice = input()
            if choice == 'y':
                self.player.player_cards.append(self.cards.draw())
                print(f'玩家的牌: {self.player.player_cards}')
                print(f'玩家的点数: {self.player.score()}')
            else:
                break
        print(f'电脑的牌: {self.computer.player_cards}')
        print(f'电脑的点数: {self.computer.score()}')
        while True:
            if self.computer.score() == 21:
                print('电脑 Blackjack!')
                break
            if self.computer.score() > 21:
                print(f'电脑爆牌!')
                self.computer.blook = True
                break
            if self.computer.score() < 17:
                self.computer.player_cards.append(self.cards.draw())
                print(f'电脑的牌: {self.computer.player_cards}')
                print(f'电脑的点数: {self.computer.score()}')
            else:
                break

    def win(self):
        if self.player.blook and self.computer.blook:
            print('平局!')
        elif self.player.blook:
            print('电脑胜利!')
        elif self.computer.blook:
            print('玩家胜利!')
        elif self.player.score() > self.computer.score():
            print('玩家胜利!')
        elif self.player.score() < self.computer.score():
            print('电脑胜利!')
        else:
            print('平局!')


game = Game()
game.start()
game.win()
