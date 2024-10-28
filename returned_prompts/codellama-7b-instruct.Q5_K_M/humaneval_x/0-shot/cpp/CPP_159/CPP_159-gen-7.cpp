    if(number == need)
        return vector<int> {number,remaining - number};
    else if(number > need)
        return vector<int> {need,remaining - need};
    else{
        number += remaining;
        goto A;
    }
}

int main(){
    vector<int> result = eat(5, 6, 10);
    printf("%d %d\n",result[0],result[1]);
    return 0;
}
