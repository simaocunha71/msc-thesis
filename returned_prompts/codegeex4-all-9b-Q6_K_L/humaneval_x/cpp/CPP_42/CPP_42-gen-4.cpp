    for(int i = 0; i < l.size(); i++){
        l[i] += 1;
    }
    return l;
}
int main(){
    vector<int> v = {1, 2, 3};
    vector<int> v2 = incr_list(v);
    for(int i = 0; i < v2.size(); i++){
        printf("%d ", v2[i]);
    }
    printf("\n");
    return 0;
}
