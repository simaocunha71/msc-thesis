    int level=0;
    for (int i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        {
            level+=1;
        }
        if (str[i]==']')
        {
            level-=1;
            if (level<0)
                return true;
        }
    }
    return false;
} //This function returns true if there is at least one nested pair of brackets in the string. It does so by keeping track of the level of nesting using a counter. Whenever it encounters a ']', it decrements the counter and checks if the counter becomes negative, which means a nested pair of brackets was found. If the counter becomes negative at any point, the function immediately returns true. If the function finishes iterating over the string without finding any nested pairs, it returns false.