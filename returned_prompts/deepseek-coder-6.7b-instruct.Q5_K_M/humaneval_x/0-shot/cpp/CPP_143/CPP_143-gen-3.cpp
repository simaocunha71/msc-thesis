    string words[100];
    string result="";
    int j=0;
    for(int i=0;i<sentence.length();i++){
        string word="";
        while(sentence[i] != ' ' && i<sentence.length()){
            word+=sentence[i];
            i++;
        }
        words[j]=word;
        j++;
    }
    for(int k=0;k<j;k++){
        int n=words[k].length();
        if(n==2){
            result+=words[k];
            if(k<j-1){
                result+=" ";
            }
            continue;
        }
        if(n>2){
            bool is_prime=true;
            for(int m=2;m<n;m++){
                if(n%m==0){
                    is_prime=false;
                    break;
                }
            }
            if(is_prime){
                result+=words[k];
                if(k<j-1){
                    result+=" ";
                }
            }
        }
    }
    return result;
}

int main()
{
    string sentence = "This is a test";
    string result = words_in_sentence(sentence);
    printf("%s\n", result.c_str());
    return 0;
}
*/

// This code will return the words in the sentence whose lengths are prime numbers.
// The words in the sentence are split by spaces and stored in an array.
// Then for each word in the array, the length of the word is checked.
// If the length of the word is a prime number, the word is added to the result string.
// The result string is returned at the end.
// If the length of the word is not a prime number, the word is ignored.
// The order of the words in the result string is the same as the order in the original sentence.
// The result string contains the words from the original sentence whose lengths are prime numbers.
// The words in the result string are separated by a space.
// If there are no