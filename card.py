class Card:
    """
    Класс карты
    """
    idx_values_card = None
    idx_suit_card = None
    VALUES_CARD_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    # ♡ - \u2661 / Hearts   (Червы)
    # ♢ - \u2662 / Diamonds (Бубны)
    # ♧ - \u2667 / Clubs    (Трефы)
    # ♤ - \u2664 / Spades   (Пики)
    SUIT_CARDS_LIST = ['\u2664', '\u2667', '\u2662', '\u2661']
    TITLE_SUIT_CARDS_LIST = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    str_card = None

    def __init__(self, value, suit):
        self.idx_values_card = self.VALUES_CARD_LIST.index(value)
        self.idx_suit_card = self.TITLE_SUIT_CARDS_LIST.index(suit)
        self.str_card = self.to_str()

    def to_str(self):
        return self.VALUES_CARD_LIST[self.idx_values_card] + self.SUIT_CARDS_LIST[self.idx_suit_card]

    def equal_values(self, second_card):
        return self.idx_values_card == second_card.idx_values_card

    def equal_suit(self, second_card):
        return self.idx_suit_card == second_card.idx_suit_card

    def more(self, second_card):
        if self.idx_values_card == second_card.idx_values_card:
            return self.idx_suit_card > second_card.idx_suit_card
        else:
            return self.idx_values_card > second_card.idx_values_card

    def less(self, second_card):
        if self.idx_values_card == second_card.idx_values_card:
            return self.idx_suit_card < second_card.idx_suit_card
        else:
            return self.idx_values_card < second_card.idx_values_card
