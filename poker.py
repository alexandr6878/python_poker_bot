import random
from collections import Counter

SUITS = ["diamonds", "hearts", "clubs", "spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]


def is_straight(ranks):
  sorted_ranks = sorted(set(ranks), key=RANKS.index)

  # Initialize a counter to keep track of consecutive ranks
  straight_count = 0
  for i in range(len(sorted_ranks) - 1):
    if RANKS.index(sorted_ranks[i + 1]) - RANKS.index(sorted_ranks[i]) == 1:
      straight_count += 1

    if straight_count == 5:
      return True

  return False


def is_flush(suits):
  for suit in SUITS:
    count = suits.count(suit)
    if count == 5:
      return True
  return False


def is_pair(ranks):
  sorted_ranks = sorted(set(ranks), key=RANKS.index)
  pair_counter = 0
  for i in range(len(sorted_ranks) - 1):
    if RANKS.index(sorted_ranks[i + 1]) - RANKS.index(sorted_ranks[i]) == 0:
      pair_counter += 1

  return pair_counter


def create_deck():
  deck = [{'rank': rank, 'suit': suit} for rank in RANKS for suit in SUITS]
  random.shuffle(deck)
  return deck


def deal_cards(deck, number_of_cards):
  return [deck.pop() for i in range(number_of_cards)]


def combinations(community_cards, player_card):
  all_cards = community_cards + player_card
  suits = [card['suit'] for card in all_cards]
  ranks = [card['rank'] for card in all_cards]

  #Check for straight
  straight = is_straight(ranks)
  #-------------------------

  #Check for flush
  flush = is_flush(suits)
  #----------------------

  #Check for straight flush
  straight_flush = is_straight(ranks) and is_flush(suits)
  #------------------------------------------------

  #Check for pairs
  rank_counts = Counter(ranks)
  pairs = []
  set = []
  four = []
  for key, value in rank_counts.items():
    if value == 2:
      pairs.append(key)
    elif value == 3:
      set.append(key)
    elif value == 4:
      four.append(key)
  #-------------------------------------

  if (straight_flush):
    return {'value': 9, "cards": player_card}
  elif len(four) == 1:
    return {'value': 8, "cards": player_card}
  elif len(set) == 1 and len(pairs) >= 1:  #Full House
    return {'value': 7, "cards": player_card}
  elif (flush):
    return {'value': 6, "cards": player_card}
  elif (straight):
    return {'value': 5, "cards": player_card}
  elif len(set) == 1:
    return {'value': 4, "cards": player_card}
  elif len(pairs) >= 2:
    return {'value': 3, "cards": player_card}
  elif len(pairs) == 1:
    return {'value': 2, "cards": player_card}
  else:
    return {'value': 1, "cards": player_card}


def findBiggest(cards):
  max_number = 0
  card_rank = 0
  for card in cards:
    match card['rank']:
      case "a":
        card_rank = 14
      case "k":
        card_rank = 13
      case "q":
        card_rank = 12
      case "j":
        card_rank = 11
      case _:
        card_rank = int(card['rank'])

    if max_number < card_rank:
      max_number = card_rank

  return max_number

def check_winner(player_one_comb, player_two_comb, bot, id):
  if player_one_comb['value'] > player_two_comb['value']:
    bot.send_message(id, "Player one wins")
  elif player_one_comb['value'] < player_two_comb['value']:
    bot.send_message(id, "Player two wins")
  else:
    first_number = findBiggest(player_one_comb['cards'])
    second_number = findBiggest(player_two_comb['cards'])
    if first_number > second_number:
      bot.send_message(id, "playr one wins")
    elif first_number < second_number:
      bot.send_message(id, "playr two wins")
    else:
      bot.send_message(id, "its a tie")