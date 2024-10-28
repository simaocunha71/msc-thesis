    if  (strings.size()==0)
    return "";
    string longest=strings[0];
    for  (int i=0;i<strings.size();i++)
    if  (strings[i].length()>longest.length())
    longest=strings[i];
    return longest;
}


