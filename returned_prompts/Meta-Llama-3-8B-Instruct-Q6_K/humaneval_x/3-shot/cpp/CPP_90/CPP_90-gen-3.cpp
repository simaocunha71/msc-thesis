    if(lst.size()<2)
        return -1;
    sort(lst.begin(), lst.end());
    if(lst[0]==lst[1])
        return -1;
    return lst[1];
}
//Note: The problem statement doesn't specify the type of the return value, so I'm returning -1 for "None" and the 2nd smallest element for successful cases. If the problem statement specifies that the return type should be an integer or None (or some other type), you may need to adjust this code. Also, the problem statement doesn't specify whether the input vector should be modified, so I've chosen not to modify it. If the problem statement requires the input vector to be modified, you may need to adjust this code.