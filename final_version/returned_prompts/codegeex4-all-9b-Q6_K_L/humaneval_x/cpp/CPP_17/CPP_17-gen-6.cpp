vector<int> notes;
int sum=0;
for(int i=0;i<music_string.length();i++)
{
    if(music_string[i]=='o')
    {
        sum=0;
        notes.push_back(4);
    }
    else if(music_string[i]=='.')
    {
        notes.pop_back();
        notes.push_back(1);
    }
    else if(music_string[i]=='|')
    {
        sum++;
        if(sum==2)
        {
            notes.pop_back();
            notes.push_back(2);
        }
        else if(sum==4)
        {
            notes.pop_back();
            notes.push_back(2);
        }
    }
}
return notes;

B:
#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<int> parse_music(string music_string) {
    vector<int> notes;
    int beat = 0;
    for (int i = 0; i < music_string.length(); i++) {
        if (music_string[i] == 'o') {
            beat = 4;
        } else if (music_string[i] == '.') {
            beat = 1;
            notes.pop_back();
        } else if (music_string[i] == '|') {
            if (music_string[i+1] == 'o') {
                beat = 2;
                notes.pop_back();
            } else {
                beat = 1;
            }
        }
        notes.push_back(beat);
    }
    return notes;
}
int main() {
    vector<int> result = parse_music("o o| .| o| o| .| .| .| .| o o");
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> notes;
    for (int i = 0; i < music_string.length(); i++) {
        if (music_string[i] == 'o') {
            notes.push_back(4);
        } else if (music_string[i] == '.') {
            notes.push_back(1);
        } else if (music_string[i] == '|') {
            if (music_string[i+1] == 'o') {
                notes.pop_back();
                notes.push_back(2);
            } else {
