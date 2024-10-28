    string words[100];
    string result = "";
    int j = 0;
    int len = sentence.length();
    for(int i = 0; i < len; i++){
        string temp = "";
        while(sentence[i] != ' ' && i < len){
            temp += sentence[i];
            i++;
        }
        words[j] = temp;
        j++;
    }

B:
    for(int k = 0; k < j; k++){
        int word_length = words[k].length();
        if(word_length == 2 || word_length == 3){
            result += words[k];
            result += ' ';
        }
    }

C:
    if(result.length() > 0){
        result.pop_back();
    }
    return result;
}

// Test cases:
assert(words_in_sentence("