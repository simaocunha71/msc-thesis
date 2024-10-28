    long long int sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]%2!=0 && lst[i]>0){
            sum+=pow(lst[i],2);
        }
    }
    return sum;
}








int main(){
    vector<float> lst;
    lst.push_back(1);
    lst.push_back(3);
    lst.push_back(2);
    lst.push_back(0);
    printf("%f\n",double_the_difference(lst));
    return 0;
}




```
