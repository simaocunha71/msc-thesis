
int sum = 0;
    for (int i = 0; i < lst.size(); i++)
    {
        if(i % 3 == 0)
        {
            lst[i] *= lst[i];
        }
        else if(i % 4 == 0 && i % 3 != 0)
        {
            lst[i] *= lst[i] * lst[i];
        }
        sum += lst[i];
    }
    return sum;
}

int main(){
    vector<int> lst = {1,2,3};
    int sum = sum_squares(lst);
    cout << sum << endl;
    return 0;
}

