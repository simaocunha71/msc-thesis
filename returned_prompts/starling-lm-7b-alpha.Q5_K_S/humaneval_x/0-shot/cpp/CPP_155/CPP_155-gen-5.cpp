    vector<int> even_nums;
    vector<int> odd_nums;
    int num_length = 0;
    while(num != 0){
        num_length++;
        num = num / 10;
    }

    int num_copy = num;
    for(int i = 0; i < num_length; i++){
        if(num_copy % 2 == 0){
            even_nums.push_back(num_copy);
        }else{
            odd_nums.push_back(num_copy);
        }
        num_copy = num_copy / 10;
    }
    return vector<int>{even_nums.size(), odd_nums.size()};
}

int main(){
    int input = -12;
    vector<int> result = even_odd_count(input);
    printf("{");
    for(int i = 0; i < result.size(); i++){
        printf("%d", result[i]);
        if(i != result.size()-1) printf(", ");
    }
    printf("}\n");
    return 0;
}







*/
































































































































































































































