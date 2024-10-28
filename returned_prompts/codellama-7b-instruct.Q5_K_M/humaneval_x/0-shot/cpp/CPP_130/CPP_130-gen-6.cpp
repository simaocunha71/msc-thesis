}

int main(void){
    int n;
    scanf("%d", &n);
    vector<int> result = tri(n);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}