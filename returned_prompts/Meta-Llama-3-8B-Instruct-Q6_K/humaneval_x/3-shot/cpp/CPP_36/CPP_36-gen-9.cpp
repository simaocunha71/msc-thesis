    int count=0;
    for (int i=1;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            char buffer[10];
            sprintf(buffer, "%d", i);
            for (int j=0;j<strlen(buffer);j++)
            {
                if (buffer[j]=='7')
                count++;
            }
        }
    }
    return count;
}  // This code is not efficient as it converts each number to string and then checks for digit. It can be improved by checking the digit directly without conversion.
}
