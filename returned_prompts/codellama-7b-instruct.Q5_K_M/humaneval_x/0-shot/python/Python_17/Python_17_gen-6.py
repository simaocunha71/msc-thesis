
from collections import deque

class Parser:
    def __init__(self, music_string: str):
        self.music_string = music_string
        self.tokens = deque(self.music_string)

    def parse(self):
        return self._parse_beat()

    def _parse_beat(self):
        beat = 0
        while self.tokens:
            token = self.tokens.popleft()
            if token == 'o':
                beat += 4
            elif token == '|':
                beat += 1
            elif token == '.' and self.tokens[0] == '|':
                self.tokens.popleft()
                beat += 1
            else:
                raise ValueError
        return beat


def parse_music(music_string: str) -> List[int]:
    return Parser(music_string).parse()
