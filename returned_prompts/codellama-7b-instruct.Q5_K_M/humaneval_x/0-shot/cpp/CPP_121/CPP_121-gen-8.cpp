
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (i % 2 == 0 && lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    return sum;
}

int main(){
    int t;
    vector<int> lst;
    scanf("%d",&t);
    while (t--) {
        int n,a;
        scanf("%d",&n);
        for (int i = 0; i < n; i++) {
            scanf("%d",&a);
            lst.push_back(a);
        }
        printf("%d\n",solutions(lst));
        lst.clear();
    }
    return 0;
}

