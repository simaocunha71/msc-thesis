    int i, j, k;
    string words[100];
    string prime_words = "";
    stringstream ss(sentence);
    for (i = 0; ss >> words[i]; i++)
    {
        for (j = 2, k = words[i].length(); j < k && k % j != 0; j++)
        {
            if (j * j > k)
            {
                if (prime_words != "")
                    prime_words += " ";
                prime_words += words[i];
                break;
            }
        }
    }
    return prime_words;
}


