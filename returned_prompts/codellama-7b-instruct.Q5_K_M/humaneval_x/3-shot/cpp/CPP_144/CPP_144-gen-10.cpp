    int x1, x2, n1, n2;
    x1=x.find("/");
    x2=x.find("/",x1+1);
    n1=n.find("/");
    n2=n.find("/",n1+1);
    int a=stoi(x.substr(0,x1))*stoi(n.substr(n1+1));
    int b=stoi(x.substr(x2+1))*stoi(n.substr(0,n1));
    return (a%b==0);
}


