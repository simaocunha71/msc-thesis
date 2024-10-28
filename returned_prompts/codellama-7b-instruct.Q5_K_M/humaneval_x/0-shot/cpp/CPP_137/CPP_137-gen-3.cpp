
    if(a.type()!=b.type())
    {
        if(a.type()==typeid(int) && b.type()==typeid(float))
        {
            return b;
        }
        else if(a.type()==typeid(float) && b.type()==typeid(int))
        {
            return a;
        }
        else if(a.type()==typeid(float) && b.type()==typeid(float))
        {
            return b;
        }
        else if(a.type()==typeid(int) && b.type()==typeid(int))
        {
            if(a==b)
            {
                return "None";
            }
            else
            {
                return b;
            }
        }
        else if(a.type()==typeid(string) && b.type()==typeid(string))
        {
            if(a==b)
            {
                return "None";
            }
            else
            {
                return b;
            }
        }
        else
        {
            goto A;
        }
    }
    else
    {
        return b;
    }

}

int main()
{
    cout<<compare_one(1, 2.5)<<endl;
    cout<<compare_one(1, "2,3")<<endl;
    cout<<compare_one("5,1", "6")<<endl;
    cout<<compare_one("1", 1)<<endl;
    return 0;
}
