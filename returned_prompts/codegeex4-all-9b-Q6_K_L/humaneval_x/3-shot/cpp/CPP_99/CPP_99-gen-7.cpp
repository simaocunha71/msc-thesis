    float num;
    num=atof(value.c_str());
    if (num-int(num)<0.5)
        return int(num);
    else
        return int(num)+1;
}

