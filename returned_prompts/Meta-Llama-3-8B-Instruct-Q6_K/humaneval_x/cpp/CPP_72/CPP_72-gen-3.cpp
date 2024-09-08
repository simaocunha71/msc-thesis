    // Check if the vector is balanced
    string s;
    for(int i=0;i<q.size();i++){
        s+=to_string(q[i]);
    }
    if(s!=s.substr(0,s.size()/2)+s.substr(s.size()/2)){
        return false;
    }

    // Check if the sum of the vector is less than or equal to the maximum possible weight
    int sum=0;
    for(int i=0;i<q.size();i++){
        sum+=q[i];
    }
    if(sum> w){
        return false;
    }

    return true;
}

int main(){
    vector<int> q={3,2,3};
    int w=9;
    printf("%d\n", will_it_fly(q,w));
    return 0;
}

