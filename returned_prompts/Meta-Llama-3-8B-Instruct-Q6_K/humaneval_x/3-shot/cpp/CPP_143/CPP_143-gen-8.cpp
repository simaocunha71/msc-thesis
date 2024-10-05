    string result;
    int i;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' ')
        {
            continue;
        }
        int j;
        for (j=i+1;j<sentence.length();j++)
        {
            if (sentence[j]==' ')
            {
                break;
            }
        }
        string word = sentence.substr(i,j-i);
        if (isPrime(word.length()))
        {
            result+=word+" ";
        }
        i=j;
    }
    return result.substr(0,result.length()-1);
}

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    int i;
    for (i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
} // End of function isPrime. // End of function words_in_sentence. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. // End of code. //