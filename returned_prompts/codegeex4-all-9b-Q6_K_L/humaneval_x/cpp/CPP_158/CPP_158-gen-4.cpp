#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
#include<unordered_map>
using namespace std;
string find_max(vector<string> words){
    string result = "";
    int max_unique_chars = 0;
    for (string word : words) {
        unordered_map<char, int> char_count;
        for (char c : word) {
            char_count[c]++;
        }
        if (char_count.size() > max_unique_chars) {
            result = word;
            max_unique_chars = char_count.size();
        } else if (char_count.size() == max_unique_chars && word < result) {
            result = word;
        }
    }
    return result;
}
B:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
#include<unordered_map>
using namespace std;
string find_max(vector<string> words){
    string result = "";
    int max_unique_chars = 0;
    for (string word : words) {
        unordered_map<char, int> char_count;
        for (char c : word) {
            char_count[c]++;
        }
        if (char_count.size() > max_unique_chars) {
            result = word;
            max_unique_chars = char_count.size();
        } else if (char_count.size() == max_unique_chars && word < result) {
            result = word;
        }
    }
    return result;
}

C:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
#include<unordered_map>
using namespace std;
string find_max(vector<string> words){
    string result = "";
    int max_unique_chars = 0;
    for (string word : words) {
        unordered_map<char, int> char_count;
        for (char c : word) {
            char_count[c]++;
        }
        if (char_count.size() > max_unique_chars) {
            result = word;
            max_unique_chars = char_count.size();
        } else if (char_count.size() == max_unique_chars && word < result) {
            result = word;
        }
    }
    return result;
}

D:
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
#include<unordered_map>
using namespace std;
string find_max(vector<string> words){
    string result = "";
    int max_unique_chars = 0;
    for (string word : words) {
        unordered_map<char, int> char_count;
        for (char c : word) {
            char_count[c]++;
        }
        if (char_count.size() > max_unique