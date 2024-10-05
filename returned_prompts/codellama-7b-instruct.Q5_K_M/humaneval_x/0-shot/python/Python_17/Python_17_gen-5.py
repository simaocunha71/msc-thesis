    music = []

    for i in music_string:
        if i == 'o':
            music.append(4)
        elif i == 'o|':
            music.append(2)
        elif i == '.|':
            music.append(1)
        else:
            raise ValueError('Invalid input')

    return music
