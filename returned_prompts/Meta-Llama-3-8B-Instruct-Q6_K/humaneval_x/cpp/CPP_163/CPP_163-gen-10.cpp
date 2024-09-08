    vector<int> res;
    if(a>b) swap(a,b);
    for(int i=a;i<=b;i++){
        int temp=i;
        while(temp>0){
            int last_digit=temp%10;
            if(last_digit%2==0) res.push_back(last_digit);
            temp=temp/10;
        }
    }
    sort(res.begin(),res.end());
    return res;
}

int main()
{
    int a,b;
    printf("Enter the start and end range:\n");
    scanf("%d %d",&a,&b);
    vector<int> v=generate_integers(a,b);
    for(int i=0;i<v.size();i++)
        printf("%d ",v[i]);
    return 0;
}

