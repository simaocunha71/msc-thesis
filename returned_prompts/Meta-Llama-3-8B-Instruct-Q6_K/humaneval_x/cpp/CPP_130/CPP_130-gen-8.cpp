    vector<int> result;
    if(n == 0) {
        return result;
    }
    result.push_back(3);
    if(n == 1) {
        return result;
    }
    result.push_back(1 + (2 / 2));
    for(int i = 3; i <= n; i++) {
        if(i % 2 == 0) {
            result.push_back(1 + i / 2);
        } else {
            result.push_back(result[i-1] + result[i-2] + result[i]);
        }
    }
    return result;

}
int main() {
    printf("%lu", tri(3).size());
    for(int i = 0; i < tri(3).size(); i++) {
        printf("%d ", tri(3)[i]);
    }
    return 0;
}

