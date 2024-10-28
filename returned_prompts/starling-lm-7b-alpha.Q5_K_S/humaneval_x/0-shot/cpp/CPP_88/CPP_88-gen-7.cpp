    int a = array.size();
    if(a==0){
        return array;
    }
    if(a==1){
        return array;
    }
    if(a==2){
        if((array[0]+array[1])%2==0){
            return {array[1],array[0]};
        }
        return {array[0],array[1]};
    }
    int b = a/2;
    vector<int> left = array.begin(),right = array.begin()+b;
    if((*left+*right)%2==0){
        std::merge(left,left+b,right,right+b,array.begin());
        return array;
    }
    std::merge(right,right+b,left,left+b,array.begin());
    std::reverse(array.begin(),array.end());
    return array;
}
int main(){
    vector<int> array = {2, 4, 3, 0, 1, 5, 6};
    vector<int> result = sort_array(array);
    for(auto i:result){
        printf("%d ",i);
    }
    return 0;
}



*/
























































































































































































































