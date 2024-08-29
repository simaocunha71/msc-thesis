def max_aggregate(lst):
    players = {}

    for player, score in lst:
        if player in players:
            players[player] += score
        else:
            players[player] = score

    max_score = max(players.values())
    max_player = [player for player, score in players.items() if score == max_score]

    return (max_player[0], max_score)