    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];
    if(start1 > end2 || start2 > end1) return "NO";
    int start = max(start1, start2);
    int end = min(end1, end2);
    if(start > end) return "NO";
    int len = end - start + 1;
    bool isPrime = true;
    if(len < 2) return "NO";
    for(int i=2; i*i<=len; i++){
        if(len%i == 0) isPrime = false;
    }
    return isPrime ? "YES" : "NO";
}
int main()
{
    printf("%s\n", intersection({1, 2}, {2, 3}).c_str());
    printf("%s\n", intersection({-1, 1}, {0, 4}).c_str());
    printf("%s\n", intersection({-3, -1}, {-5, 5}).c_str());
    return 0;
}
B:
int main()
{
    printf("%s\n", intersection({1, 3}, {2, 4}).c_str());
    printf("%s\n", intersection({-1, 1}, {0, 4}).c_str());
    printf("%s\n", intersection({-3, -1}, {-5, 5}).c_str());
    return 0;
}
C:
int main()
{
    printf("%s\n", intersection({1, 2}, {2, 3}).c_str());
    printf("%s\n", intersection({-1, 1}, {0, 4}).c_str());
    printf("%s\n", intersection({-3, -1}, {-5, 5}).c_str());
    return 0;
}
D:
int main()
{
    printf("%s\n", intersection({1, 3}, {2, 4}).c_str());
    printf("%s\n", intersection({-1, 1}, {0, 4}).c_str());
    printf("%s\n", intersection({-3, -1}, {-5, 5}).c_str());
    return 0;
}
E:
int main()
{
    printf("%s\n", intersection({1, 2}, {2, 3}).c_str());
    printf("%s\n