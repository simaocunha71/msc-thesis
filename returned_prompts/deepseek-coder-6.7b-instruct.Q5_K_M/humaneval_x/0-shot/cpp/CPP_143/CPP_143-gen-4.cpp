    int i,j,flag;
    string word,result="";

B:
    for(i=0;i<sentence.length();i++){
        flag=0;
        word="";
        while(sentence[i] != ' ' && i<sentence.length()){
            word+=sentence[i];
            i++;
        }
        if(word.length()>=2){
            for(j=2;j<=sqrt(word.length());j++){
                if(word.length()%j==0){
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                result+=word+" ";
            }
        }
    }
    if(result.length()>0){
        result.pop_back();
    }
    return result;
}

int main(){
    string sentence;
    printf("Enter the sentence: ");
    getline(cin,sentence);
    string result=words_in_sentence(sentence);
    printf("Result: %s\n",result.c_str());
    return 0;
}
```

When you run this program, it will ask for a sentence and then it will print the words from the sentence that have a length of a prime number.

For example, if you enter "This is a test", the program will output "is". If you enter "lets go for swimming", the program will output "go for".

This program works by splitting the input sentence into words and checking the length of each word. If the length of a word is a prime number, it adds the word to the result string. The order of the words in the result string is the same as the order in the input sentence.

Note: This program assumes that words are separated by a single space and there are no punctuation marks. It also assumes that the input sentence length is less than or equal to 100.

Note: The length of a word is considered to be 2 or more, as prime numbers are defined to be numbers that have only two divisors: 1 and the number itself. The number 1 is not considered a prime number.

Note: The program uses the sqrt