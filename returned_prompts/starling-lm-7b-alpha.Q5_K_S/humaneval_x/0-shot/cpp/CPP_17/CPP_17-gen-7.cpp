    vector<int> res;
    for (char c : music_string) {
        if (c == 'o') {
            res.push_back(4);
        } else if (c == 'o' | c == '|') {
            res.push_back(2);
        } else if (c == '.' | c == '|') {
            res.push_back(1);
        } else {
            return res;
        }
    }
    return res;
}




/*
Given a string containing musical notes in the following format, return a vector of integers representing
how many beats each note lasts:

"o" - whole note, lasts four beats
"o|" - half note, lasts two beats
".|" - quarter note, lasts one beat

>>> parse_music("o o| .| o| o| o")
{4, 2, 1, 2, 2}

>>> parse_music("o o| .| o| o| .| .| .| .| o o")
{4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4}

>>> parse_music("o o| .| o| o| .| .| .| .| .| .| .| .|")
{4, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1}
*/




















































































































































