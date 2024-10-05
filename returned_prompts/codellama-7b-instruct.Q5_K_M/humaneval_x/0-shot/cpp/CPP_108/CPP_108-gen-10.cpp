    int num_digits = n.size();
    int sum_digits = 0;
    for(int i = 0; i < num_digits; i++){
        sum_digits += abs(n[i]);
    }
    return sum_digits > 0;
}
int main(int argc, char const *argv[])
{
    vector<int> a = {-1, 11, -11};
    vector<int> b = {1, 1, 2};
    vector<int> c = {};
    int x = count_nums(a);
    int y = count_nums(b);
    int z = count_nums(c);
    if(x == 1 && y == 3 && z == 0){
        printf("Correct");
    }else{
        printf("Wrong");
    }
    return 0;
}
