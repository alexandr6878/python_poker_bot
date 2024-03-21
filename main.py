import telebot
import poker
# from telebot import types
SUITS = ["diamonds", "hearts", "clubs", "spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]

bot = telebot.TeleBot("7014625991:AAEWWbWXozSuTHP1ObGmR8l5XOahlWNqQls")
@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.from_user.id, "if you want to play send me /deal")
@bot.message_handler(commands=["deal"])
def deal(message):
  deck = poker.create_deck()
  player_one = poker.deal_cards(deck, 2)
  player_two = poker.deal_cards(deck, 2)
  community_cards = poker.deal_cards(deck, 5)
  player_one_comb = poker.combinations(community_cards, player_one)
  player_two_comb = poker.combinations(community_cards, player_two)
  print(f"player one have{player_one_comb}, player two have {player_two_comb}")

  print(f'community cards are {community_cards}')
  poker.check_winner(player_one_comb, player_two_comb, bot, message.from_user.id)

#TODO: Instead of x player wins - First player cards: - 1 - 2 Cards on a table - 1 Second player cards 1, 2 Combinations (1, 2 player), who won
bot.polling(none_stop=True, interval=0)
