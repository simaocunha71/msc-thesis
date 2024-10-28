    int sum=0;
    int product=1;
    for (int i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    vector<int> final_answer;
    final_answer.push_back(sum);
    final_answer.push_back(product);
    return final_answer;
}


