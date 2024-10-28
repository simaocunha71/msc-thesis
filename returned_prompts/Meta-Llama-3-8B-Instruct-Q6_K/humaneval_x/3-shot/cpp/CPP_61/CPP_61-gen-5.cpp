    int level=0;
    char chr;
    int i;
    for (i=0;i<brackets.length();i++)
    {
        chr=brackets[i];
        if (chr=='(')
        {
            level+=1;
        }
        if (chr==')')
        {
            level-=1;
            if (level<0)
            {
                return false;
            }
        }
    }
    return level==0;
}  // 0 if all brackets matched  // 1 if there are unmatched opening brackets  // -1 if there are unmatched closing brackets  // -2 if there are both unmatched opening and closing brackets
}  // 0 if all brackets matched  // 1 if there are unmatched opening brackets  // -1 if there are unmatched closing brackets  // -2 if there are both unmatched opening and closing brackets  // -3 if there are unmatched opening and unmatched closing brackets  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  // 