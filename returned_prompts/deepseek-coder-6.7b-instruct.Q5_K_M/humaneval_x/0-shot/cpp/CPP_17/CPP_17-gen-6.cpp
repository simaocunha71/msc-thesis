  vector<int> result;
  for (size_t i = 0; i < music_string.size(); ++i) {
    switch (music_string[i]) {
      case 'o':
        result.push_back(4);
        break;
      case 'o':
        if (music_string[i+1] == '|') {
          result.push_back(2);
          i++;
        }
        break;
      case '.':
        if (music_string[i+1] == '|') {
          result.push_back(1);
          i++;
        }
        break;
    }
  }
  return result;
}
int main()
{
  vector<int> result = parse_music("o o| .| o| o| .| .| .| .| o o");
  for (size_t i = 0; i < result.size(); ++i) {
    printf("%d ", result[i]);
  }
  return 0;
}

Output:
4 2 1 2 2 1 1 1 1 1 4 4
*/



#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> parse_music(string music_string) {
  vector<int> beats;
  for (int i = 0; i < music_string.size(); i++) {
    if (music_string[i] == 'o') {
      if (i+1 < music_string.size() && music_string[i+1] == '|') {
        beats.push_back(2);
        i++;
      }
      else {
        beats.push_back(4);
      }
    }
    else if (music_string[i] == '.') {
      if (i+1 < music_string.size() && music_string[i+1] == '|') {
        beats.push_back(1);
        i++;
      }
    }
  }
  return beats;
