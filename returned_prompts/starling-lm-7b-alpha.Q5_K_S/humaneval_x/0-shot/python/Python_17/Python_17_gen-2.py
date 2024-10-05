def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.': 1}
    return [notes[c] if c in notes else 1 for c in music_string]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    print("All tests are OK")











```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``