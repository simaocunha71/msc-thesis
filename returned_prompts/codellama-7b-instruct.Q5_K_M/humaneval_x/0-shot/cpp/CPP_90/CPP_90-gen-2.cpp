    if(lst.size() == 0)
        return -1;
    if(lst.size() == 1)
        return -1;
    if(lst.size() == 2)
        return lst[1];
    for(int i = 0; i < lst.size() - 1; i++)
    {
        for(int j = i + 1; j < lst.size(); j++)
        {
            if(lst[i] < lst[j])
            {
                return lst[j];
            }
        }
    }
}
int main(){
    vector<int> lst = {1, 2, 3, 4, 5};
    printf("%d\n", next_smallest(lst));
    lst = {5, 1, 4, 3, 2};
    printf("%d\n", next_smallest(lst));
    lst = {};
    printf("%d\n", next_smallest(lst));
    lst = {1, 1};
    printf("%d\n", next_smallest(lst));
    return 0;
}
