    string s = to_string(x);
    int len = s.length();
    if (shift >= len)
        reverse(s.begin(), s.end());
    else {
        rotate(s.begin(),s.begin()+s.length()-shift,s.end());
    }
    return s;
}

