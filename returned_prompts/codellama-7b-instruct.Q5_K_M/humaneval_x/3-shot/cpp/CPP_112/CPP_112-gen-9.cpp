    vector<string> result;
    string result_str="";
    for (int i=0;i<s.length();i++)
    if (find(c.begin(),c.end(),s[i])==c.end())
    result_str+=s[i];
    result_str=result_str;
    result.push_back(result_str);
    if (result_str.length()==0)
    result.push_back("False");
    else if (result_str.length()!=0)
    result.push_back("True");
    return result;
}


