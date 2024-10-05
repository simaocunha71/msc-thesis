    int i;
    for (i=0;i<arr.size();i++)
    if (i>0 && arr[i]<arr[i-1]) return false;
    return true;
}


