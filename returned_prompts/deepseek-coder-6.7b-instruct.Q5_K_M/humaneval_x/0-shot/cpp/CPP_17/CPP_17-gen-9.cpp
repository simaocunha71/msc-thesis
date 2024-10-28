    vector<int> result;
    int pos = 0;
    while(pos < music_string.length()){
        if(music_string[pos] == 'o'){
            if(music_string[pos+1] == '|'){
                result.push_back(1);
                pos += 2;
            }
            else{
                result.push_back(4);
                pos += 2;
            }
        }
        else if(music_string[pos] == '.'){
            if(music_string[pos+1] == '|'){
                result.push_back(2);
                pos += 2;
            }
            else{
                result.push_back(1);
                pos += 2;
            }
        }
    }
    return result;
}

int main(){
    vector<int> v = parse_music("o o| .");
    for(int i = 0; i < v.size(); i++){
        printf("%d ", v[i]);
    }
    return 0;
}
```
This code creates a vector of integers that represent the duration of each note in beats. It iterates through the string, checking for the presence of the special ASCII characters to determine the duration of each note and adds this value to the vector.

This code does not handle the case where the string ends with a note that doesn't have a trailing "|". In such a case, the code would throw an out of bounds exception. You could add a check at the end of the string to ensure that the last character is "|" before trying to add the value to the vector.

This code also assumes that the input string is well-formed and doesn't contain any unexpected characters. If this is not the case, you would need to add error checking code to handle these cases.

Finally, the code uses printf to print the values in the vector. You could replace this with any method of printing the values that you prefer.

This code is written in C++. If you want to write it in a different language, you would need to adjust the syntax and conventions of that language.

Note: This code assumes that the input string is well-formed. If the string is