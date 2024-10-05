    string words[100],prime_words="";
    int count=0,i,j,len;
    len=sentence.length();
    for(i=0;i<len;i++)
    {
        string word="";
        while(i<len && sentence[i] != ' ')
        {
            word+=sentence[i];
            i++;
        }
        words[count]=word;
        count++;
    }
    for(i=0;i<count;i++)
    {
        int flag=0;
        int length_of_word=words[i].length();
        if(length_of_word>1){
            for(j=2;j*j<=length_of_word;j++)
            {
                if(length_of_word%j==0)
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                prime_words=prime_words+words[i]+' ';
            }
        }
    }
    return prime_words;
}

int main()
{
    string sentence;
    printf("Enter a sentence: ");
    getline(cin,sentence);
    string result = words_in_sentence(sentence);
    printf("Words with prime lengths: %s",result.c_str());
    return 0;
}

*/

This is a C++ solution for the problem. The function words_in_sentence takes in a string sentence and returns a string of words that have prime lengths. The function first splits the input sentence into words, then checks if the length of each word is a prime number. If it is, it adds the word to the result string prime_words. The function then returns this string. 

The main function takes in a sentence, calls the words_in_sentence function with this sentence, and then prints the returned string.

Note: This solution assumes that words in the sentence are separated by a single space and there are no multiple spaces between words. Also, it doesn't handle punctuation at the end of words.

It's also important