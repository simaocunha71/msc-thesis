    vector<int> result;
    if(a>b) swap(a,b);
    for(int i=a;i<=b;i++){
        int temp=i;
        int count=0;
        while(temp!=0){
            int digit=temp%10;
            if(digit%2==0) count++;
            temp=temp/10;
        }
        if(count>0) result.push_back(i);
    }
    return result;
}
int main()
{
    vector<int> res = generate_integers(2, 8);
    for(int i=0;i<res.size();i++)
    {
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}
