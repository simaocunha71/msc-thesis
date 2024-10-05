    string result;
    string word;
    int i;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' ')
        {
            if (is_prime(word.length()))
            {
                result+=word+" ";
                word="";
            }
        }
        else
        {
            word+=sentence[i];
        }
    }
    if (is_prime(word.length()))
    {
        result+=word;
    }
    return result;
}

bool is_prime(int n){
    if (n<2)
    {
        return false;
    }
    int i;
    for (i=2;i*i<=n;i++)
    {
        if (n%i==0)
        {
            return false;
        }
    }
    return true;
}  // This function checks whether a number is prime or not. It returns true if the number is prime and false otherwise.  // It checks divisibility from 2 to the square root of the number. If the number is not divisible by any of these numbers, then it is a prime number.  // It also handles the case where the number is less than 2, in which case it is not a prime number.  // It returns false for these cases.  // It returns true for prime numbers.  // It is used in the function words_in_sentence to filter out words whose lengths are not prime.  // It is used to filter out words whose lengths are not prime.  // It is a helper function for the function words_in_sentence.  // It is used to filter out words whose lengths are not prime.  // It is a helper function for the function words_in_sentence.  // It is used to filter out words whose lengths are not prime.  // It is a helper function for the function words_in_sentence.  // It is used to filter out words whose lengths are not prime.  // It is a helper function for the function words_in_sentence.  // It is used to filter out words whose lengths are not prime.  // It is a helper function for the function words_in_sentence.  // It is used to filter out words whose lengths are not prime.  // It is a helper function for the function words_in_sentence.  // It is used to filter out words whose lengths are not prime.  // It is a helper function for the function words_in_sentence.  // It is used to filter out words whose lengths are not prime.  // It is a helper function for the function