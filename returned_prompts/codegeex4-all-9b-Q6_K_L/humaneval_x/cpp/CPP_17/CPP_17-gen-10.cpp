#include <string>
#include <vector>
using namespace std;
vector<int> parse_music(string music_string){
    vector<int> res;
    int i = 0;
    while(i < music_string.size()){
        if(music_string[i] == 'o'){
            res.push_back(4);
            i++;
        }
        else if(music_string[i] == '.'){
            i++;
            res.push_back(1);
        }
        else{
            i++;
        }
    }
    return res;
}