    int x_num=atoi(x.c_str());
    int x_den=atoi(n.c_str());
    float x_num_float=(float)x_num;
    float x_den_float=(float)x_den;
    float result=x_num_float/x_den_float;
    if (result-int(result)==0)
    return true;
    else
    return false;
}

