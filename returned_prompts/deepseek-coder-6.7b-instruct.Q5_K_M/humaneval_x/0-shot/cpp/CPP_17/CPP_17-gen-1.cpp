
    vector<int> result;
    int i = 0;
    while(i < music_string.length()){
        if(music_string[i] == 'o' && music_string[i+1] == ' '){
            result.push_back(4);
            i += 2;
        }
        else if(music_string[i] == 'o' && music_string[i+1] == '|'){
            result.push_back(2);
            i += 2;
        }
        else if(music_string[i] == '.' && music_string[i+1] == '|'){
            result.push_back(1);
            i += 2;
        }
    }
    return result; 
}

int main(){
    string music_string = "o o| .| o| o| .| .| .| .| o o";
    vector<int> result = parse_music(music_string);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}

*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> parse_music(string music_string){ 
    vector<int> result;
    int i = 0;
    while(i < music_string.length()){
        if(music_string[i] == 'o' && music_string[i+1] == ' '){
            result.push_back(4);
            i += 2;
        }
        else if(music_string[i] == 'o' && music_string[i+1] == '|'){
            result.push_back(2);
            i += 2;
        }
        else if(music_string[i] == '.' && music_string[i+1] == '|'){
            result.push_back(1);
            i += 2;
        }
    }
    return result; 
}

int main(){
    string music_