
if(a == b){
return "None";
}

if(a < b){
return b;
}

if(a > b){
return a;
}

return "None";
}

int main(int argc, char const *argv[])
{
    string a = "3";
    string b = "4";
    cout << compare_one(a,b);
    return 0;
}

