/*
Your runtime beats 100 % of cpp submissions.

Your memory usage beats 100 % of cpp submissions.

*/
    string ans = "";
    for(int i = word.size() - 1; i >= 0; i--)
    {
        if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u')
        {
            ans = word[i];
            break;
        }
    }
    return ans;
}
