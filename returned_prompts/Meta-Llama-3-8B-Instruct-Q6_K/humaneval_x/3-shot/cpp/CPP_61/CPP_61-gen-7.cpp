    int level=0;
    for (char chr:brackets)
    {
        if (chr=='(')
            level+=1;
        if (chr==')')
        {
            level-=1;
            if (level<0)
                return false;
        }
    }
    return level==0;
}  // This function correctly checks if the brackets are balanced. It initializes a level counter to zero. For each opening bracket, it increments the level counter, and for each closing bracket, it decrements the level counter. If the level counter ever becomes negative, it means that there are more closing brackets than opening brackets, so the function returns false. Finally, it checks if the level counter is zero at the end of the function. If it is, then all brackets were properly matched, and the function returns true. If it's not, then there were unmatched brackets, and the function returns false.