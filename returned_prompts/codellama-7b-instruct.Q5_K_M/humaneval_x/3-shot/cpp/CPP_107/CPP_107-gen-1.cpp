    vector<int> answer;
    int even=0;
    int odd=0;
    for (int i=1;i<n;i++){
        string s=to_string(i);
        string rev=string(s.rbegin(),s.rend());
        if (s==rev){
            if (i%2==0)
                even+=1;
            else
                odd+=1;
        }
    }
    answer.push_back(even);
    answer.push_back(odd);
    return answer;
}


