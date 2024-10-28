    int result = 0;
    for(int i = 0; i < lst.size(); i++)
    {
        int x = ceil(lst[i]);
        result += (x * x);
    }
    return result;
}

int main()
{
    vector<float> lst = {1.4,4.2,0};
    printf("%d", sum_squares(lst));
    return 0;
}

