    int count=0;
    int i;
    bool in_sentence=false;
    for (i=0;i<S.length();i++)
    {
        if (S[i]=='.' || S[i]=='?' || S[i]=='!')
        {
            in_sentence=false;
        }
        else if (in_sentence)
        {
            if (S[i]=='I')
            {
                count++;
            }
        }
        else if (S[i]=='I')
        {
            in_sentence=true;
        }
    }
    return count;
}
# Include necessary libraries.
# Initialize a variable to store the count of boredoms.
# Iterate over each character in the input string.
# If the character is a punctuation mark, reset the 'in_sentence' flag.
# If the 'in_sentence' flag is True and the character is 'I', increment the boredom count.
# If the character is 'I' and the 'in_sentence' flag is False, set the 'in_sentence' flag to True.
# Return the boredom count.
# END OF CODE
# END OF CODE

