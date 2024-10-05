    vector<int> beats;
    for(int i=0;i<music_string.length();i++){
        if(music_string[i]=='o' && music_string[i+1]==' '){
            beats.push_back(4);
        }
        else if(music_string[i]=='o' && music_string[i+1]=='|'){
            beats.push_back(2);
            i++;
        }
        else if(music_string[i]=='.' && music_string[i+1]=='|'){
            beats.push_back(1);
            i++;
        }
    }
    return beats;
}

int main(){
    string test = "o o| .| o| o| .| .| .| .| o o";
    vector<int> output = parse_music(test);
    for(int i=0;i<output.size();i++){
        printf("%d ", output[i]);
    }
    return 0;
}
```

This program will iterate through the string and check the character and the next character to determine the length of the note. If the note is a whole note, it will push 4 to the vector. If it's a half note, it will push 2. If it's a quater note, it will push 1. It then prints the vector to the console.

The time complexity of this program is O(n) where n is the length of the string. This is because it iterates through the string once. The space complexity is also O(n) where n is the number of notes in the string. This is because it stores the lengths of the notes in a vector.

This program assumes that the input string is well-formed and does not contain any errors. If the input string is not well-formed, the program will not work correctly.
