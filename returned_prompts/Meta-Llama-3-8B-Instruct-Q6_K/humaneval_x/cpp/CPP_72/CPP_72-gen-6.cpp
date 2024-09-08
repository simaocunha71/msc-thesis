    if(q.size()%2!=0){
        return false;
    }
    int sum=0;
    for(int i=0;i<q.size();i++){
        sum+=q[i];
    }
    if(sum>w){
        return false;
    }
    for(int i=0;i<q.size()/2;i++){
        if(q[i]!=q[q.size()-1-i]){
            return false;
        }
    }
    return true;
}

int main(){
    vector<int> q1={1,2};
    vector<int> q2={3,2,3};
    vector<int> q3={3,2,3};
    vector<int> q4={3};
    printf("%d\n",will_it_fly(q1,5));
    printf("%d\n",will_it_fly(q2,1));
    printf("%d\n",will_it_fly(q3,9));
    printf("%d\n",will_it_fly(q4,5));
    return 0;
}
