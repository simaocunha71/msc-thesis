#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using std::string;
using std::vector;
using std::stringstream;
using std::sort;

bool isPrime(int n) {
    if(n <= 1)
        return false;
    if(n <= 3)
        return true;
    if(n % 2 == 0 || n % 3 == 0)
        return false;
    for(int i = 5; i * i <= n; i += 6)
        if(n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

string words_in_sentence(string sentence) {
    stringstream ss(sentence);
    string word;
    string result;
    while(ss >> word) {
        if(isPrime(word.size())) {
            result += word + " ";
        }
    }
    if(result.size() > 0)
        result.pop_back();
    return result;
}

C:
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using std::string;
using std::vector;
using std::stringstream;
using std::sort;

bool isPrime(int n) {
    if(n <= 1)
        return false;
    if(n <= 3)
        return true;
    if(n % 2 == 0 || n % 3 == 0)
        return false;
    for(int i = 5; i * i <= n; i += 6)
        if(n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

string words_in_sentence(string sentence) {
    stringstream ss(sentence);
    string word;
    vector<string> result;
    while(ss >> word) {
        if(isPrime(word.size())) {
            result.push_back(word);
        }
    }
    sort(result.begin(), result.end());
    string output;
    for(auto& w : result) {
        output += w + " ";
    }
    if(output.size() > 0)
        output.pop_back();
    return output;
}

D:
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using std::string;
using std::vector;
using std::stringstream;
using std::sort;

bool isPrime(int n) {
    if(n <= 1)
        return false;
    if(n <= 3)
        return true;
    if(n % 2 == 