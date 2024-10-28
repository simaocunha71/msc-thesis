    int result = 0;
    for (int i = 1; i < lst.size(); i += 2)
        result += lst[i];
    return result;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    int result = add(lst);
    printf("%d", result);
    return 0;
}
