    string fixed_text;
    int i;
    for (i=0;i<text.length();i++)
    if (text[i]==' '){
        if (i==0||i==text.length()-1)
        fixed_text+="_";
        else
        fixed_text+="-";
    }
    else
    fixed_text+=text[i];
    return fixed_text;
}


