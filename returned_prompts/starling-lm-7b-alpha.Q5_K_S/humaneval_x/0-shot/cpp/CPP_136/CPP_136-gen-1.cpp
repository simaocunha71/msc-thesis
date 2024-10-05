    int min = 0;
    int max = 0;
    for (int i = 0; i < lst.size(); i++)
    {
        if (lst[i] < 0 && lst[i] < min)
        {
            min = lst[i];
        }
        if (lst[i] > 0 && lst[i] > max)
        {
            max = lst[i];
        }
    }
    vector<int> lst2;
    lst2.push_back(min);
    lst2.push_back(max);
    return lst2;
}
int main()
{
    vector<int> lst;
    lst.push_back(2);
    lst.push_back(4);
    lst.push_back(1);
    lst.push_back(3);
    lst.push_back(5);
    lst.push_back(7);
    vector<int> lst2 = largest_smallest_integers(lst);
    printf("%d %d", lst2[0], lst2[1]);
    return 0;
}

*/


































































































































































































































