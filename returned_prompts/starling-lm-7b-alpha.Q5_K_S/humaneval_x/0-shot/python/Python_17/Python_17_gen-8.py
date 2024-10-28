def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
    notes = [note.replace('|', '') for