    // Replace all spaces in it with underscores
    for(int i=0; i<text.length(); i++){
        if(text[i] == ' '){
            text[i] = '_';
        }
    }
    // Check if a string has more than 2 consecutive spaces
    for(int i=0; i<text.length()-2; i++){
        if(text[i] == ' ' && text[i+1] == ' ' && text[i+2] == ' '){
            // Replace all consecutive spaces with -
            for(int j=i; j<text.length(); j++){
                if(j == i || text[j] != ' '){
                    i = j;
                    break;
                }
                text[j] = '-';
            }
        }
    }
    return text;
}

int main(){
    string text = "Example   3";
    string result = fix_spaces(text);
    cout << result << endl;
    return 0;
}

