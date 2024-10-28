int main(){
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> ans;
    ans=common(l1, l2);
    for(int i=0;i<ans.size();i++)
    {
        printf("%d ", ans[i]);
    }
    printf("\n");
    return 0;
}
