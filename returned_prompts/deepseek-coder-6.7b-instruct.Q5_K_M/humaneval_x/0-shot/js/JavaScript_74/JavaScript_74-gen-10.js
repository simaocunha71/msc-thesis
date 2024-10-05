  let charsInList1 = lst1.join("").length;
  let charsInList2 = lst2.join("").length;

  if(charsInList1 < charsInList2) return lst1;
  if(charsInList2 < charsInList1) return lst2;
  return lst1;
}

console.log(totalMatch([], [])); // ➞ []
console.log(totalMatch(['hi', 'admin'], ['hI', 'Hi'])); // ➞ ['hI', 'Hi']
console.log(totalMatch(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])); // ➞ ['hi', 'admin']
console.log(totalMatch(['hi', 'admin'], ['hI', 'hi', 'hi'])); // ➞ ['hI', 'hi', 'hi']
console.log(totalMatch(['4'], ['1', '2', '3', '4', '5'])); // ➞ ['4']

Explanation:
The function totalMatch is accepting two parameters, lst1 and lst2, which are two lists of strings. It first calculates the total number of characters in the strings in lst1 and lst2 by joining the strings in both lists and getting their length. It then compares these two counts and returns the list with the smaller count. If both counts are equal, it returns lst1.
*/
```

## C# Solution
```csharp
using System;
using System.Linq;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        Console.WriteLine(string.Join(", ", TotalMatch(new List<string>{}, new List<string>{}))); // ➞ []
        Console.WriteLine(string.Join(", ", TotalMatch(new List<string>{"hi", "admin"}, new List<string>{"hI", "Hi"}))); // ➞ hI, Hi
        Console.WriteLine(string.Join(", ", TotalMatch(new List<string>{"hi", "admin"}, new List<string>{"hi", "hi",