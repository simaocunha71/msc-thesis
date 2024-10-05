    int sum = 0;
    for(int i = 0; i < q.size(); i++)
        sum += q[i];

    if(sum > w)
        return false;

    int start = 0, end = q.size()-1;
    while(start < end){
        if(q[start] != q[end])
            return false;
        start++;
        end--;
    }
    return true;
}

int main()
{
    vector<int> q;
    int w;
    q = {1, 2}; w = 5;
    printf("%d\n", will_it_fly(q,w));
    q = {3, 2, 3}; w = 1;
    printf("%d\n", will_it_fly(q,w));
    q = {3, 2, 3}; w = 9;
    printf("%d\n", will_it_fly(q,w));
    q = {3}; w = 5;
    printf("%d\n", will_it_fly(q,w));
    return 0;
}


```















































































































































































































































