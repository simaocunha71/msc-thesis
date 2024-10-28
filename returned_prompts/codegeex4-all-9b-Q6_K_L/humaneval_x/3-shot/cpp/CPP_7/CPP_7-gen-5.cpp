    vector<string> new_strings;
    string chr;
    int i,j;
    for (i=0;i<strings.size();i++)
    for (j=0;j<strings[i].length();j++)
    {
        chr=strings[i][j];
        if (chr==substring[0]){
            new_strings.push_back(strings[i]);
            break;
        }
    }
    return new_strings;
}

