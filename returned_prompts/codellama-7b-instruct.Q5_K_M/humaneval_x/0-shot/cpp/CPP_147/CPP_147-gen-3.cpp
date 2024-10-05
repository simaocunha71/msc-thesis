    vector<int> a(n);
    for (int i = 0; i < n; i++)
    {
        a[i] = i * i - i + 1;
    }
    int ans = 0;
    for (int i = 0; i < n - 2; i++)
    {
        for (int j = i + 1; j < n - 1; j++)
        {
            for (int k = j + 1; k < n; k++)
            {
                if ((a[i] + a[j] + a[k]) % 3 == 0)
                {
                    ans++;
                }
            }
        }
    }
    return ans;
}
int main() {
    int n;
    scanf("%d", &n);
    int ans = get_matrix_triples(n);
    printf("%d\n", ans);
    return 0;
}
