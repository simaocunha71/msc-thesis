    string t="";
    for(int i=0;i<s.size();i++)
    {
        if(s[i]>='a'&&s[i]<='z')
        {
            int k=s[i]+2*2;
            while(k>123)
            {
                k=k-26;
            }
            t+=char(k);
        }
        else if(s[i]>='A'&&s[i]<='Z')
        {
            int k=s[i]+2*2;
            while(k>91)
            {
                k=k-26;
            }
            t+=char(k);
        }
        else
        {
            t+=s[i];
        }
    }
    return t;
}
int main()
{
    string s="asdfghjkl";
    printf("%s\n",encrypt(s).c_str());
    return 0;
}


*/











































































































































































































































































