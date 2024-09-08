    bool is_balanced=false;
    int sum=0;
    for(int i=0;i<q.size();i++){
        sum+=q[i];
        if(q[i]!=q[q.size()-i-1]){
            is_balanced=false;
            break;
        }
        is_balanced=true;
    }
    if(is_balanced && sum<=w){
        return true;
    }
    return false;
}

int main(){
    vector<int> q1={1,2};
    vector<int> q2={3,2,3};
    vector<int> q3={3};
    printf("%d\n",will_it_fly(q1,5)); // prints 0
    printf("%d\n",will_it_fly(q2,1)); // prints 0
    printf("%d\n",will_it_fly(q2,9)); // prints 1
    printf("%d\n",will_it_fly(q3,5)); // prints 1
    return 0;
}
