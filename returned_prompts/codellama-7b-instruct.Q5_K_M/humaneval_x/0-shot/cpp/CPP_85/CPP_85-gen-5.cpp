    int ans = 0;
    for(int i = 0; i < lst.size(); i++) {
        if(i % 2 == 0)
            ans += lst[i];
    }
    return ans;
}

int main() {
    vector<int> lst = {4, 2, 6, 7};
    printf("ans: %d\n", add(lst));
    return 0;
}

