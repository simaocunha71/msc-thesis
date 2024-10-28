    int res = 0,count = 0;
    for(int i = 0;i < lst.size();i++)
    {
        if(i % 2 != 0 && lst[i] % 2 == 0)
        {
            res += lst[i];
            count++;
        }
    }
    return res;
}
int main()
{
    vector<int> lst = {4, 2, 6, 7};
    printf("%d",add(lst));
    return 0;
}



/*
In the above program, we are taking a vector of integers and we have to add the even elements that are at odd indices. The given vector is [4, 2, 6, 7]. The even elements at odd indices are 4 and 2. The sum of these elements is 2 and thus, it will be printed out.

In the add function, we initialize the result variable to 0 and the count variable to 0. We then iterate over the vector using a for loop. Inside the loop, we check if the index of the element is odd using the condition i % 2 != 0. If the index is odd, we check if the element itself is even using the condition lst[i] % 2 == 0. If both conditions are true, we add the element to the result variable and increment the count variable. After the loop, we return the result.

In the main function, we create a vector of integers and initialize it with the values [4, 2, 6, 7]. We then call the add function with this vector as the argument and print out the result using the printf function.
*/






























































































































