    bool balanced=true;
    int sum=0;
    for(int i=0;i<q.size();i++){
        sum+=q[i];
        if(q[i]!=q[q.size()-1-i]){
            balanced=false;
            break;
        }
    }
    if(sum>w||!balanced){
        return false;
    }
    return true;
}int main(){
    vector<int> q1={1,2};
    vector<int> q2={3,2,3};
    vector<int> q3={3};
    printf("%d\n",will_it_fly(q1,5));
    printf("%d\n",will_it_fly(q2,1));
    printf("%d\n",will_it_fly(q2,9));
    printf("%d\n",will_it_fly(q3,5));
    return 0;
}