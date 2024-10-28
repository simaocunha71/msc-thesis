    if(arr.size()==0)
        return true;
    int a=arr[0];
    for(int i=1;i<arr.size();i++){
        if(arr[i]<a){
            a=arr[i];
            goto A;
        }
    }
    return true;
}
int main(){
    vector<int>v1={3, 4, 5, 1, 2};
    vector<int>v2={3, 5, 4, 1, 2};
    if(move_one_ball(v1))
        printf("Yes, it's possible to sort the vector in non-decreasing order by performing right shift operation\n");
    else
        printf("No, it's not possible to sort the vector in non-decreasing order by performing right shift operation\n");
    if(move_one_ball(v2))
        printf("Yes, it's possible to sort the vector in non-decreasing order by performing right shift operation\n");
    else
        printf("No, it's not possible to sort the vector in non-decreasing order by performing right shift operation\n");
    return 0;
}
