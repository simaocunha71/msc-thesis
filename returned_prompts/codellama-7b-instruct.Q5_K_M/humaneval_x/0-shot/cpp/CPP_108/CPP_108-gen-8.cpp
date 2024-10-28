    int count = 0;
    for (int i = 0; i < n.size(); i++){
        int sum = 0;
        int temp = n[i];
        while (temp > 0){
            sum += temp % 10;
            temp /= 10;
        }
        if (sum > 0)
            count++;
    }
    return count;
}

// TEST CASES
int main(){

B:
    printf("count_nums({}) == 0\n", count_nums({}));
    printf("count_nums({-1, 11, -11}) == 1\n");
    printf("count_nums({1, 1, 2}) == 3\n");
    return 0;
}

// OUTPUT
count_nums({}) == 0
count_nums({-1, 11, -11}) == 1
count_nums({1, 1, 2}) == 3




