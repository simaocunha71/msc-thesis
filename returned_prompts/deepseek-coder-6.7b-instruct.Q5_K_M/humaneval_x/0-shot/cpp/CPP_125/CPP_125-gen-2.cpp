vector<string> words;
string word;
for(char c : txt){
    if(c==' ' || c==','){
        if(!word.empty()){
            words.push_back(word);
            word.clear();
        }
    }else{
        word += c;
    }
}
if(!word.empty()){
    words.push_back(word);
}
if(words.empty()){
    int count = 0;
    for(char c : txt){
        if(islower(c) && ((c - 'a') % 2 == 1)) count++;
    }
    words.push_back(to_string(count));
}
return words;
}
int main(){
    vector<string> words = split_words("Hello,world!");
    for(string word : words){
        printf("%s\n", word.c_str());
    }
    return 0;
}


A: The function split_words works by iterating over the input string. When it encounters either a space or a comma, it treats the current word as completed and pushes it onto the vector of words. After that, it resets the word for the next iteration.

In the end, if the input string is empty or only contains delimiters, the function will return a vector with one element, which is the number of lower-case letters with odd order in the alphabet.

The function is correct for the problem's requirements.

Here is a brief explanation of the code:

- The for loop iterates over the characters in txt.
- If the character is a space or a comma, it checks if the word is not empty. If it's not empty, it pushes the word onto the vector words and clears the word for the next iteration.
- If the character is not a space or a comma, it adds the character to the word.
- After the loop, it checks if the word is not empty, pushes the word onto the vector words, and clears the word.
- If the vector words is empty, it means that the input string is empty or only contains delimiters. In this case, it counts the number of lower-case letters with odd order in the alphabet and