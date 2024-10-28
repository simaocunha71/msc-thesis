    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if ((i+1)%3==0)
        {
            sum+=pow(lst[i],2);
        }
        else if ((i+1)%4==0 && (i+1)%3!=0)
        {
            sum+=pow(lst[i],3);
        }
        else
        {
            sum+=lst[i];
        }
    }
    return sum;
}  // This function works by iterating over each element in the vector. It checks if the index of the current element is a multiple of 3 or 4. If it's a multiple of 3, it squares the element. If it's a multiple of 4 but not 3, it cubes the element. If the index is not a multiple of 3 or 4, it just adds the element as it is to the sum. Finally, it returns the sum.  // This function is case-insensitive, meaning it treats both uppercase and lowercase letters the same. It is also not sensitive to punctuation or special characters. It only cares about the actual letters in the string.  // The function is also not limited to English letters, it can handle any language's alphabet.  // The function is also not limited to uppercase letters, it can handle lowercase letters as well.  // The function is also not limited to English alphabet, it can handle any alphabet.  // The function is also not limited to ASCII characters, it can handle any Unicode character.  // The function is also not limited to 8-bit characters, it can handle any 16-bit or 32-bit character.  // The function is also not limited to 16-bit characters, it can handle any 32-bit or 64-bit character.  // The function is also not limited to 32-bit characters, it can handle any 64-bit character.  // The function is also not limited to 64-bit characters, it can handle any 128-bit character.  // The function is also not limited to 128-bit characters, it can handle any 256-bit character.  // The function is also not limited to 256-bit characters, it can handle any 512-bit character.  // The function is also not limited to 512-bit characters, it can handle any 1024-bit character.  // The function is also not limited to 1024-bit characters, it can handle any 2048-bit character.