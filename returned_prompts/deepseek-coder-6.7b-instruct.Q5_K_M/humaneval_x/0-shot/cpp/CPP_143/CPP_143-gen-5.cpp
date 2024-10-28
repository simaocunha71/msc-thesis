    int count = 0, len = sentence.length();
    string word = "", result = "";
    for (int i = 0; i <= len; ++i){
        if (sentence[i] != ' ' && sentence[i]){
            word += sentence[i];
        }
        else{
            for (int j = 2; j < word.length(); ++j){
                if (word.length() % j == 0){
                    count = 1;
                    break;
                }
            }
            if (count == 0 && word.length() != 0){
                result += word + " ";
            }
            count = 0;
            word = "";
        }
    }
    if (result.length() > 0){
        result.pop_back();
    }
    return result;
}

int main(){
    string sentence;
    getline(cin,sentence);
    cout<<words_in_sentence(sentence);
    return 0;
}
*/

