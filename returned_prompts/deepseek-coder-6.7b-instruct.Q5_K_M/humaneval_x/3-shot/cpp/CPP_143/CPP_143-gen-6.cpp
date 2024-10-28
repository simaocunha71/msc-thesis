    for  (int p=2; p*p<=n; p++)
    {
        if  (is_prime[p] == true)
        {
            for  (int i=p*p; i<=n; i += p)
                is_prime[i] = false;
        }
    }
    string new_sentence = "";
    string word = "";
    for  (int i = 0; i < sentence.size(); i++)
    {
        if  (sentence[i] == ' ')
        {
            if  (is_prime[word.size()])
                new_sentence = new_sentence + " " + word;
            word = "";
        }
        else
        {
