from card import Card
import random


class Deck:
    """
    Класс колоды
    """
    cards = None

    def __init__(self):
        self.cards = []
        # заполняем полную упорядоченную колоду из 52 шт.
        for item_suit in reversed(Card.TITLE_SUIT_CARDS_LIST):
            for item_value in Card.VALUES_CARD_LIST:
                self.cards.append(Card(item_value, item_suit))
        pass

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, x):
        slice_list = self.cards[:x]
        self.cards = self.cards[x:]
        return slice_list

    def show(self):
        value_string = f"deck[{len(self.cards)}]: "
        for index in range(len(self.cards)):
            value_string += self.cards[index].to_str() + ', '
        return value_string[:-2]
