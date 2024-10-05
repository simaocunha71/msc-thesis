    vector<int> pile(n+1);
    for(int i=1;i<=n;i++){
        if(i%2==0)pile[i]=i+1;
        else pile[i]=i;
    }
    return pile;
}




/*
    Given a sequence of characters, find the longest subsequence such that all the
    characters in the subsequence are distinct.
    For example, the longest subsequence of the string "abcabcbb" is "abc", with length 3.
    Note that the subsequence does not have to be contiguous in the string.
    Return the length of the longest distinct subsequence found.

Examples:
>>> longest_distinct_subsequence("abcabcbb")
3
>>> longest_distinct_subsequence("bbbbb")
1
>>> longest_distinct_subsequence("abcabcabc")
4
>>> longest_distinct_subsequence("abcdefghijklmnop")
10

>>> longest_distinct_subsequence("abac")
3
>>> longest_distinct_subsequence("axcba")
2
>>> longest_distinct_subsequence("abcaxcb")
3

>>> longest_