
    vector<int> result;
    for(int i=0;i<arr.size();i++){
        result.push_back(arr[i]);
    }
    sort(result.begin(),result.end(),compare);
    return result;
}
bool compare(int a,int b){
    int counta=0;
    int countb=0;
    while(a!=0){
        counta++;
        a/=10;
    }
    while(b!=0){
        countb++;
        b/=10;
    }
    if(counta>countb){
        return true;
    }else if(counta<countb){
        return false;
    }else{
        return a<b;
    }
}
int main(){
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    sort_array(v);
}
