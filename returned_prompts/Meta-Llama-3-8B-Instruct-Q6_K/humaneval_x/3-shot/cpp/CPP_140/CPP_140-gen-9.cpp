    string result;
    for (char c:text)
    {
        if (c==' ')
        {
            if (result.size()>0 && result.back()==' ')
            {
                result+="-";
            }
            else
            {
                result+="_";
            }
        }
        else
        {
            result+=c;
        }
    }
    return result;
} 
