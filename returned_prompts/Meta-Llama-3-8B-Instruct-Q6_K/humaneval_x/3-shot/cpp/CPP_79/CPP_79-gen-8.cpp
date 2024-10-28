    string binary;
    while(decimal>0)
    {
        binary=char(decimal%2+'0')+binary;
        decimal=decimal/2;
    }
    return "db"+binary+"db";
}  //  or  return string("db") + binary + string("db");  // more C++ like


