#include <string>
using namespace std;

string fix_spaces(string text){
    string ans;
    for (int i = 0; i < text.size(); i++) {
        if (text[i] == ' ') {
            ans += "_";
            while (i < text.size() && text[i] == ' ') {
                i++;
            }
            i--;
            if (i < text.size() - 2 && text[i+1] == ' ' && text[i+2] == ' ') {
                ans += "-";
            }
        } else {
            ans += text[i];
        }
    }
    return ans;
}

