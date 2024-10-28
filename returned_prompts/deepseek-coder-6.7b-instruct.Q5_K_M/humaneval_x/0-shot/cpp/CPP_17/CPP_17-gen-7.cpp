    vector<int> result;
    string::iterator it;
    int beat = 0;
    for(it=music_string.begin();it<music_string.end();it++){
        switch(*it){
            case 'o': beat = 4; break;
            case '|': beat /= 2; break;
            case '.': beat /= 4; break;
            default: continue;
        }
        result.push_back(beat);
    }
    return result;
}

int main(){
    vector<int> result = parse_music("o o| .| o| o| .| .| .| .| o o");
    for(int i=0; i<result.size(); i++)
        printf("%d ", result[i]);
    return 0;
}
```

## Answer:
The problem is asking to parse the given string and return a vector of integers representing the duration of each note in beats.

In the given string, 'o' represents a whole note which lasts for 4 beats, '|' represents half or quater note and '.' represents a quater note.

The '|' character changes the beat duration depending on the previous character. If the previous character is 'o' it means the note is half long, so divide the beat by 2. If the previous character is '.' it means the note is a quater note, so divide the beat by 4.

We iterate over the given string and update the beat accordingly for each character. We then push the beat into the result vector.

Finally, we return the result vector.

The complexity of this solution is O(n), where n is the length of the given string.

Here is the code:

```C++
#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<int> parse_music(string music_string){ 
    vector<int> result;
    int beat = 4; // initialize beat to 4
    for(char &c : music_string){
        switch(c){
            case 'o': beat = 4; break;
            case '|': beat /= 2; break;
