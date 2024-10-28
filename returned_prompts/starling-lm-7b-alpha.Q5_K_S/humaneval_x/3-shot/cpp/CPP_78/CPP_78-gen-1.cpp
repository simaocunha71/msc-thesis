    vector<string> primes={"2","3","5","7","B","D"};
    int count=0;
    int i,j;
    for (i=0;i<num.size();i++)
    {
        for (j=0;j<primes.size();j++)
        if (num[i]==primes[j])
        {
            count+=1;
            break;
        }
    }
    return count;
}

int main(){
    string num;
    cin>>num;
    cout<<hex_key(num)<<endl;
}



