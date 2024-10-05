    int xnum=0,xden=0,nnum=0,nden=0;
    int len1=x.length(),len2=n.length();
    for(int i=0;i<len1;i++){
        if(x[i]=='/'){
            xnum=atoi(x.substr(0,i).c_str());
            xden=atoi(x.substr(i+1,len1-i-1).c_str());
            break;
        }
    }
    for(int i=0;i<len2;i++){
        if(n[i]=='/'){
            nnum=atoi(n.substr(0,i).c_str());
            nden=atoi(n.substr(i+1,len2-i-1).c_str());
            break;
        }
    }
    long long int num=(long long int)nnum*xden;
    long long int den=(long long int)nden*xnum;
    long long int gcd=gcd(num,den);
    num/=gcd,den/=gcd;
    if(num==1&&den==1)return true;
    return false;
}























































































































































































































