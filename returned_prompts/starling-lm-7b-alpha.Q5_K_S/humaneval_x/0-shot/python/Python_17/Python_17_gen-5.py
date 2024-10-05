def parse_music(music_string: str) -> List[int]:
    note_list = []
    for note in music_string:
        if note == 'o':
            note_list.append(4)
        elif note == 'o|':
            note_list.append(2)
        elif note == '.':
            note_list.append(1)
    return note_list

# Alternative solution
def parse_music(music_string: str) -> List[int]:
    note_list = []
    for char in music_string:
        if char == 'o':
            note_list.append(4)
        elif char == 'o|':
            note_list.append(2)
        elif char == '.':
            note_list.append(1)
    return note_list

# Alternative solution
def parse_music(music_string: str) -> List[int]:
    return [4 if note == 'o' else 2 if note == 'o|' else 1 for note in music_string]




# Made By Mostafa_Khaled




```
parse_music('o o| .| o| o| o')
```