    string word, res = "";
    stringstream ss(sentence);
    while (ss >> word) {
        int len = word.length();
        bool isPrime = true;
        if (len < 2)
            isPrime = false;
        else
            for (int i = 2; i * i <= len; ++i) {
                if (len % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        if (isPrime)
            res += word + " ";
    }
    if (res.length() > 0)
        res.pop_back();  // Remove last space
    return res;
}

