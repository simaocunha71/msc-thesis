    string result="";
    bool last_was_space=false;
    for(char c : text)
    {
        if(c==' ')
        {
            if(last_was_space)
                result+="-";
            else
                result+="_";
            last_was_space=true;
        }
        else
        {
            result+=c;
            last_was_space=false;
        }
    }
    return result;
}


