    vector<int> result;
    int temp = n;
    while(temp > 0) {
        if(temp % 2 == 0) {
            result.push_back(temp);
            temp = temp - 1;
        } else {
            result.push_back(temp);
            temp = temp - 2;
        }
    }
    return result;
}

int main() {
    int n;
    printf("Enter the number of levels: ");
    scanf("%d", &n);
    vector<int> res = make_a_pile(n);
    for(int i = 0; i < res.size(); i++) {
        printf("%d ", res[i]);
    }
    return 0;
}

