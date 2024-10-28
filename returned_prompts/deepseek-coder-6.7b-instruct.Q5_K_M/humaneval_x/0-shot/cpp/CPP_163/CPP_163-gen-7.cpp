    vector<int> even_digits;
    if(a>b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

B:
    for(int i=a;i<=b;i++)
    {
        if(i%2==0)
            even_digits.push_back(i);
    }
    return even_digits;
}


int main()
{
    vector<int> even_digits = generate_integers(8, 2);
    for(int i=0; i<even_digits.size(); i++)
    {
        printf("%d ",even_digits[i]);
    }
    return 0;
}

*/

#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int a = 2, b = 8;
    int even_digits[100], count = 0;

    for(int i = a; i <= b; i++) {
        if(i % 2 == 0) {
            even_digits[count++] = i;
        }
    }

    qsort(even_digits, count, sizeof(int), compare);

    for(int i = 0; i < count; i++) {
        printf("%d ", even_digits[i]);
    }

    return 0;
}

//c/problems/8/main.c
/*
