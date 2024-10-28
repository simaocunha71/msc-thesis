    string str_x = to_string(x);
    int len = str_x.length();
    if(shift>=len)
        reverse(str_x.begin(), str_x.end());
    else
    {
        rotate(str_x.begin(),str_x.begin()+str_x.length()-shift,str_x.end());
    }
    return str_x;
}


