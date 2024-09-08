    int total = number + need;
    int left = remaining - (need - (need - number));
    vector<int> result;
    result.push_back(total);
    result.push_back(left);
    return result;
}

int main()
{
    vector<int> res = eat(5,6,10);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}  //Output: 11 4

