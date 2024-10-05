    int sum1 = 0, sum2 = 0;
    for(auto &i : lst1)
        sum1 += i.size();
    for(auto &i : lst2)
        sum2 += i.size();
    return sum1 < sum2 ? lst1 : lst2;
}

int main()
{
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"hI", "Hi"};
    vector<string> res = total_match(v1, v2);
    for(auto &i : res)
        printf("%s ", i.c_str());
    return 0;
}

