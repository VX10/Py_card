from deck import Deck
import random


def cmp_cards(card_one, cards_list):
    """
    фн поиска у игрока2 минимальной старшей карты
    возращает индекс найденной карты, если карта не найдена, то вернёт None
    """
    for index, item in enumerate(cards_list):
        if item.more(card_one):
            return index
    return None


def sort_cards(cards_list):
    """
    фн сортировки карт по возрастанию
    """
    for i in range(len(cards_list)):
        for j in range(len(cards_list) - 1):
            if cards_list[j].more(cards_list[j + 1]):
                cards_list.insert(j, cards_list.pop(j + 1))


def find_similar(cards_pattern, cards_on_field):
    """
    фн поиска карты у игрока1, значение которой такое же, как у одной из карт, лежащих на столе
    иначе, возвращает None
    """
    for index_pattern, item_pattern in enumerate(cards_pattern):
        for item_field in cards_on_field:
            if item_pattern.equal_values(item_field):
                return index_pattern
    return None


# точка входа в программу
if __name__ == '__main__':

    deck = Deck()
    cards_player1 = None
    cards_player2 = None
    cards_on_field = []
    idx_sort = []
    step = 0

    print('Колода (новая):')
    print(deck.show()[10:])  # удаляю "deck[52]:" (который есть по заданию в фн "show")

    print('\nКолода (перемешанная):')
    deck.shuffle()
    print(deck.show()[10:])  # удаляю "deck[52]:" (который есть по заданию в фн "show")

    print()
    cards_player1 = deck.draw(10)
    sort_cards(cards_player1)
    print('Раздали первому игроку:', end=' ')
    for item in cards_player1:
        print(item.to_str(), end=' ')

    print()
    cards_player2 = deck.draw(10)
    sort_cards(cards_player2)
    print('Раздали второму игроку:', end=' ')
    for item in cards_player2:
        print(item.to_str(), end=' ')

    # игровой цикл
    while True:
        step += 1

        if step == 1:
            # игрок1 кидает случайную карту
            random_index = random.randint(0, len(cards_player1) - 1)
            rand_card1 = cards_player1.pop(random_index)
        else:
            similar_card = find_similar(cards_player1, cards_on_field)
            if similar_card is None:
                print('\n\nИгрок 2 выиграл.')
                break
            else:
                rand_card1 = cards_player1.pop(similar_card)

        print(f'\n\nХод {step}')
        print(f'Игрок 1: {rand_card1.to_str()}')
        cards_on_field.append(rand_card1)

        print(f'Игрок 2: ', end='')
        # игрок2 проверяет минимальную старшию карту
        cmp_result = cmp_cards(rand_card1, cards_player2)
        # если есть карта старше, то игрок2 кидает эту карту
        if cmp_result is not None:
            for index, item in enumerate(cards_player2):
                if cmp_result == index:
                    select_card2 = cards_player2.pop(index)
                    print(select_card2.to_str(), '(покрыл)')
                    cards_on_field.append(select_card2)
                    break
        else:
            print('не смог покрыть')
            print('\nИгрок 1 выиграл.')
            break

        if len(cards_player2) == 0:
            print('\nИгрок 2 выиграл.')
            break

        print('\nКакие карты выбрасывались:', end=' ')
        for item in cards_on_field:
            print(item.to_str(), end=' ')

        print('\nУ первого игрока осталось:', end=' ')
        for item in cards_player1:
            print(item.to_str(), end=' ')

        print('\nУ второго игрока осталось:', end=' ')
        for item in cards_player2:
            print(item.to_str(), end=' ')
