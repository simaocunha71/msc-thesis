    string s=str;
    string r=s;
    reverse(r.begin(),r.end());
    int i=0;
    while(i<s.size() && s[i]==r[0])
    {
        i++;
        r.erase(0,1);
    }
    if (r.size()==0)
    return s;
    else
    return s+r;
}
int main() {
    string str="cata";
    cout << make_palindrome(str) << endl;
    return 0;
}
