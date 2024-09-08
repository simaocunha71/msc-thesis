    vector<int> result;
    sort(l1.begin(),l1.end());
    sort(l2.begin(),l2.end());
    vector<int>::iterator it1 = l1.begin();
    vector<int>::iterator it2 = l2.begin();
    while(it1 != l1.end() && it2 != l2.end())
    {
        if(*it1 == *it2)
        {
            result.push_back(*it1);
            it1++;
            it2++;
        }
        else if(*it1 < *it2)
        {
            it1++;
        }
        else
        {
            it2++;
        }
    }
    return result;
}

int main()
{
    vector<int> v1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> v2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> common_elements = common(v1,v2);
    for(int i = 0; i < common_elements.size(); i++)
    {
        printf("%d ", common_elements[i]);
    }
    printf("\n");
    return 0;
}
B:
    vector<int> common(vector<int> l1,vector<int> l2){
        vector<int> result;
        set<int> s1(l1.begin(),l1.end());
        set<int> s2(l2.begin(),l2.end());
        set<int>::iterator it1 = s1.begin();
        set<int>::iterator it2 = s2.begin();
        while(it1 != s1.end() && it2 != s2.end())
        {
            if(*it1 == *it2)
            {
                result.push_back(*it1);
                it1++;
                it2++;
            }
            else if(*it1 < *it2)
            {
                it1++;
            }
            else
            {
                it2++;
            }
        }
        return result;
    }

int main()
{
    vector<int> v1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> v2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> common_elements = common(v1,v2);
    for(int i = 0; i < common_elements.size(); i++)
    {
        printf("%d ", common_elements[i]);
