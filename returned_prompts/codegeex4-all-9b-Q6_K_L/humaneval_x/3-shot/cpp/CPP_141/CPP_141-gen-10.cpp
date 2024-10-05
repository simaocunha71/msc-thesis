    int i,counter=0;
    bool isdot=false;
    bool isletter=false;
    bool isvalid=false;
    char chr;
    for (i=0;i<file_name.length();i++)
    {
        chr=file_name[i];
        if (chr>='0'&&chr<='9')
        counter+=1;
        if (chr=='.')
        {
            if (i==0||i==file_name.length()-1)
            return "No";
            isdot=true;
        }
        if (chr>='a'&&chr<='z'||chr>='A'&&chr<='Z')
        isletter=true;
    }
    string substr=file_name.substr(file_name.find('.')+1,file_name.length());
    if (substr=="txt"||substr=="exe"||substr=="dll")
    isvalid=true;
    if (counter>3||isdot==false||isletter==false||isvalid==false)
    return "No";
    return "Yes";
}

