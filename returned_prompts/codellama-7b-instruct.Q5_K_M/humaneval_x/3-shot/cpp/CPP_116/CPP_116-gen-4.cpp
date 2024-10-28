    vector<int> answer;
    int i;
    for (i=0;i<arr.size();i++)
    answer.push_back(arr[i]);
    sort(answer.begin(),answer.end(),[](int a,int b){
        if (a==b)
        return a<b;
        int a_ones=0,b_ones=0;
        while(a>0){
            if (a%2==1)
            a_ones++;
            a/=2;
        }
        while(b>0){
            if (b%2==1)
            b_ones++;
            b/=2;
        }
        if (a_ones==b_ones)
        return a<b;
        return a_ones<b_ones;
    });
    return answer;
}

