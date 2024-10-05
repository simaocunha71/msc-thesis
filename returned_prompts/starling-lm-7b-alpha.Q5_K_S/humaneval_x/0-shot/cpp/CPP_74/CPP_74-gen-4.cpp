    if(lst1.size() < lst2.size())
    {
        return lst1;
    }
    else if(lst1.size() > lst2.size())
    {
        return lst2;
    }
    else
    {
        int sum = 0;
        for(int i=0;i<lst1.size();i++)
        {
            sum += lst1[i].size();
        }
        int sum1 = 0;
        for(int i=0;i<lst2.size();i++)
        {
            sum1 += lst2[i].size();
        }
        if(sum < sum1)
        {
            return lst1;
        }
        else if(sum > sum1)
        {
            return lst2;
        }
        else
        {
            return lst1;
        }
    }
}

int main(void)
{
    vector<string> lst1;
    vector<string> lst2;
    lst1.push_back("4");
    lst2.push_back("1");
    lst2.push_back("2");
    lst2.push_back("3");
    lst2.push_back("4");
    lst2.push_back("5");
    printf("%s\n",total_match(lst1,lst2).data());
    return 0;
}


































































































































































