    if(need == 0){
        return {number,remaining};
    }
    if(number == 0){
        return {0,0};
    }
    if(remaining == 0){
        remaining = 0;
        goto A;
    }

    if(remaining >= need){
        remaining -= need;
        number += need;
        goto A;
    }
    remaining = 0;
    number += remaining;
    goto A;
}
int main(){
    int number = 0,need = 0,remaining = 0;
    vector<int> ans;
    ans = eat(number,need,remaining);
    printf("%d %d\n",ans[0],ans[1]);
    return 0;
}