/*
Input to this function is a string representing musical notes in a special ASCII format.
Your task is to parse this string and return vector of integers corresponding to how many beats does each
not last.

Here is a legend:
"o" - whole note, lasts four beats
"o|" - half note, lasts two beats
".|" - quater note, lasts one beat

>>> parse_music("o o| .| o| o| .| .| .| .| o o")
{4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_music(string music_string){ 
    vector<int> beats;
    string note = "";
    for(int i = 0; i < music_string.length(); i++){
        if(music_string[i] == 'o'){
            note += "o";
            if(i + 1 < music_string.length() && music_string[i + 1] == '|'){
                beats.push_back(4);
                i++;
            }
            else{
                beats.push_back(2);
            }
        }
        else if(music_string[i] == '.'){
            note += ".";
            if(i + 1 < music_string.length() && music_string[i + 1] == '|'){
                beats.push_back(1);
                i++;
            }
            else{
                beats.push_back(0.5);
            }
        }
    }
    return beats;
}
