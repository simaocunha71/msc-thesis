    int i, j, flag;
    int prime, sum = 0;
    for(i = 0; i < lst.size(); i++){
        if(lst[i]>1){
            flag = 0;
            for(j = 2; j <= lst[i]/2; ++j){
                if(lst[i] % j == 0){
                    flag = 1;
                    break;
                }
            }
            if(flag == 0){
                prime = lst[i];
            }
        }
    }
    while(prime > 0){
        sum += prime % 10;
        prime /= 10;
    }
    return sum;
}

int main() {
    vector<int> lst;
    lst.push_back(0);
    lst.push_back(3);
    lst.push_back(2);
    lst.push_back(1);
    lst.push_back(3);
    lst.push_back(5);
    lst.push_back(7);
    lst.push_back(4);
    lst.push_back(5);
    lst.push_back(5);
    lst.push_back(5);
    lst.push_back(2);
    lst.push_back(181);
    lst.push_back(32);
    lst.push_back(4);
    lst.push_back(32);
    lst.push_back(3);
    lst.push_back(2);
    lst.push_back(32);
    lst.push_back(324);
    lst.push_back(4);
    lst.push_back(3);

    printf("%d", skjkasdkd(lst));

    return 0;
}

//