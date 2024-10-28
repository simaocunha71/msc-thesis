    int a = 0, b = 0, flag_a = 1, flag_b = 1;
    for (int i = 0; i < lst.size(); i++){
        if (lst[i] < 0 && lst[i] > a){
            a = lst[i];
            flag_a = 0;
        }
        if (lst[i] > 0 && lst[i] < b || flag_b){
            b = lst[i];
            flag_b = 0;
        }
    }
    if (flag_a) a = 0;
    if (flag_b) b = 0;
    return {a, b};
}

int main()
{
    vector<int> vec1 = {2, 4, 1, 3, 5, 7};
    vector<int> result1 = largest_smallest_integers(vec1);
    printf("%d %d\n", result1[0], result1[1]);

    vector<int> vec2 = {};
    vector<int> result2 = largest_smallest_integers(vec2);
    printf("%d %d\n", result2[0], result2[1]);

    vector<int> vec3 = {0};
    vector<int> result3 = largest_smallest_integers(vec3);
    printf("%d %d\n", result3[0], result3[1]);

    return 0;
}

*/

//Problem110/solution.cpp
/*
