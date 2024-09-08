    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];

    if(start1 > end2 || start2 > end1)
        return "NO";
    int start = max(start1, start2);
    int end = min(end1, end2);
    if(start > end)
        return "NO";
    int length = end - start + 1;
    int i = 2;
    while(i * i <= length)
        if(length % i == 0)
            return "NO";
        i++;
    return "YES";
}
int main()
{
    vector<int> interval1 = {1,3};
    vector<int> interval2 = {2,4};
    printf("%s\n", intersection(interval1,interval2).c_str());
    return 0;
}
