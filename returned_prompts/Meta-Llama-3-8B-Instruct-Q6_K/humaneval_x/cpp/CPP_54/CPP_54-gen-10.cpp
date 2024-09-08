    sort(s0.begin(), s0.end());
    sort(s1.begin(), s1.end());

    return s0 == s1;
}
int main()
{
    cout<<same_chars("eabcdzzzz", "dddzzzzzzzddeddabc")<<endl;
    cout<<same_chars("abcd", "dddddddabc")<<endl;
    cout<<same_chars("dddddddabc", "abcd")<<endl;
    cout<<same_chars("eabcd", "dddddddabc")<<endl;
    cout<<same_chars("abcd", "dddddddabce")<<endl;
    cout<<same_chars("eabcdzzzz", "dddzzzzzzzddddabc")<<endl;
    return 0;
}

