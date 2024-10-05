    int sum1 = 0;
    int sum2 = 0;
    for(auto &i : lst1)
        sum1 += i.size();
    for(auto &i : lst2)
        sum2 += i.size();
    if(sum1 < sum2)
        return lst1;
    else
        return lst2;
}



int main()
{
    vector<string> lst1 = {"hi", "admin"};
    vector<string> lst2 = {"hI", "Hi"};
    vector<string> res = total_match(lst1, lst2);
    for(auto &i : res)
        printf("%s ", i.c_str());
    return 0;
}



This program first calculates the total number of characters in the strings of lst1 and lst2 by summing up the sizes of the strings. Then it compares these sums and returns the vector with the smaller sum. If the sums are equal, it returns lst1.
*/

// 1:

/*
