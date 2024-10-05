    int i;
    if (number<2)
    return false;
    for (i=2;i<=sqrt(number);i++)
    if (number%i==0)
    return false;
    return true;
}

int main(){
    vector<int> lst={0,8,1,2,1,7};
    printf("%d", sum_of_digits(skjkasdkd(lst)));
}



