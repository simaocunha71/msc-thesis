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

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))

#Output: ('Juan Whelan', 212)
<jupyter_output>
('Juan Whelan', 212)
<jupyter_text>
Question 2
<jupyter_code>
