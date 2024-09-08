    int max=0;
    for(int i=1; i<=lst.size(); i++){
        int count=0;
        for(int j=0; j<lst.size(); j++){
            if(lst[j]==i){
                count++;
            }
        }
        if(count>=i && i>max){
            max=i;
        }
    }
    return max>0?max:-1;
}

int main(){
    printf("%d\n", search({4, 1, 2, 2, 3, 1}));
    printf("%d\n", search({1, 2, 2, 3, 3, 3, 4, 4, 4}));
    printf("%d\n", search({5, 5, 4, 4, 4}));
    return 0;
}
