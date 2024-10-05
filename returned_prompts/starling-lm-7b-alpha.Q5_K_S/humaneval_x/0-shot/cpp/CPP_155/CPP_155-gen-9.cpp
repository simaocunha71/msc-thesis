    vector<int> result;
    if(num<0){
        result.push_back(0);
        result.push_back(1);
        return result;
    }
    if(num==0){
        result.push_back(0);
        result.push_back(0);
        return result;
    }
    int even_count=0,odd_count=0;
    while(num!=0){
        if(num%2==0){
            even_count++;
        }else{
            odd_count++;
        }
        num/=10;
    }
    result.push_back(odd_count);
    result.push_back(even_count);
    return result;
}
int main(int argc, char *argv[]) {
    // insert code here...
    printf("even: %d\nodd: %d\n",even_odd_count(123).at(0),even_odd_count(123).at(1));
    return 0;
}









































































































































































































































































