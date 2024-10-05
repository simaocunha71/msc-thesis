    // I have to return a string that contains the words from the original sentence,
    // whose lengths are prime numbers,
    // the order of the words in the new string should be the same as the original one.
    // Example 1:
    //     Input: sentence = "This is a test"
    //     Output: "is"
    // Example 2:
    //     Input: sentence = "lets go for swimming"
    //     Output: "go for"
    // Constraints:
    //     * 1 <= len(sentence) <= 100
    //     * sentence contains only letters
*/
string result;
string word;
bool prime;

for(int i = 0; i < sentence.length(); i++){
    if(sentence[i] == ' '){
        word[prime] = '\0';
        result += word;
        prime = false;
    }else if(sentence[i] != ' '){
        word += sentence[i];
        prime = true;
    }
}
return result;
}
