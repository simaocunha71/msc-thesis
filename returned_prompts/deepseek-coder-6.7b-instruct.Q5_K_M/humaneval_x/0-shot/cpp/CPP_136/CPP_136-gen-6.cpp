    vector<int> ans(2);
    int max_neg = -1000000;
    int min_pos = 1000000;
    for(int i=0; i<lst.size(); i++){
        if(lst[i] < 0 && lst[i] > max_neg){
            max_neg = lst[i];
        }
        if(lst[i] > 0 && lst[i] < min_pos){
            min_pos = lst[i];
        }
    }
    if(max_neg == -1000000){
        ans[0] = 0;
    }
    else{
        ans[0] = max_neg;
    }
    if(min_pos == 1000000){
        ans[1] = 0;
    }
    else{
        ans[1] = min_pos;
    }
    return ans;
}

int main(){
    vector<int> vec = {2, 4, 1, 3, 5, 7};
    vector<int> res = largest_smallest_integers(vec);
    printf("{ %d , %d }",res[0],res[1]);
    return 0;
}

*/

