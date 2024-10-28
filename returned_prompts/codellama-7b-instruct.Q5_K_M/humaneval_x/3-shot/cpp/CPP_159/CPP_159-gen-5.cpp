    vector<int> answer;
    int after_eat;
    int left;
    if (remaining<need)
    {
        after_eat=number+remaining;
        left=0;
    }
    else
    {
        after_eat=number+need;
        left=remaining-need;
    }
    answer.push_back(after_eat);
    answer.push_back(left);
    return answer;
}


