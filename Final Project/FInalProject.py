import blackjack_games as games
import blackjack_players as players

game = games.Game()
bet = int(input('how much would you like to bet?'))
bet2 = int(input('how much would you like to bet to compare results with your previous bet?'))
game.add_player(players.BaselinePlayer('Baseline Player 1'))
game.add_player(players.SmartPlayer('Smart Player 1'))

number_of_hands = 100000
debug_output = False
for i in range(1, number_of_hands+1):
    game.deal()
    game.play()

    if debug_output:
        print(game)

for p in game.players:
    win_rate = p.wins / (p.wins + p.losses)
    loss_rate = p.losses / (p.wins + p.losses)
    draw_rate = p.draws / (p.wins + p.losses + p.draws)
    win_loss_total_amount = (p.wins * bet) - (p.losses * bet)
    win_loss_total_amount2 = (p.wins * bet2) - (p.losses * bet2)
    print('{0}:{1} wins, {2} losses, {3} draws, {4:.2f} win rate, {5:.2f} loss rate, {6:.2f} draw rate, {7} total amount currently\n'
          .format(p.name, p.wins, p.losses, p.draws, win_rate, loss_rate, draw_rate, win_loss_total_amount))

    print('After the original bet of', bet, ' dollars, resulting in the current amount,',win_loss_total_amount, ', in comparison to money earned/gained if player bet',
          bet2, 'amount is', win_loss_total_amount2, 'in the end\n')

# In my experimentation, I compared two different aspects, one is seeing the affect of bet variance on the total amount,
# The second aspect is an adjusted AI player I created based off odds sheets who should perform better than an baseline player,
# This increased performance due to a strategy from odds sheets

#Final checklist/Rubric- Final Project (below)

# Blackjack game created
# unit tests conducted and passed
# 100000 simuations completed and generate an odds sheet on total wins and losses
# Baseline win/loss total amounts have been generated after 100000 simulations along with rates of winning/losing
# 2 different strategies have been attempted and put against each other to see overall affect



