import random
import os


class Card:

    def __init__(self, card_face, value, symbol):
        self.card_face = card_face
        self.value = value
        self.symbol = symbol


def show_cards(cards, hidden):
    s = ''
    for card in cards:
        s = s + '\t ________________'
    if hidden:
        s += '\t ________________'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        if card.card_face in ['J', 'Q', 'K', 'A']:
            s = s + '\t|  {}             |'.format(card.card_face)
        elif card.value == 10:
            s = s + '\t|  {}            |'.format(card.value)
        else:
            s = s + '\t|  {}             |'.format(card.value)

    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|      * *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|    *     *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|   *       *    |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|       {}        |'.format(card.symbol)
    if hidden:
        s += '\t|          *     |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|         *      |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|                |'
    if hidden:
        s += '\t|                |'
    print(s)

    s = ''
    for card in cards:
        if card.card_face in ['J', 'Q', 'K', 'A']:
            s = s + '\t|            {}   |'.format(card.card_face)
        elif card.value == 10:
            s = s + '\t|           {}   |'.format(card.value)
        else:
            s = s + '\t|            {}   |'.format(card.value)
    if hidden:
        s += '\t|        *       |'
    print(s)

    s = ''
    for card in cards:
        s = s + '\t|________________|'
    if hidden:
        s += '\t|________________|'
    print(s)
    print()


def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card, deck


def play_blackjack(deck):
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    os.system('Очистить')

    while len(player_cards) < 2:
        player_card, deck = deal_card(deck)
        player_cards.append(player_card)
        player_score += player_card.value

        if len(player_cards) == 2:
            if player_cards[0].value == 11 and player_cards[1].value == 11:
                player_cards[0].value = 1
                player_score -= 10

        print('КАРТЫ ИГРОКА:  ')
        show_cards(player_cards, False)
        print('СЧЕТ ИГРОКА =  ', player_score)

        input('Продолжать...')

        dealer_card, deck = deal_card(deck)
        dealer_cards.append(dealer_card)
        dealer_score += dealer_card.value

        # If dealt a second Ace, adjust dealer score
        # Note: adjusts 2nd card to hide that the dealer has an Ace
        if len(dealer_cards) == 2:
            if dealer_cards[0].value == 11 and dealer_cards[1].value == 11:
                dealer_cards[1].value = 1
                dealer_score -= 10

        print('КАРТЫ ДИЛЕРА:  ')
        if len(dealer_cards) == 1:
            show_cards(dealer_cards, False)
            print('СЧЕТ ДИЛЕРА =  ', dealer_score)
        else:
            show_cards(dealer_cards[:-1], True)
            print('СЧЕТ ДИЛЕРА =  ', dealer_score - dealer_cards[-1].value)

        input('Продолжать...')

    if player_score == 21:
        print('У ИГРОКА ЕСТЬ БЛЭКДЖЕК!!!!')
        print('ИГРОК ВЫИГРЫВАЕТ!!!!')
        quit()
    os.system('Очистить')

    print('КАРТЫ ДИЛЕРА:  ')
    show_cards(dealer_cards[:-1], True)
    print('СЧЕТ ДИЛЕРА =  ', dealer_score - dealer_cards[-1].value)
    print()
    print('КАРТЫ ИГРОКА:  ')
    show_cards(player_cards, False)
    print('СЧЕТ ИГРОКА =  ', player_score)

    while player_score < 21:
        choice = input('Введите H, чтобы ударить, или S, чтобы встать:').upper()
        if len(choice) != 1 or (choice not in ['H', 'S']):
            os.system('Очистить')
            print('Неверный выбор!! пробовать снова...')
            continue

        if choice.upper() == 'S':
            break
        else:
            player_card, deck = deal_card(deck)
            player_cards.append(player_card)
            player_score += player_card.value
            card_pos = 0

            # If dealt an Ace, adjust score for each existing Ace in hand
            while player_score > 21 and card_pos < len(player_cards):
                if player_cards[card_pos].value == 11:
                    player_cards[card_pos].value = 1
                    player_score -= 10
                    card_pos += 1
                else:
                    card_pos += 1

            if player_score > 21:
                break

            os.system('Очистить')
            print('КАРТЫ ДИЛЕРА:  ')
            show_cards(dealer_cards[:-1], True)
            print('СЧЕТ ДИЛЕРА =  ', dealer_score - dealer_cards[-1].value)
            print()
            print('КАРТЫ ИГРОКА:  ')
            show_cards(player_cards, False)
            print('СЧЕТ ИГРОКА =  ', player_score)

    os.system('Очистить')
    print('КАРТЫ ИГРОКА:  ')
    show_cards(player_cards, False)
    print('СЧЕТ ИГРОКА =  ', player_score)
    print()
    print('ДИЛЕР РАСКРЫВАЕТ СВОИ КАРТЫ....')
    print('КАРТЫ ДИЛЕРА:  ')
    show_cards(dealer_cards, False)
    print('СЧЕТ ДИЛЕРА =  ', dealer_score)

    if player_score == 21:
        print('У ИГРОКА ЕСТЬ БЛЭКДЖЕК, ИГРОК ВЫИГРЫВАЕТ!!!')
        quit()

    if player_score > 21:
        print('ИГРОК ПОЙМАН!!! ИГРА ОКОНЧЕНА!!!')
        quit()

    input('Продолжать...')
    while dealer_score < 17:
        os.system('Очистить')
        print('ДИЛЕР РЕШАЕТ НАНЕСТИ УДАР.....')
        dealer_card, deck = deal_card(deck)
        dealer_cards.append(dealer_card)
        dealer_score += dealer_card.value

        # If dealt an Ace, adjust score for each existing Ace in hand
        card_pos = 0
        while dealer_score > 21 and card_pos < len(dealer_cards):
            if dealer_cards[card_pos].value == 11:
                dealer_cards[card_pos].value = 1
                dealer_score -= 10
                card_pos += 1
            else:
                card_pos += 1

        print('КАРТЫ ИГРОКА:  ')
        show_cards(player_cards, False)
        print('СЧЕТ ИГРОКА =  ', player_score)
        print()
        print('КАРТЫ ДИЛЕРА:  ')
        show_cards(dealer_cards, False)
        print('СЧЕТ ДИЛЕРА =  ', dealer_score)
        if dealer_score > 21:
            break
        input('Продолжать...')

    if dealer_score > 21:
        print('ДИЛЕР ПОПАЛСЯ!!! ВЫ ВЫИГРАЛИ!!!')
        quit()
    elif dealer_score == 21:
        print('У ДИЛЕРА БЛЭКДЖЕК!!! ИГРОК ПРОИГРЫВАЕТ!!!')
        quit()
    elif dealer_score == player_score:
        print('ИГРА вничью!!!!')
    elif player_score > dealer_score:
        print('ИГРОК ВЫИГРЫВАЕТ!!!')
    else:
        print('ДИЛЕР ВЫИГРЫВАЕТ!!!')


def init_deck():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    # UNICODE values for card symbol images
    suit_symbols = {'Hearts': '\u2661', 'Diamonds': '\u2662',
                   'Spades': '\u2664', 'Clubs': '\u2667'}
    cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    deck = []
    for suit in suits:
        for card, value in cards.items():
            deck.append(Card(card, value, suit_symbols[suit]))
    return deck


if __name__ == '__main__':
    deck = init_deck()
    play_blackjack(deck)