    vector<int> a(n);
    int i, j, k;
    int triples = 0;

B:
    for(i = 1; i <= n; i++)
        a[i-1] = i * i - i + 1;

C:
    for(i = 0; i < n; i++)
        for(j = i+1; j < n; j++)
            for(k = j+1; k < n; k++)
                if((a[i] + a[j] + a[k]) % 3 == 0)
                    triples++;

    return triples;
}

int main(){
    int n;
    printf("Enter the value of n: