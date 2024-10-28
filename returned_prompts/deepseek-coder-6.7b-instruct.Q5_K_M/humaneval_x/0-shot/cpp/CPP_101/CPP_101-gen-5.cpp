    vector<string> result;
    size_t pos = 0, next_pos = 0;
    string delimiter = " ,";
    while ((next_pos = s.find_first_of(delimiter, pos)) != string::npos) {
        if (next_pos != pos)
            result.push_back(s.substr(pos, next_pos - pos));
        pos = next_pos + 1;
    }
    if(pos < s.size())
        result.push_back(s.substr(pos));
    return result;
}

int main() {
    vector<string> words = words_string("Hi, my name is John");
    for(string word : words) {
        printf("%s\n", word.c_str());
    }
    return 0;
}

*/

// This program splits the input string into words based on whitespace and commas, and returns a vector of these words.
// It uses the `find_first_of` method of the string class, which returns the position of the first character in the string that is found in the given set of characters.
// In this case, the set of characters is " ," which includes whitespace and comma.
// If the position is not `string::npos` (which it is if the character is not found), it means a delimiter was found.
// The `substr` method is then used to extract a substring from the original string from the current position to the position of the found delimiter.
// This substring is then added to the vector.
// The process is repeated until all characters in the string have been processed.
// The final word is added to the vector separately because there are no more delimiters after the final word.
// The vector of words is then returned.
// The `main` function tests this function by splitting the string "Hi, my name is John" into words and printing them.
// The output should be:
// Hi
// my
// name
// is
// John
// This is just an example, the same process can be used to split any string into words.

// This is a simple and efficient way to split a string into words in C++.
