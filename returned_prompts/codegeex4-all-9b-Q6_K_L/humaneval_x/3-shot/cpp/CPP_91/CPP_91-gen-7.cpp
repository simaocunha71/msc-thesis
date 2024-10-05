
In the first function, you have a variable named i in the for loop, but you also have a variable named i in the if statement. You should rename one of them to prevent confusion.
for (i=0;i<numbers.size();i++)
for (j=i+1;j<numbers.size();j++)

In the second function, you can simplify the for loop by using a range-based for loop.
for (auto chr : paren_string)

In the third function, you can use the fmod function to calculate the decimal part of the number.
return fmod(number, 1.0);

In the fourth function, you can use the stringstream class to split the string into words.
stringstream ss(S);
string word;
while (ss >> word)
{
    if (word == "I")
        bored += 1;
}

Overall, your code looks good, but there are some minor improvements that can be made.