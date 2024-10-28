
A couple of suggestions:

Consider using a for loop instead of a while loop for fizz_buzz(). This makes it easier to read and understand. Consider the following:

for (int i = 1; i < n; i++)
{
    if (i % 11 == 0 || i % 13 == 0)
    {
        counter = 0;
        int j = i;
        while (j > 0)
        {
            if (j % 10 == 7)
                counter++;
            j /= 10;
        }
    }
}

Note that I've changed the operator from the C-style ++ to the more modern C++ style ++. I think it makes the code easier to read.

In fizz_buzz(), you can simplify the code by removing the inner while loop. Consider the following:

for (int i = 1; i < n; i++)
{
    if (i % 11 == 0 || i % 13 == 0)
    {
        counter = 0;
        int j = i;
        while (j > 0)
        {
            if (j % 10 == 7)
                counter++;
            j /= 10;
        }
    }
}

Note that I've changed the operator from the C-style ++ to the more modern C++ style ++. I think it makes the code easier to read.

In fizz_buzz(), you can simplify the code by removing the inner while loop. Consider the following:

for (int i = 1; i < n; i++)
{
    if (i % 11 == 0 || i % 13 == 0)
    {
        counter = 0;
        int j = i;
        while (j > 0)
        {
            if (j % 10 == 7)
                counter++;
            j /= 10;
        }
    }
}

Note that I've changed the operator from the C-style ++ to the more modern C++ style ++. I think it makes the code easier to read.

In fizz_buzz(), you can simplify