    return false;
}

int main(){
    vector<int> arr;
    arr.push_back(3);
    arr.push_back(4);
    arr.push_back(5);
    arr.push_back(1);
    arr.push_back(2);
    bool result = move_one_ball(arr);
    printf("%d", result);
    return 0;
}
