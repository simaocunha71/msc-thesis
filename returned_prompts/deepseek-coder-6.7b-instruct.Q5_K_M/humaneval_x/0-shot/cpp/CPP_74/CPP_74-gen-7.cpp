    int sum1 = 0;
    int sum2 = 0;
    for(int i=0; i<lst1.size(); i++)
        sum1 += lst1[i].size();
    for(int i=0; i<lst2.size(); i++)
        sum2 += lst2[i].size();
    if(sum1 < sum2)
        return lst1;
    else if(sum2 < sum1)
        return lst2;
    else
        return lst1;
}

int main()
{
    vector<string> lst1 = {"hI", "Hi"};
    vector<string> lst2 = {"hi", "hi", "admin", "project"};
    vector<string> res = total_match(lst1, lst2);
    for(int i=0; i<res.size(); i++)
        printf("%s ", res[i].c_str());
    return 0;
}

*/

// ANSWER:
// The code provided above is a solution to the problem. It first calculates the total number of