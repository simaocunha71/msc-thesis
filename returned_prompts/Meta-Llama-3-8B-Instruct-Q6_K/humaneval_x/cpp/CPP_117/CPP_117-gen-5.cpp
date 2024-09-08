    vector<string> res;
    s.erase(remove(s.begin(), s.end(), ' '), s.end());
    for(int i=0;i<s.size();i++){
        string word;
        while(i<s.size() && (isalpha(s[i]) || s[i]==' ')){
            if(isalpha(s[i])){
                word += tolower(s[i]);
            }
            i++;
        }
        if(!word.empty()){
            int count=0;
            for(int j=0;j<word.size();j++){
                if(!isalpha(word[j]))
                    continue;
                if(word[j] != 'a' && word[j] != 'e' && word[j] != 'i' && word[j] != 'o' && word[j] != 'u')
                    count++;
            }
            if(count==n)
                res.push_back(word);
        }
    }
    return res;
}

int main(){
    vector<string> res = select_words("Mary had a little lamb", 4);
    for(auto it = res.begin(); it != res.end(); ++it)
        cout << *it << " ";
    return 0;
}

Explanation:

This C++ program is designed to solve the problem described in the question. The `select_words` function takes a string `s` and an integer `n` as input and returns a vector of all words from `s` that contain exactly `n` consonants, in the order they appear in `s`.

Here's a step-by-step explanation of the program:

1. The `select_words` function is defined, which takes a string `s` and an integer `n` as input.
2. The function first removes all spaces from the input string `s` using the `erase` and `remove` functions.
3. Then, it iterates through the modified string `s` and constructs words by concatenating characters until it encounters a non-alphabetic character or the end of the string.
4. For each constructed word, it counts the number of consonants using a loop that checks if each character is a vowel or not.
5. If the word contains exactly `n` consonants, it is added to the result vector `res`.
6. Finally, the function returns the result vector `res`.
7. In the `main` function, the `select_words` function is called with the input string "Mary had a little lamb" and `n=4`, and the result is printed to the console.

The output of the program will