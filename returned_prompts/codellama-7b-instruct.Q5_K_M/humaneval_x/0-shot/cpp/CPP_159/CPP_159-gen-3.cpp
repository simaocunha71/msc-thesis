    if(number+remaining>=need){
        number+=remaining;
        remaining=0;
    }else{
        number+=number+remaining-need;
        remaining=need-number;
    }
    vector<int> res;
    res.push_back(number);
    res.push_back(remaining);
    return res;
}
int main(){
    printf("%d %d %d\n",eat(5,10,6)[0],eat(5,10,6)[1],eat(4,9,8)[0],eat(4,9,8)[1]);
    return 0;
}
