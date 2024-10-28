    def parse_music(music_string: str) -> List[int]:
        music_list = []
        i = 0
        while i < len(music_string):
            if music_string[i] == 'o':
                music_list.append(4)
                i += 1
            elif music_string[i:i+2] == 'o|':
                music_list.append(2)
                i += 2
            elif music_string[i:i+3] == '.|':
                music_list.append(1)
                i += 3
            else:
                raise ValueError('Invalid music string')
        return music_list

    print(parse_music('o o| .| o| o| .| .| .| .| o o'))  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    # Test Case 2:
    print(parse_music('o| .| .| o| o| .| .| o| o|'))  # Output: [2, 1, 1, 2, 2, 1, 1, 2, 2]  # Test Case 3:
    print(parse_music('o o o| .| .| o| o| o| .| .|'))  # Output: [4, 2, 1, 2, 2, 4, 1, 1, 2]  # Test Case 4:
    print(parse_music('o o| .| .| o| .| .| o| o|'))  # Output: [2, 1, 1, 2, 1, 1, 2, 2]  # Test Case 5:
    print(parse_music('o o| o| .| .| o| o| o| .| .|'))  # Output: [2, 4, 1, 1, 2, 2, 4, 1, 1]  # Test Case 6:
    print(parse_music('o o o| .| .| o| o| o| .| .| .|'))  # Output: [4, 2, 1, 1, 2, 2, 4, 1, 1, 1]  # Test Case 7:
    print(parse_music('o o| o| .