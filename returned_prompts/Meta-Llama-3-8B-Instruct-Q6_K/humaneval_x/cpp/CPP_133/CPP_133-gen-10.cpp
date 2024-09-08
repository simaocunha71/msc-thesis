    int sum=0;
    for(int i=0;i<lst.size();i++){
        float num = ceil(lst[i]);
        sum += pow(num,2);
    }
    return sum;
}

int main(){
    vector<float> lst = {1.4,4.2,0};
    printf("%d\n",sum_squares(lst));
    return 0;
}
