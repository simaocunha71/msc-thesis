    string result = "";
    string word;
    int count = 0;
    for(int i = 0; i < sentence.length(); i++){
        if(sentence[i] == ' '){
            count++;
            if(isPrime(word.length())){
                result += word + " ";
            }
            word = "";
        }else{
            word += sentence[i];
        }
    }
    if(isPrime(word.length())){
        result += word;
    }
    return result;
}
int isPrime(int num){
    if(num <= 1)
        return 0;
    for(int i = 2; i * i <= num; i++){
        if(num % i == 0)
            return 0;
    }
    return 1;
}
int main()
{
    string s = "This is a test";
    cout<<words_in_sentence(s)<<endl;
    return 0;
}

B:
    string words_in_sentence(string sentence){
        string result = "";
        for(string word : split(sentence, " ")){
            if(isPrime(word.length())){
                result += word + " ";
            }
        }
        return result.trim();
    }
    string split(string str, string delimiter){
        string result[100];
        size_t pos = 0;
        int count = 0;
        while((pos = str.find(delimiter)) != string::npos){
            result[count] = str.substr(0, pos);
            str.erase(0, pos + delimiter.length());
            count++;
        }
        result[count] = str;
        return result[0];
    }
    int isPrime(int num){
        if(num <= 1)
            return 0;
        for(int i = 2; i * i <= num; i++){
            if(num % i == 0)
                return 0;
        }
        return 1;
    }
    int main()
    {
        string s = "This is a test";
        cout<<words_in_sentence(s)<<endl;
        return 0;
    }
C:
    string words_in_sentence(string sentence){
        string result = "";
        for(string word : split(sentence, " ")){
            if(isPrime(word.length())){
                result += word + " ";
            }
        }
        return result.substr(0, result.length() - 1);
    }
    string split(string str, string delimiter){
        string result[100];
        size_t pos = 0;
        int count = 0;
        while((pos = str.find(delimiter))