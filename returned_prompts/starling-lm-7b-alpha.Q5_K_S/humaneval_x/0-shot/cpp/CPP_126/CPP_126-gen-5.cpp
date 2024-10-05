    for (int i=1; i<lst.size(); i++) {
        if (lst[i] < lst[i-1]) {
            return false;
        }
    }
    return true;
}


int main()
{
    vector<int> lst={1, 2, 3, 4, 5};
    if (is_sorted(lst)) {
        printf("true\n");
    } else {
        printf("false\n");
    }
    return 0;
}



```
