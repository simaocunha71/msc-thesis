    int count=0;
    string vowels = "aeiou";

    // converting the string to lowercase
    transform(s.begin(), s.end(), s.begin(), ::tolower);

    // checking each character
    for(int i=0; i<s.length(); i++)
    {
        // if it is a vowel, increment the count
        if(vowels.find(s[i]) != string::npos)
            count++;
    }

    // if the last character is 'y', increment the count
    if(s[s.length()-1] == 'y')
        count++;

    return count;
}
int main() {
    printf("%d\n", vowels_count("abcde")); 
    printf("%d\n", vowels_count("ACEDY")); 
    return 0;
}

// output will be 2 and 3 respectively.
```



## Python

```python
def vowels_count(s):
    vowels = "aeiou"
    count = sum(1 for char in s.lower() if char in vowels)
    if s[-1] == 'y':
        count += 1
    return count

print(vowels_count("abcde"))  # output will be 2
print(vowels_count("ACEDY"))  # output will be 3
```



## C#

```csharp
using System;
using System.Linq;

public class Program
{
    public static void Main()
    {
        Console.WriteLine(vowels_count("abcde"));  // output will be 2
        Console.WriteLine(vowels_count("ACEDY"));  // output will be 3
    }

    public static int vowels_count(string s)
    {
        int count = 0;
        string vowels = "aeiou";

        // converting the string to lowercase
        s = s.ToLower();

        // checking each character
        foreach (char c in s)
        {
            // if it is a vowel, increment the count
           