    vector<string> v;
    s.erase(remove_if(s.begin(),s.end(),[&c](char x){return c.find(x)!=string::npos;}),s.end());
    v.push_back(s);
    v.push_back(is_palindrome(s));
    return v;
}



