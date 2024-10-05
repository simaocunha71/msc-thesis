int sum_squares(vector<int> lst){
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if ((i % 3 == 0) && (i % 4 == 0)) {
            sum += lst[i] * lst[i] * lst[i];
        } else if (i % 3 == 0) {
            sum += lst[i] * lst[i] * lst[i];
        } else if (i % 4 == 0) {
            sum += lst[i] * lst[i] * lst[i];
        } else {
            sum += lst[i];
        }
    }
    return sum;
}

int main() {
    vector<int> lst = {-1,-5,2,-1,-5};
    int result = sum_squares(lst);
    return 0;
}
