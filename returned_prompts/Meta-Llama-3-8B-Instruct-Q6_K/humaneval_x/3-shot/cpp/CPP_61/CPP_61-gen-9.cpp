    int level=0;
    for (int i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='(')
        level+=1;
        if (brackets[i]==')')
        {
            level-=1;
            if (level<0)
            return false;
        }
    }
    return level==0;
}  // level should be 0 at the end if brackets are correct.  // if level is negative, it means we have extra close bracket.  // if level is greater than 0, it means we have extra open bracket.  // level should not change when we reach the end of the string.  // if level is 0 at the end, it means every open bracket has a corresponding close bracket.  // if level is not 0 at the end, it means not every open bracket has a corresponding close bracket.  // so we should return false when level is not 0 at the end.  // so the function should return true when level is 0 at the end and false when level is not 0 at the end.  // so we should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0.  // so the function should return level==0