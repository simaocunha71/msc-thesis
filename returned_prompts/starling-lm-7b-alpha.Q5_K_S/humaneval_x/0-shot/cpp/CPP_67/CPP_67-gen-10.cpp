    int x,y,z,t=0;
    x=s.find("apples");
    y=s.find("oranges");
    z=s.find("mango");
    if(x==string::npos && y==string::npos && z==string::npos)
        return 0;
    else{
        char a,b,c;
        a=s[x-1];
        b=s[y-1];
        c=s[z-1];
        s.erase(x-1,7);
        s.erase(y-1,7);
        s.erase(z-1,6);
        string p,q,r;
        p=s.substr(0,x);
        q=s.substr(x,y-x);
        r=s.substr(y,z-y);
        x=p.size();
        y=q.size();
        z=r.size();
        int u,v,w;
        u=x*2;
        v=y*2;
        w=z*2;
        if(u==0 && v==0 && w==0)
            t=n;
        else if(u==0 && v==0)
            t=n-w;
        else if(u==0 && w==0)
            t=n-v;
        else if(v==0 && w==0)
            t=n-u;
        else if(u==0)
            t=n-(v+w);
        else if(v==0)
            t=n-(u+w);
        else if(w==0)
            t=n-(u+v);
        else
            t=n-(u+v+w);
    }
    return t;
}
int main(){
    string s;
    int n;
    cin>>s>>n;
    cout<<fruit_distribution(s,n);
    return 0;
}







































