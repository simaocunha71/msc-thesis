    vector<int> result;
    set_intersection(l1.begin(), l1.end(), l2.begin(), l2.end(),
                     back_inserter(result));
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    return result;
}

int main()
{
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> result = common(l1,l2);
    for(auto i:result)
        printf("%d ",i);
    printf("\n");
    return 0;
}

