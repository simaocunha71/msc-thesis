    // Split the string into words
    string word;
    string result = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ' '){
            result += word + " ";
            word = "";
        }else{
            word += s[i];
        }
    }
    result += word;

    // Arrange the words in ascending order of ASCII values
    vector<string> words;
    for(int i = 0; i < result.length(); i++){
        if(result[i] == ' '){
            words.push_back(result.substr(0, i));
            result = result.substr(i+1);
            i = 0;
        }
    }
    words.push_back(result);
    sort(words.begin(), words.end());

    // Arrange the characters in each word in ascending order of ASCII values
    result = "";
    for(int i = 0; i < words.size(); i++){
        string temp = words[i];
        sort(temp.begin(), temp.end());
        result += temp + " ";
    }

    // Remove the trailing space
    result = result.substr(0, result.length()-1);

    return result;
}

int main(){
    printf("%s\n", anti_shuffle("Hello World!!!").c_str());
    return 0;
}

