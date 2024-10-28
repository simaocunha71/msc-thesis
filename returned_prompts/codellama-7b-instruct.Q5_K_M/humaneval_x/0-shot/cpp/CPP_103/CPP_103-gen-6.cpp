/*
This function is mainly about the calculation of the average of the integers from n to m.
First, the average is calculated by (m+n)/2.
Then, the average is rounded up to the nearest integer.
Finally, the integer is converted to binary.
*/
    int count;
    double avg=0;
    string str;
    count=m-n;
    avg=(m+n)/2;
    avg=floor(avg);
    if(m>n){
        str=to_string(avg);
        return str;
    }
    else{
        return "-1";
    }
}

int main(){
    int n,m;
    scanf("%d",&n);
    scanf("%d",&m);
    if(n>m){
        printf("-1");
        return 0;
    }
    else{
        printf("%s",rounded_avg(n,m).c_str());
        return 0;
    }
}


