    return lst;
}
int main(){
    vector<int> lst = {1, 2, 3, 4};
    vector<int> lst_strange = strange_sort_list(lst);
    for(int i: lst_strange) printf("%d ", i);
    printf("\n");
    return 0;
}
