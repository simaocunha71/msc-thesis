    int result = 0;
    for(int i = 0; i < lst.size(); i++)
    {
        if(i % 2 == 0 && lst[i] % 2 != 0)
        {
            result += lst[i];
        }
    }
    return result;
}

int main()
{
    vector<int> test_case = {3, 3, 3, 3, 3};
    printf("%d\n", solutions(test_case));
    return 0;
}

