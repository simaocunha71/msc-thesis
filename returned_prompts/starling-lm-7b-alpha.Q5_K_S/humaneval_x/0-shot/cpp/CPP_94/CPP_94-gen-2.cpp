    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] != 0){
            sum += lst[i];
        }
    }
    if(sum == 0){
        return 0;
    }
    while(sum > 0){
        if(sum < 10){
            return sum;
        }
        else{
            int tmp = sum;
            int dig = 0;
            while(tmp != 0){
                dig += tmp % 10;
                tmp /= 10;
            }
            sum = dig;
        }
    }
}

int main(){
    vector<int> lst;
    int a;
    while(scanf("%d", &a) != EOF){
        lst.push_back(a);
    }
    int sum = skjk