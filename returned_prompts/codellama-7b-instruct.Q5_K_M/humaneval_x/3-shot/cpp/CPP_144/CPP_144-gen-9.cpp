    int x_num=x.find("/")+1;
    int x_denom=x.find("/")-x_num;
    int n_num=n.find("/")+1;
    int n_denom=n.find("/")-n_num;
    int x_mult=atoi(x.substr(x_num,x_denom).c_str());
    int n_mult=atoi(n.substr(n_num,n_denom).c_str());
    int result=x_mult*n_mult;
    string result_str=to_string(result);
    int result_num=result_str.find("/")+1;
    int result_denom=result_str.find("/")-result_num;
    if(result_str.length()==result_denom)
    return true;
    else
    return false;
}


