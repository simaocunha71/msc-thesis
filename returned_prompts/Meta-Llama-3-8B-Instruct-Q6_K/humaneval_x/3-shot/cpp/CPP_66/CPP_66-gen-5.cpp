    int sum=0;
    for(int i=0;i<s.size();i++)
    {
        if(isupper(s[i]))
        {
            sum+=int(s[i]);
        }
    }
    return sum;
}
// OR
int digitSum(string s){
    int sum=0;
    for(char c:s)
        if(isupper(c))
            sum+=c;
    return sum;
} // This one is more efficient. It iterates over the string only once.