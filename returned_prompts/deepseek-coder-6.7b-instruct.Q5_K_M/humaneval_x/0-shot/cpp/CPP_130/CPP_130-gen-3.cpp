    vector<int> res(n+1);
    if (n>=0)
        res[0] = 3;
    if (n>=1)
        res[1] = 2;
    if (n>=2)
        res[2] = 8;
    for (int i = 3; i <= n; i++) {
        if (i%2==0) 
            res[i] = 1 + i/2;
        else
            res[i] = res[i-1] + res[i-2] + res[i-1];
    }
    return res;
}

int main()
{
    int n;