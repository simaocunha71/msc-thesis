    vector<int> a(n);
    int count = 0;
    for(int i=0; i<n; i++){
        a[i] = (i+1)*(i+1) - i;
    }
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            for(int k=j+1; k<n; k++){
                if((a[i] + a[j] + a[k])%3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Output: %d", get_matrix_triples(n));
    return 0;
}

