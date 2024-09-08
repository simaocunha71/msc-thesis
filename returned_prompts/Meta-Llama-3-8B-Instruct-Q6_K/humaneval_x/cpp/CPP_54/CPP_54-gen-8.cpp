    // sort the strings
    sort(s0.begin(), s0.end());
    sort(s1.begin(), s1.end());

    // check if the sorted strings are equal
    return s0 == s1;
}

int main()
{
    cout<<same_chars("eabcdzzzz", "dddzzzzzzzddeddabc");
    return 0;
}

