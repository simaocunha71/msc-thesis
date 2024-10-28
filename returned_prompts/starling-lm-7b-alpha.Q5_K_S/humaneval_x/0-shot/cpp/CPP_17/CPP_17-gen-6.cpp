	int index = 0, value = 0;
	vector<int> result;
	while (index < music_string.size()) {
		if (music_string[index] == 'o') {
			result.push_back(4);
			index += 1;
		} else if (music_string[index] == 'o' && music_string[index + 1] == '|') {
			result.push_back(2);
			index += 2;
		} else if (music_string[index] == '.' && music_string[index + 1] == '|') {
			result.push_back(1);
			index += 2;
		}
	}
	return result;
}


/*
Write a function parse_music that takes a string of musical notes in a special ASCII format and returns a
vector of integers that represents how many beats each note lasts.

Input to this function is a string representing musical notes in a special ASCII format.
Your task is to parse this string and return vector of integers corresponding to how many beats does each
not last.

Here is a legend:
"o" - whole note, lasts four beats
"o|" - half note, lasts two beats
".|" - quater note, lasts one beat

>>> parse_music("o o| .| o| o| o| .| .| .| .| o o")
{4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4}

For example, the string "o o| .| o| o| o| .| .| .| .| o o" should be parsed as follows:

The first note is an "o" which corresponds to 4 beats, the next note is an "o|" which also corresponds to 4 beats,
the third note is a "." which corresponds to 1 beat, and so on.

The function should return a vector of integers representing how many beats each note in the string lasts.
*/
