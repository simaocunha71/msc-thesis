    vector<string> res;
    vector<string> v;
    for(int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            v.push_back(s.substr(i - 1, i));
            i--;
        } else if (i == s.size() - 1) {
            v.push_back(s.substr(i - 1, i + 1));
        }
    }
    for(int i = 0; i < v.size(); i++) {
        int c = 0;
        for(int j = 0; j < v[i].size(); j++) {
            if (!isalpha(v[i][j])) continue;
            if (!isvowel(v[i][j])) c++;
        }
        if (c == n) res.push_back(v[i]);
    }
    return res;
}


/*
Given a string s, a set of words w, and a natural number n, you have been tasked to implement 
a function that returns a vector of all words from string s that contain exactly n consecutive 
words from the set w, in order these words appear in the string s. If the string s is empty then the 
function should return an empty vector. Note: the order of the consecutive words in the set w is 
the same as the order of the words in the set.
Examples:
consecutive_words("Mary had a little lamb", {"little"}, 1) ==> {"little"}
consecutive_words("Mary had a little lamb", {"little"}, 2) ==> {}
consecutive_words("Mary had a little lamb", {"little", "lamb"}, 2) ==> {"little lamb"}
consecutive_words("Mary had a little lamb", {"little", "lamb"}, 1) ==> {"little"}
consecutive_words("Mary had a little lamb", {"little"}, 3) ==> {}
consecutive_words("Mary had a little lamb", {"little"}, 4) ==> {}
consecutive_words("Mary