    bool balanced=true;
    int sum=0;
    for(int i=0;i<q.size();i++){
        sum+=q[i];
        if(q[i]!=q[q.size()-i-1]){
            balanced=false;
            break;
        }
    }
    if(sum<=w && balanced){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    vector<int> q={3,2,3};
    int w=9;
    printf("%d\n",will_it_fly(q,w));
    return 0;
}🚀
