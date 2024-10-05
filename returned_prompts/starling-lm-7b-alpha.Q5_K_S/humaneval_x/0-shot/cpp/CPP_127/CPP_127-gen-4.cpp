    if( interval2[0] > interval1[1] ){
        swap(interval1[0],interval1[1]);
        swap(interval2[0],interval2[1]);
        goto A;
    }
    else if( interval2[0] >= interval1[1] ){
        return "NO";
    }
    else if( interval1[0] >= interval2[1] ){
        return "NO";
    }
    else if( interval2[1] >= interval1[1] ){
        return "YES";
    }
    int length = interval1[1] - interval2[0];
    for(int i=2;i<length;i++){
        if( length%i == 0 ){
            return "NO";
        }
    }
    return "YES";
}
int main(){
    vector<int> interval1;
    vector<int> interval2;
    while(scanf("%d %d",&interval1[0],&interval1[1])!=EOF){
        scanf("%d %d",&interval2[0],&interval2[1]);
        printf("%s\n",intersection(interval1,interval2).c_str());
    }
    return 0;
}

*/






















































































































































































































