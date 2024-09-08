    vector<int> a(n);
    for(int i = 1; i <= n; i++){
        a[i-1] = i * i - i + 1;
    }

    int res = 0;
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            for(int k = j + 1; k < n; k++){
                if((a[i] + a[j] + a[k]) % 3 == 0){
                    res++;
                }
            }
        }
    }
    return res;
}

int main(int argc, char const *argv[])
{
    int n = 5;
    int res = get_matrix_triples(n);
    printf("The number of triples is: %d\n", res);
    return 0;
}

