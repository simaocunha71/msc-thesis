    if (number>remaining){
        number=remaining;
    }
    if (number+number>=need){
        number=need-number;
    }
    if (number<0){
        number=0;
    }
    return vector<int> {number, remaining-number};
}
int main(){
    int number=5, need=10, remaining=6;
    vector<int> result=eat(number, need, remaining);
    printf("%d", result[0]);
    return 0;
}