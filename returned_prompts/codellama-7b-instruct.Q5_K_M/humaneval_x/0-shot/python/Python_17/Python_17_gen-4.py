    music_list = music_string.split()
    return [4 if x == 'o' else 2 if x == 'o|' else 1 for x in music_list]
