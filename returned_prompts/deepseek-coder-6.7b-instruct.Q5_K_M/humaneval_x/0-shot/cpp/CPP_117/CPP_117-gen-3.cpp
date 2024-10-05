    vector<string> words;
    vector<string> result;
    string temp = "";

    for(int i = 0; i < s.size(); i++){
        if(s[i] == ' '){
            words.push_back(temp);
            temp = "";
        } else {
            temp += s[i];
        }
    }
    words.push_back(temp);

    for(int i = 0; i < words.size(); i++){
        int count = 0;
        for(int j = 0; j < words[i].size(); j++){
            if(tolower(words[i][j]) != 'a' && tolower(words[i][j]) != 'e' && tolower(words[i][j]) != 'i' && tolower(words[i][j]) != 'o' && tolower(words[i][j]) != 'u' && tolower(words[i][j]) != ' '){
                count++;
            }
        }
        if(count == n){
            result.push_back(words[i]);
        }
    }
    return result;
}

int main(){
    string s;
    int n;
    printf("Enter a string: ");
    getline(cin,s);
    printf("Enter the number of consonants: ");
    scanf("%d",&n);
    vector<string> res= select_words(s,n);
    for(int i=0;i<res.size();i++){
        printf("%s ",res[i].c_str());
    }
    return 0;
}

Explanation:
The function works by first splitting the string into words and storing them in a vector. It then iterates over each word, counting the number of consonants. If the count of consonants in a word equals n, the word is added to the result vector.

The main function takes a string and a number as input, calls the select_words function with these inputs, and prints the result.

The use of tolower function in the for loop is to consider 'A', 'E', 'I', 'O