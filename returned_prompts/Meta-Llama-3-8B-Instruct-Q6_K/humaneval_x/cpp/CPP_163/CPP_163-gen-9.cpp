    vector<int> result;
    if(a>b)
        swap(a,b);
    for(int i=a; i<=b; i++){
        int temp=i;
        while(temp>0){
            int last_digit=temp%10;
            if(last_digit%2==0)
                result.push_back(last_digit);
            temp=temp/10;
        }
    }
    return result;
}

int main()
{
    printf("%d\n",generate_integers(2,8).size());
    //vector<int> result = generate_integers(2,8);
    //for(int i=0; i<result.size(); i++)
        //printf("%d ", result[i]);
    return 0;
}
