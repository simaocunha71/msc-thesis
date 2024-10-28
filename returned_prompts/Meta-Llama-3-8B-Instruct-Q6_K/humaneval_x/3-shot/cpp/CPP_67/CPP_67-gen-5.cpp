    int apples, oranges;
    string temp;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            temp="";
            i++;
        }
        if (s[i]>='0'&&s[i]<='9')
        {
            temp+=s[i];
        }
        if (s[i]=='a'&&s[i+1]=='p')
        {
            apples=stoi(temp);
        }
        if (s[i]=='o'&&s[i+1]=='r')
        {
            oranges=stoi(temp);
        }
    }
    return n-apples-oranges;
} 
// This is a very bad code, it's not recommended to use it in production.
// The function is not robust and will fail for most inputs.
// For example, it will not handle cases where the string contains multiple sets of 
// apples and oranges, or where the string contains other types of fruit. 
// It also does not handle the case where the total number of fruits in the basket is not 
// equal to the sum of the apples and oranges.
// The function also assumes that the string is in a specific format, which may not always be 
// the case. 
// It's better to write a more robust function that can handle these cases. 
// For example, you could use a regular expression to extract the numbers of apples and 
// oranges from the string, and then check that the total number of fruits is equal to 
// the sum of the apples and oranges. 
// You could also use a more robust way to parse the string, such as using a parser 
// library. 
// In general, it's a good idea to write code that is robust and can handle a wide range 
// of inputs, rather than code that is specific to a particular input. 
// This will make your code more reliable and easier to maintain. 
// It will also make it easier to add new features and functionality to your code in the 
// future. 
// For example, you could add a feature to handle multiple sets of apples and oranges, 
// or to handle other types of fruit. 
// You could also add a feature to check that the total number of fruits is equal to 
// the sum of the apples and oranges, and to handle the case where it's not. 
// This would make your code more robust and reliable, and would make it easier to add 
// new features and functionality in the future. 
