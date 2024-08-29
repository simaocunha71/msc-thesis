#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> words_string(string s){
  vector<string> words;
  stringstream ss(s);
  string word;
  while (ss >> word) {
    words.push_back(word);
  }
  return words;
}
B:
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> words_string(string s){
  vector<string> words;
  stringstream ss(s);
  string word;
  while (ss >> word) {
    words.push_back(word);
  }
  return words;
}

int main() {
  string s = "Hi, my name is John";
  vector<string> result = words_string(s);
  for (const auto& word : result) {
    printf("%s\n", word.c_str());
  }
  return 0;
}
C:
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> words_string(string s){
  vector<string> words;
  stringstream ss(s);
  string word;
  while (ss >> word) {
    words.push_back(word);
  }
  return words;
}

int main() {
  string s = "Hi, my name is John";
  vector<string> result = words_string(s);
  for (const auto& word : result) {
    cout << word << endl;
  }
  return 0;
}
D:
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> words_string(string s){
  vector<string> words;
  stringstream ss(s);
  string word;
  while (ss >> word) {
    words.push_back(word);
  }
  return words;
}

int main() {
  string s = "Hi, my name is John";
  vector<string> result = words_string(s);
  for (const auto& word : result) {
    printf("%s\n", word.c_str());
  }
  return 0;
}

E:
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> words_string(string s){
  vector<string> words;
  stringstream ss(s);
  string word;
  while (ss >> word) {
    words.push_back(word);
  }
  return words;
}

int main() {
  string s = "Hi, my name is John";
  vector<string> result = words_string(s);
  for (const auto& word : result) {
    cout << word <<