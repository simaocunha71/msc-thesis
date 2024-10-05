    int i, j;
    for(i=1; i<=*max_element(lst.begin(),lst.end()); i++){
        int count = 0;
        for(j=0; j<lst.size(); j++){
            if(lst[j] == i){
                count++;
            }
        }
        if(count >= i){
            return i;
        }
    }
    return -1;
}
int main() {
    vector<int> lst = {4, 1, 2, 2, 3, 1};
    printf("%d", search(lst));
    return 0;
}
*/

// 