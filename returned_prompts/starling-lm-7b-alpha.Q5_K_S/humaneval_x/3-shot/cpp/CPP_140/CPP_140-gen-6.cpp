    string new_str="";
    bool prev_space=false;
    for (int i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            if (prev_space)
            {
                new_str+='-';
            }
            else
            {
                new_str+='_';
            }
            prev_space=true;
        }
        else
        {
            new_str+=text[i];
            prev_space=false;
        }
    }
    return new_str;
}


