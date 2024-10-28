    long long int sum=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]>0 && floor(lst[i])==lst[i] && lst[i]%2==1){
            sum+=pow(lst[i],2);
        }
    }
    return sum;
}

int main() {
    vector<float> vec = {1, 3, 2, 0};
    printf("%lld", double_the_difference(vec));
    return 0;
}


