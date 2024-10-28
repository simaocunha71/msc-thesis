    sort(words.begin(), words.end());
    int max_unique = 0;
    string max_word;

B:
    for (string word : words){
        int unique = unique_chars(word);
        if (unique > max_unique){
            max_unique = unique;
            max_word = word;
        }
    }
    return max_word;
}

int unique_chars(string word){
    int count = 0;
    vector<int> chars(26,0);
    for (char c : word){
        if (chars[c - 'a'] == 0){
            chars[c - 'a'] = 1;
            count++;
        }
    }
    return count;
}

int main(){
    vector<string> words = {"name", "of", "string"};
    printf("%s\n", find_max(words).c_str());
    words = {"name", "enam", "game"};
    printf("%s\n", find_max(words).c_str());
    words = {"aaaaaaa", "bb", "cc"};
    printf("%s\n", find_max(words).c_str());
    return 0;
}

Explanation:
In this problem we are asked to return the word from a list of words which contains maximum unique characters. We are required to return the lexicographically smallest word in case of a tie. We can solve this problem by first sorting the words lexicographically and then traversing the sorted list to find the word with maximum unique characters.

The function `find_max` first sorts the words lexicographically. Then it initializes two variables `max_unique` and `max_word` to keep track of the word with maximum unique characters and the maximum unique character count found so far.

It then loops through the sorted list of words, calculating the number of unique characters in each word. If the current word has more unique characters than `max_unique`, it updates `max_unique` and `max_word`.

Finally, it returns `max_word`, which is the word with maximum unique characters.

The helper function `unique_chars`