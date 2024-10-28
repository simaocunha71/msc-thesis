    vector<int> a;
    for(int i=1;i<=n;i++){
        int val = i*i-i+1;
        a.push_back(val);
    }
    int count = 0;
    for(int i=0;i<a.size();i++){
        for(int j=i+1;j<a.size();j++){
            for(int k=j+1;k<a.size();k++){
                if(a[i]+a[j]+a[k]%3 == 0){
                    count++;
                }
            }
        }
    }
    return count;
}
int main(){
    int n;
    scanf("%d",&n);
    int result = get_matrix_triples(n);
    printf("%d",result);
    return 0;
}
