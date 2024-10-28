    int i;
    int int_value;
    float float_value;
    for (i=0;i<value.length();i++)
        if (value[i]=='.')
        {
            value=value.substr(0,i);
            int_value=atoi(value.c_str());
            float_value=atof(value.c_str());
            if (float_value-int_value>=0.5)
                return int_value+1;
            else
                return int_value;
        }
    return atoi(value.c_str());
}

