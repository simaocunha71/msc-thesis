    vector<int> result;
    if(a>b) swap(a,b);
    for(int i=a;i<=b;i++){
        string s=to_string(i);
        bool is_even=true;
        for(int j=0;j<s.length();j++){
            if(s[j]%2!=0){
                is_even=false;
                break;
            }
        }
        if(is_even) result.push_back(i);
    }
    return result;
}

int main()
{
    vector<int> result = generate_integers(10,14);
    for(int i = 0; i < result.size(); i++)
    {
        cout<<result[i]<<" ";
    }
    return 0;
}

