    vector<int> beats;
    int i = 0;
    while(i < music_string.size()){
        if(music_string[i] == 'o' && music_string[i+1] == ' '){
            beats.push_back(4);
            i += 2;
        }else if(music_string[i] == 'o' && music_string[i+1] == '|'){
            beats.push_back(2);
            i += 2;
        }else if(music_string[i] == '.' && music_string[i+1] == '|'){
            beats.push_back(1);
            i += 2;
        }
    }
    return beats;
}

int main(){
    vector<int> beats = parse_music("o o| .| o| o| .| .| .| .| o o");
    for(int i = 0; i < beats.size(); i++){
        printf("%d ", beats[i]);
    }
    return 0;
}
*/

The code above will parse the given string and will return a vector of integers representing the number of beats each note lasts. It first initializes an empty vector of integers called beats. Then, it uses a while loop to iterate through the given string. For each character in the string, it checks if it is a "o", a "|", or a ".", and based on that, it pushes the corresponding integer to the beats vector. Finally, it returns the beats vector.

The main function is just to test the parse_music function. It calls the function with the given string and prints the returned vector of integers.

Please note that this code assumes that the input string will always be well-formed and will not contain any errors. If the input string could have errors, the code would need to be modified to handle these errors.
*/

