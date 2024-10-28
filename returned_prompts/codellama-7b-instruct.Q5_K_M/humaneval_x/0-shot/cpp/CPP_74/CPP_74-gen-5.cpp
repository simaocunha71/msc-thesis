    if (lst1.size() <= lst2.size())
    {
        return lst1;
    }
    else if (lst1.size() > lst2.size())
    {
        return lst2;
    }
    else
    {
        goto A;
    }
}


int main()
{
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"hI", "Hi"};
    vector<string> v3 = {"hi", "hi", "admin", "project"};
    vector<string> v4 = {"hi", "admin"};
    vector<string> v5 = {"hI", "hi", "hi"};
    vector<string> v6 = {"4"};
    vector<string> v7 = {"1", "2", "3", "4", "5"};

    printf("%s", total_match(v1,v2).front().c_str());
    printf("%s", total_match(v3,v4).front().c_str());
    printf("%s", total_match(v4,v5).front().c_str());
    printf("%s", total_match(v6,v7).front().c_str());

    return 0;
}
