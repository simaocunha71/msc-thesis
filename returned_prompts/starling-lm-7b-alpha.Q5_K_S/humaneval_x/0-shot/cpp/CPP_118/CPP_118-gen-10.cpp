    int length = word.size();
    if(length <= 1) return "";
    for(int i = 1; i < length - 1; i++){
        if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u'){
            if(word[i - 1] == 'a' || word[i - 1] == 'e' || word[i - 1] == 'i' || word[i - 1] == 'o' || word[i - 1] == 'u') continue;
            if(word[i + 1] == 'a' || word[i + 1] == 'e' || word[i + 1] == 'i' || word[i + 1] == 'o' || word[i + 1] == 'u') continue;
            return word.substr(i, 1);
        }
    }
    return "";
}
int main(){
    string word;
    while(cin >> word){
        string ret = get_closest_vowel(word);
        if(ret == "") printf("No\n");
        else printf("Yes %s\n", ret.c_str());
    }
    return 0;
}

*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    string word;
    cin >> word;
    vector<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    string ret = "";
    for (int i = 1; i < word.size() - 1; i++) {
        if (vowels.end() == find(vowels.begin(), vowels.end(), word[i])) continue;
        if (vowels.end() == find(vowels.begin(), vowels.end(), word[i - 1])) continue;
        if (vowels.end() == find(vowels.begin(), vowels.end