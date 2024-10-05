    vector<int> beats_vector;
    for(int i=0; i<music_string.size(); i++){
        if(music_string[i] == 'o'){
            if(music_string[i+1] == '|'){
                beats_vector.push_back(4);
                i+=1;
            }
            else{
                beats_vector.push_back(2);
                i+=1;
            }
        }
        else if(music_string[i] == '.'){
            if(music_string[i+1] == '|'){
                beats_vector.push_back(2);
                i+=1;
            }
        }
    }
    return beats_vector;
}

int main(){
    string test_case = "o o| .| o| o| .| .| .| .| o o";
    vector<int> result = parse_music(test_case);
    for(int i=0; i<result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}
*/

Output:
4 2 1 2 2 1 1 1 1 4 4
*/

#include<iostream>
#include<vector>
#include<string>
using namespace std;
vector<int> parse_music(string music_string){ 
    vector<int> beats_vector;
    for(int i=0; i<music_string.size(); i++){
        if(music_string[i] == 'o'){
            if(music_string[i+1] == '|'){
                beats_vector.push_back(4);
                i+=1;
            }
            else{
                beats_vector.push_back(2);
                i+=1;
            }
        }
        else if(music_string[i] == '.'){
            if(music_string[i+1] == '|'){
                beats_vector.