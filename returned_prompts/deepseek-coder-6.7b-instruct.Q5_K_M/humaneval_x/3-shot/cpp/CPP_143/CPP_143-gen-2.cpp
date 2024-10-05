    string words[100];
    string result = "";
    int j = 0;
    for (int i = 0; i < sentence.length(); i++)
    {
        string word = "";
        while (sentence[i] != ' ' && i < sentence.length())
        {
            word += sentence[i];
            i++;
        }
        words[j] = word;
        j++;
    }
    for (int k = 0; k < j; k++)
    {
        int flag = 0;
        if (words[k].length() > 1)
        {
            for (int l = 2; l <= words[k].length() / 2; l++)
            {
                if (words[k].length() % l == 0)
                {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0)
            {
                result += words[k] + " ";
            }
        }
    }
    return result.substr(0, result.length() - 1);
}


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 


A: 

