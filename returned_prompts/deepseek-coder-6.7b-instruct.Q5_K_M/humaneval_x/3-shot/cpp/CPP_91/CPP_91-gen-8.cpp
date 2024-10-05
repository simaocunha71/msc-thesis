    int count = 0;
    string temp = "";
    for (int i = 0; i < S.size(); i++)
    {
        if (S[i] == '.' || S[i] == '?' || S[i] == 'A')
        {
            if (temp[0] == 'I')
            {
                count++;
            }
            temp = "";
        }
        else
        {
            temp += S[i];
        }
    }
    if (temp[0] == 'I')
    {
        count++;
    }
    return count;
}

