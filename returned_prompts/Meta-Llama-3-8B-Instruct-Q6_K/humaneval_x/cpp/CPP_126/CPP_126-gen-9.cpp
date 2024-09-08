    if(lst.size() < 2)
        return true;
    for(int i = 1; i < lst.size(); i++){
        if(lst[i] < lst[i-1])
            return false;
        else if(lst[i] == lst[i-1])
            return false;
    }
    return true;
}

int main(){
    vector<int> lst = {1, 2, 3, 4, 5};
    printf("%d\n", is_sorted(lst));
    return 0;
}*/


C:
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool is_sorted(int* lst, int n) {
    for (int i = 1; i < n; i++) {
        if (lst[i] < lst[i-1]) {
            return false;
        }
        else if (lst[i] == lst[i-1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int lst[] = {1, 2, 3, 4, 5};
    int n = sizeof(lst) / sizeof(lst[0]);
    printf("%d\n", is_sorted(lst, n));
    return 0;
}
C++:
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool is_sorted(vector<int> lst) {
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] < lst[i-1]) {
            return false;
        }
        else if (lst[i] == lst[i-1]) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<int> lst = {1, 2, 3, 4, 5};
    printf("%d\n", is_sorted(lst));
    return 0;
}
C#:
using System;
using System.Linq;

class Program
{
    static bool IsSorted(int[] lst)
    {
        for (int i = 1; i < lst.Length; i++)
        {
            if (lst[i] < lst[i - 1])
            {
                return false;
            }
            else if (lst[i] == lst[i - 1])
            {
                return false;
            }
        }
        return true;
    }

    static void Main()
    {
        int[] lst = new int[] { 1, 2, 3, 4, 5 };
        Console.WriteLine