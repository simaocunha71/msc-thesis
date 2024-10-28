def parse_music(music_string: str) -> List[int]:
    notes_length = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    music_list = music_string.split(' ')
    notes_list = []
    for i in range(len(music_list)):
        if music_list[i] not in notes_length:
            notes_list.append(notes_length[music_list[i]])
        else:
            notes_list.append(notes_length[music_list[i][0]])
    return notes_list


def test_parse_music():
    assert parse_music('o o| .| o| o| o') == [4, 2, 1, 2, 2, 1]
    assert parse_music('o| .| .| .| .| .') == [2, 1, 1, 1, 1, 1]
    assert parse_music('.| .| .| .| .') == [1, 1, 1, 1]
    assert parse_music('o o') == [4, 4]
    assert parse_music('o| o') == [2, 2]
    assert parse_music('.| .') == [1, 1]
    assert parse_music('o| .| .| .') == [2, 1, 1]
    assert parse_music('o o| .| o') == [4, 2, 2]
    assert parse_music('o| o| .| .') == [2, 2, 1]
    assert parse_music('o| .| o| o') == [2, 1, 2]
    assert parse_music('o| o| .| .| o') == [2, 2, 1, 2]
    assert parse_music('o| o| .| .| .') == [2, 2, 1, 1]
    assert parse_music('o| .| .| .| .| .') == [2