    int size = lst.size();

    if(size < 2)
        return NULL;

    sort(lst.begin(), lst.end());

    for(int i = 1; i < size; i++)
        if(lst[i] != lst[0])
            return lst[i];

    return NULL;
}

*/

