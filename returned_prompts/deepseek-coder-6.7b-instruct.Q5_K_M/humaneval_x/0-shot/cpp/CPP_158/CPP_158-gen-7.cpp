    sort(words.begin(), words.end());

B:
    int max_unique = 0;
    string max_word;

C:
    for(string word : words){
        vector<bool> used(26, false);
        int unique = 0;
        for(char c : word){
            if(!used[c - 'a']){
                unique++;
                used[c - 'a'] = true;
            }
        }
        if(unique > max_unique){
            max_unique = unique;
            max_word = word;
        }
    }

D:
    return max_word;
}
int main() {
    vector<string> words = {"name", "of", "string"};
    printf("The word with maximum number of unique characters is: %s", find_max(words).c_str());
    return 0;
}

*/

