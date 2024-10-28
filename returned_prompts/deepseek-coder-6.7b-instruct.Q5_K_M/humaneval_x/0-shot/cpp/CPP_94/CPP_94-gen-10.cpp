    int ans = 0, max = -1;
    vector<bool> prime(100000, true);
    prime[0] = prime[1] = false;
    for (int p = 2; p * p <= 100000; p++) {
        if (prime[p] == true) {
            for (int i = p * p; i <= 100000; i += p)
                prime[i] = false;
        }
    }
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] > max && prime[lst[i]]){
            max = lst[i];
        }
    }
    while (max != 0) {
        ans += max % 10;
        max /= 10;
    }
    return ans;
}
int main(){
    vector<int> lst = {0,81,12,3,1,21};
    printf("%d\n",skjkasdkd(lst));
    return 0;
}

*/

//11.cpp
/*
