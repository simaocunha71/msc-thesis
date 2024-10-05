/*
Given a string, return a vector of words, separated by spaces, where each word is a substring of the original string.
Examples
"Hello World!" ➞ ["Hello", "World!"]
"Hello,World!" ➞ ["Hello", "World!"], ["Hello", "World!"]
"Hello World!" ➞ ["Hello", "World!"], ["Hello", "World!"]
*/
vector<string> split_words(string txt){
    vector<string> words;
    string word = "";
    for (int i = 0; i < txt.length(); i++) {
        if (txt[i] != ' ') {
            word += txt[i];
        } else {
            words.push_back(word);
            word = "";
        }
    }
    words.push_back(word);
    return words;
}

