    int a,b,c,d;
    a=stoi(x.substr(0,x.find('/')));
    b=stoi(n.substr(0,n.find('/')));
    c=stoi(x.substr(x.find('/')+1));
    d=stoi(n.substr(n.find('/')+1));

    return (a*d)%b==0 && (c*d)%d==0;
}



