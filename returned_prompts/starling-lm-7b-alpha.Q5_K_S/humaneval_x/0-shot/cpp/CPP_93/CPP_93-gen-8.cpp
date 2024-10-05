    string result = "";
    for(int i=0;i<message.length();i++){
        char c = message[i];
        if('a'<=c && c<='z')
            result += toupper(c);
        else if('A'<=c && c<='Z')
            result += tolower(c);
        else{
            result += c;
        }
    }
    // swap all cases
    for(int i=0, j=message.length()-1;i<j;i++,j--)
        swap(result[i],result[j]);
    // replace vowels
    string vowels = "aeiou";
    for(int i=0;i<message.length();i++){
        char c = result[i];
        if(vowels.find(c) != string::npos){
            c = vowels[(vowels.find(c)+2)%5];
            result[i] = c;
        }
    }
    return result;
}

int main(){
    printf("%s\n",encode("test").c_str());
    printf("%s\n",encode("This is a message").c_str());
    return 0;
}

























































































































































































































