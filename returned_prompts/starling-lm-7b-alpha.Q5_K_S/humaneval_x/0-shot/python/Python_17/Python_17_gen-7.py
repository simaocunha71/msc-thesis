def parse_music(music_string: str) -> List[int]:
    music_notes = music_string.split(" ")
    res = []
    for note in music_notes:
        if note == "o":
            res.append(4)
        elif note == "o|":
            res.append(2)
        elif note == ".|":
            res.append(1)
    return res


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    # print(parse_music('o o| .| o| o| .| .| .| .| o o'))
    # print(parse_music('o .| .| o| .| .| .| .| .| o o'))
    # print(parse_music('o o| .| o| .| .| .| .| .| .| o o'))
    assert parse_music('o o| .| o| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o .| .| o| .| .| .| .| .| .| o o') == [4, 1, 1, 2, 1, 1, 1, 1, 1, 4, 4]
    assert parse_music('o o| .| o| .| .| .| .| .| .| o o') == [4, 2, 1, 1, 1, 1, 1, 1, 1, 4, 4]
    print("all tests passed")



























































```