    int sum = 0;
    int max = 0;
    for (int i=0; i<lst.size(); i++){
        if (lst[i] > max){
            max = lst[i];
        }
    }

    string maxstr = to_string(max);
    for (int i=0; i<maxstr.size(); i++){
        sum += maxstr[i] - '0';
    }
    return sum;
}
int main(){
    vector<int> lst = {0,81,12,3,1,21};
    int result = skjkasdkd(lst);
    printf("%d", result);
    return 0;
}

