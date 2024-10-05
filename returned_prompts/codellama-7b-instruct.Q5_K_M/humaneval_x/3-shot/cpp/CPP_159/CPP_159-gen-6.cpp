    int i=0, j=0;
    int total=0, left=0;
    vector<int> answer;

    total=number+remaining;
    left=total-need;

    answer.push_back(total);
    answer.push_back(left);

    return answer;
}




