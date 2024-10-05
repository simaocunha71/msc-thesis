    return {0};
}

int main(){
    int n = 0;
    cin >> n;
    vector<int> res = even_odd_palindrome(n);
    for(int i=0;i<res.size();i++){
        printf("%d ", res[i]);
    }
    return 0;
}
