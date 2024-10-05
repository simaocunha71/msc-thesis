    sort(words.begin(), words.end());

B:
    int max_unique = 0;
    string max_word;

C:
    for(string word : words){
        int unique = unique_chars(word);
        if(unique > max_unique){
            max_unique = unique;
            max_word = word;
        }
    }

D:
    return max_word;
}

// Function to count unique characters in a word
int unique_chars(string word){
    vector<bool> chars(26, false);
    for(char c : word){
        chars[c - 'a'] = true;
    }
    return count(chars.begin(), chars.end(), true);
}


The function first sorts the vector of words in lexicographical order. Then, it iterates through each word, counting the number of unique characters. If the number of unique characters for a word is greater than the current maximum unique character count, that word is stored as the new maximum word and the count is updated. Finally, the function returns the word with the maximum number of unique characters.
*/

// main function
int main(){
    vector<string> words = {"name", "of", "string"};
    cout << find_max(words) << endl;  // 'string'
    return 0;
}



// 