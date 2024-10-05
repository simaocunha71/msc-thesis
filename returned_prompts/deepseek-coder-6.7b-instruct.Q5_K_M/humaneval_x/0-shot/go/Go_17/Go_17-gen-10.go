
	arr := []int{}
	split_music := strings.Split(music_string, " ")
	for _, note := range split_music {
		switch note {
		case "o":
			arr = append(arr, 4)
		case "o|":
			arr = append(arr, 2)
		case ".|":
			arr = append(arr, 1)
		}
	}
	return arr
}

func main() {

	music := "o o| .| o| o| .| .| .| .| o o"
	beats := ParseMusic(music)
	fmt.Println(beats)
}
```

## Python Solution:

```python
def ParseMusic(music_string):
    notes = music_string.split()
    beats = []
    for note in notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    return beats

music = "o o| .| o| o| .| .| .| .| o o"
beats = ParseMusic(music)
print(beats)
```

This Python solution works by splitting the input string by spaces to get a list of notes. It then iterates over each note, appending the corresponding number of beats to a new list. Finally, it returns the list of beats.

## JavaScript Solution:

```javascript
function ParseMusic(music_string) {
    let notes = music_string.split(' ');
    let beats = [];
    for (let i = 0; i < notes.length; i++) {
        switch(notes[i]) {
            case 'o':
                beats.push(4);
                break;
            case 'o|':
                beats.push(2);
                break;
            case '.|':
                beats.push(1);
                break;
        }
    }
    return beats;
}