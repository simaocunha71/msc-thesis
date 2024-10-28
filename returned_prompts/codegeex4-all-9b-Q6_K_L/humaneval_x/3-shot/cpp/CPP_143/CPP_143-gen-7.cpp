    string result="";
    string temp="";
    int i;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]!=' ')
        {
            temp+=sentence[i];
        }
        else
        {
            if (is_prime(temp.length())){
                result+=temp;
                result+=" ";
            }
            temp="";
        }
    }
    return result;
}

