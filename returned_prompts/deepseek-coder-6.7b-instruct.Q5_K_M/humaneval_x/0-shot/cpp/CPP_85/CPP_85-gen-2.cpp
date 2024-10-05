    int sum=0;
    for(int i=0;i<lst.size();i++){
        if(i%2==1 && lst[i]%2==0){
            sum += lst[i];
        }
    }
    return sum;
}

int main(){
    vector<int> lst = {4, 2, 6, 7};
    printf("%d",add(lst));
    return 0;
}



The above code calculates the sum of even numbers at odd indices in a vector. The function add() iterates over the vector and checks if the index is odd and the corresponding element is even. If so, it adds it to the sum.
*/

// Your code should be similar to this:

#include <iostream>
#include <vector>

int add(const std::vector<int>& lst)
{
    int sum = 0;
    for(size_t i = 1; i < lst.size(); i += 2)
    {
        if(lst[i] % 2 == 0)
        {
            sum += lst[i];
        }
    }
    return sum;
}

int main()
{
    std::vector<int> lst = {4, 2, 6, 7};
    std::cout << add(lst) << std::endl;
    return 0;
}

The above code calculates the sum of even numbers at odd indices in a vector. The function add() iterates over the vector and checks if the index is odd and the corresponding element is even. If so, it adds it to the sum.

