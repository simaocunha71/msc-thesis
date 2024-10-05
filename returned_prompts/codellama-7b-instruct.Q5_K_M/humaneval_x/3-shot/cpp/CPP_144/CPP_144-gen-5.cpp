    int xn=int(x.substr(0,x.find('/')));
    int xd=int(x.substr(x.find('/')+1));
    int xnum=xn*xd;
    int yn=int(n.substr(0,n.find('/')));
    int yd=int(n.substr(n.find('/')+1));
    int ynum=yn*yd;
    if (xnum%ynum==0)
    return true;
    else
    return false;
}



