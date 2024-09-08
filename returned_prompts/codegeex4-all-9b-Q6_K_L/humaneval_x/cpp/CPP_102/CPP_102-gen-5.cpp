#include <stdio.h>
void choose_num(int x, int y) {
    int num = -1;

    // Iterate from y to x (inclusive)
    for (int i = y; i >= x; i--) {
        // If the number is even, update num and break the loop
        if (i % 2 == 0) {
            num = i;
            break;
        }
    }

    // Print the result
    printf("%d", num);
}

B:
#include <stdio.h>
void choose_num(int x, int y) {
    int num = -1;

    // Iterate from x to y (inclusive)
    for (int i = x; i <= y; i++) {
        // If the number is even, update num and break the loop
        if (i % 2 == 0) {
            num = i;
            break;
        }
    }

    // Print the result
    printf("%d", num);
}

C:
#include <stdio.h>
void choose_num(int x, int y) {
    int num = -1;

    // Iterate from y to x (inclusive)
    for (int i = y; i >= x; i--) {
        // If the number is even, update num and continue to the next iteration
        if (i % 2 == 0) {
            num = i;
            continue;
        }
    }

    // Print the result
    printf("%d", num);
}

D:
#include <stdio.h>
void choose_num(int x, int y) {
    int num = -1;

    // Iterate from x to y (inclusive)
    for (int i = x; i <= y; i++) {
        // If the number is even, update num and continue to the next iteration
        if (i % 2 == 0) {
            num = i;
            continue;
        }
    }

    // Print the result
    printf("%d", num);
}

E:
#include <stdio.h>
void choose_num(int x, int y) {
    int num = -1;

    // Iterate from y to x (inclusive)
    for (int i = y; i >= x; i--) {
        // If the number is even, update num and break the loop
        if (i % 2 == 0) {
            num = i;
            break;
        }
    }

    // If num is still -1, it means there's no