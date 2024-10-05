    vector<int> a(n);
    int i,j,k;
    int count = 0;
    for(i=1;i<=n;i++){
        a[i-1] = i*i - i + 1;
    }
    for(i=0;i<n;i++){
        for(j=i+1;j<n;j++){
            for(k=j+1;k<n;k++){
                if((a[i] + a[j] + a[k]) % 3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
}
int main()
{
    int n;
    n = 5;
    printf("%d\n", get_matrix_triples(n));
    return 0;
}

