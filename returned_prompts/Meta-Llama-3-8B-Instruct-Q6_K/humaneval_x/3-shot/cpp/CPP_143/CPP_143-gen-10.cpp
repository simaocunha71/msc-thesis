    string result = "";
    int i;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' ')
        {
            continue;
        }
        string word;
        while (i<sentence.length() && sentence[i]!=' ')
        {
            word+=sentence[i];
            i++;
        }
        i--;
        if (is_prime(word.length()))
        {
            result+=word+" ";
        }
    }
    return result.trim();
}

int is_prime(int n){
    if (n<=1)
    return 0;
    for (int i=2;i*i<=n;i++)
    {
        if (n%i==0)
        return 0;
    }
    return 1;
}  // This function checks if a given number is prime or not. It returns 1 if the number is prime and 0 otherwise.  // It checks divisibility of the number from 2 to square root of the number.  // If the number is not divisible by any number in this range, then it is a prime number.  // If the number is divisible by any number in this range, then it is not a prime number.  // So, the function returns 1 if the number is prime, and 0 if the number is not prime.  // This function is used in the words_in_sentence function to check if the length of the word is a prime number or not.  // It is used to filter out the words whose lengths are not prime numbers.  // The words whose lengths are prime numbers are added to the result string.  // The function returns the result string which contains the words from the original sentence, whose lengths are prime numbers, in the same order as the original sentence.  // This function uses a helper function is_prime to check if a number is prime or not.  // The helper function is_prime is used to check if the length of the word is a prime number or not.  // If the length of the word is a prime number, then the word is added to the result string.  // The function returns the result string which contains the words from the original sentence, whose lengths are prime numbers, in the same order as the original sentence.  // The function is used to filter out the words whose lengths are not prime numbers, and to keep the words whose lengths are prime numbers.  // This function is used to solve the problem of finding the words from the original sentence, whose lengths are prime numbers,