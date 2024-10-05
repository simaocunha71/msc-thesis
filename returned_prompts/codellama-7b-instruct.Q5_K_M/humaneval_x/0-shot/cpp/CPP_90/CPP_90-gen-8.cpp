    int n = lst.size();
    if(n == 0){
        return -1;
    }
    if(n == 1){
        return -1;
    }
    if(n == 2){
        if(lst[0] > lst[1]){
            return lst[1];
        }
        else{
            return -1;
        }
    }
    //sort(lst.begin(),lst.end());
    sort(lst.begin(),lst.end());
    if(lst[1] == lst[n-1]){
        goto A;
    }
    return lst[1];
}


int main(){
    vector<int> lst = {5, 1, 4, 3, 2};
    printf("%d\n",next_smallest(lst));
    return 0;
}

