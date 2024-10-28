    int x_num=stoi(x.substr(0,x.find('/')));
    int x_den=stoi(x.substr(x.find('/')+1,x.length()));
    int n_num=stoi(n.substr(0,n.find('/')));
    int n_den=stoi(n.substr(n.find('/')+1,n.length()));
    if (x_num*n_den==x_den*n_num)
    return true;
    else
    return false;
}



