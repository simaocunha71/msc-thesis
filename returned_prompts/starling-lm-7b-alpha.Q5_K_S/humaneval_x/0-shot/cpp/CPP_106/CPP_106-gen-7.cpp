    vector<int> result(n);
    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            result[i] = i;
            for (int j = 1; j <= i; j++)
            {
                result[i] *= j;
            }
        }
        else
        {
            result[i] = 0;
            for (int j = 1; j <= i; j++)
            {
                result[i] += j;
            }
        }
    }
    return result;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> result = f(n);
    for (int i = 0; i < n; i++)
    {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}





























































































































































































































































































