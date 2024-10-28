    int sum = 0;
    int len = lst.size();
    for(int i = 0; i < len; i++){
        if(i % 3 == 0){
            lst[i] = lst[i] * lst[i] * lst[i];
        }
        if(i % 4 == 0 && i % 3 != 0){
            lst[i] = lst[i] * lst[i] * lst[i];
        }
        sum += lst[i];
    }
    return sum;
}

int main() {
    int num;
    vector<int> v;
    printf("Enter the number of integers\n");
    scanf("%d",&num);
    int i;
    for(i = 0; i < num; i++){
        int x;
        scanf("%d",&x);
        v.push_back(x);
    }
    int sum = sum_squares(v);
    printf("The sum is %d\n",sum);
    return 0;
}

