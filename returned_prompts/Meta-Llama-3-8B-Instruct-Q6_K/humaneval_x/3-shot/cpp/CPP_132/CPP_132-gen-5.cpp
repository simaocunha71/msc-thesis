    int count_open=0,count_close=0;
    for (int i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        {
            count_open+=1;
        }
        if (str[i]==']')
        {
            count_close+=1;
        }
        if (count_open<count_close)
        {
            return false;
        }
        if (count_open>count_close)
        {
            return true;
        }
    }
    return false;
}  // This function is not working correctly, it is returning true for all inputs. The function should return true if there is a valid subsequence of brackets where at least one bracket in the subsequence is nested. Otherwise it should return false. For example, is_nested("[[]]") should return true because there is a valid subsequence of brackets where at least one bracket in the subsequence is nested. And is_nested("[]]]]]]][[[[[]") should return false because there is no valid subsequence of brackets where at least one bracket in the subsequence is nested. The function should return false for is_nested("[][]") and is_nested("[]"). The function should return true for is_nested("[[][]]") and is_nested("[[]][[").

