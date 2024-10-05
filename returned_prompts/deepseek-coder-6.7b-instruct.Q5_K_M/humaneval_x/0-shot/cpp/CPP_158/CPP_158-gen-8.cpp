    sort(words.begin(), words.end());
    int max_unique_count = 0;
    string max_word = "";

B:
    for(auto word: words){
        vector<int> visited(26, 0);
        int unique_count = 0;
        for(char c: word){
            if(visited[c-'a'] == 0){
                unique_count++;
                visited[c-'a'] = 1;
            }
        }
        if(unique_count > max_unique_count){
            max_unique_count = unique_count;
            max_word = word;
        }
    }
    return max_word;
}
*/

*/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string find_max(vector<string> words){
    string max_word = "";
    int max_unique = 0;

    for(string word : words){
        vector<bool> visited(26, false);
        int unique = 0;
        for(char c : word){
            if(!visited[c - 'a']){
                unique++;
                visited[c - 'a'] = true;
            }
        }
        if(unique > max_unique){
            max_unique = unique;
            max_word = word;
        } else if(unique == max_unique){
            if(word < max_word){
                max_word = word;
            }
        }
    }

    return max_word;
}

int main(){
    vector<string> words = {"name", "of", "string"};
    cout << find_max(words) << endl;
    return 0;
}
/*
E:
*/

//src/main.cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string find_max(vector<string> words){
    string max_word = "";
    int max_unique = 0;

    for(string word : words){
        vector<bool> visited(26,