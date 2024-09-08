    if(n>m){
        return "-1";
    }
    int sum=0;
    for(int i=n;i<=m;i++){
        sum+=i;
    }
    double avg=(double)sum/(m-n+1);
    int r=round(avg);
    string s;
    while(r>0){
        s.push_back(r%2+'0');
        r=r/2;
    }
    reverse(s.begin(),s.end());
    return s;
}

int main(){
    printf("%s\n",rounded_avg(1,5).c_str());
    printf("%s\n",rounded_avg(7,5).c_str());
    printf("%s\n",rounded_avg(10,20).c_str());
    printf("%s\n",rounded_avg(20,33).c_str());
    return 0;
}

