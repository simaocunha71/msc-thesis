    int sum=0;
    int n=q.size();
    for(int i=0;i<n;i++){
        sum+=q[i];
    }
    if(sum>w){
        return false;
    }
    int i=0,j=n-1;
    while(i<j){
        if(q[i]==q[j]){
            i++;
            j--;
        }
        else{
            return false;
        }
    }
    return true;
}

int main(){
    vector<int> v1 = {1,2};
    vector<int> v2 = {3,2,3};
    vector<int> v3 = {3};
    printf("%d\n",will_it_fly(v1,5)); // 0
    printf("%d\n",will_it_fly(v2,1)); // 0
    printf("%d\n",will_it_fly(v2,9)); // 1
    printf("%d\n",will_it_fly(v3,5)); // 1
    return 0;
}