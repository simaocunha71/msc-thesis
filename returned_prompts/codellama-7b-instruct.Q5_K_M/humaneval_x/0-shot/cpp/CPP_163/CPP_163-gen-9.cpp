    vector<int> v;
    for(int i=a;i<=b;i++){
        if(i%2==0){
            v.push_back(i);
        }
    }
    return v;
}

int main(){
    int a,b;
    scanf("%d%d",&a,&b);
    vector<int> v=generate_integers(a,b);
    for(int i=0;i<v.size();i++){
        printf("%d ",v[i]);
    }
    return 0;
}

