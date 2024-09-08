    bool flag=true;
    for(int i=0;i<l.size()-1;i++){
        if(l[i+1]>=l[i]){
            if(l[i+1]>l[i]){
                flag=false;
            }
        }
        else{
            flag=false;
        }
    }
    return flag;
}

int main(){
    vector<float> v = {1, 2, 4, 20};
    printf("%d\n", monotonic(v));
    return 0;
}

