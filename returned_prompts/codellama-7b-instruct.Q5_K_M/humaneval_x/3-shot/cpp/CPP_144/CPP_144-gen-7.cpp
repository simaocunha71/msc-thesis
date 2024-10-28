    int x_num,x_denom,n_num,n_denom;
    x_num=stoi(x.substr(0,x.find('/')));
    x_denom=stoi(x.substr(x.find('/')+1,string::npos));
    n_num=stoi(n.substr(0,n.find('/')));
    n_denom=stoi(n.substr(n.find('/')+1,string::npos));
    if (x_num*n_denom==x_denom*n_num){
        return true;
    }
    else{
        return false;
    }
}



