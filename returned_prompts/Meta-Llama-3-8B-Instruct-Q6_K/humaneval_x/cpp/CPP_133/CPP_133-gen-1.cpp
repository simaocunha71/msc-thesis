    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        int x = ceil(lst[i]);
        sum += x * x;
    }
    return sum;
}

int main() {
    vector<float> lst = {1.4,4.2,0,-2.4,1,1};
    printf("%d\n",sum_squares(lst));
    return 0;
}

