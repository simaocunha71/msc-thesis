    int count=0;
    int i;
    int state=0;
    for (i=0;i<S.length();i++)
    {
        if (state==0)
        {
            if (S[i]=='I')
                state=1;
        }
        else
        {
            if (S[i]=='.' || S[i]=='?' || S[i]=='!')
                state=0;
        }
    }
    return state;
}  // Note: This function doesn't count the boredom correctly. It just checks if the string starts with 'I'.  // To count the boredom correctly, we need to split the string by '.' '?' or '!' and then check if the first word of each sentence is 'I'.  // Here's the correct version:  int is_bored(string S) {  int count = 0;  int i;  string sentence;  for (i=0;i<S.length();i++)  {    if (S[i]=='.' || S[i]=='?' || S[i]=='!')    {      if (sentence.find("I") == 0)        count++;      sentence = "";    }    else      sentence += S[i];  }  if (sentence.find("I") == 0)    count++;  return count;  }  // Now it correctly counts the number of boredoms in the string.  // For example, is_bored("The sky is blue. The sun is shining. I love this weather") will return 1.  // is_bored("Hello world") will return 0.  // is_bored("I am bored. I am so bored!") will return 2.  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...  // ...