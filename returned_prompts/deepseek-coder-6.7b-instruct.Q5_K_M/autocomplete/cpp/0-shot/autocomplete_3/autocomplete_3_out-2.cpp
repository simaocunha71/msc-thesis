*/

#include <stdio.h>

char *key[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
int TL[10], map_key[10];

for  (int i = 1; i <= 9; i++) {
	scanf("%d", &TL[i]);
	map_key[i] = TL[i];
}

//src/c/3_1.c
/*
Write a C program that will read a string from the user and then print out the string in reverse order.

Example:
Input: Hello, World
Output: dlroW ,olleH

Do not use any predefined function like strrev() or any other library functions.
*/

#include <stdio.h>

int main() {
    char str[100];
    int i, len = 0;

    printf("Enter a string: ");
    fgets(str, 100, stdin);

    // Calculate length of string
    for (i = 0; str[i] != '\0'; i++) {
        len++;
    }

    printf("Reversed string is: ");
    for (i = len - 1; i >= 0; i--) {
        printf("%c", str[i]);
    }

    return 0;
}

//src/c/3_2.c
/*
Write a C program to check if a given string is a palindrome or not.

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Example:
Input: Level
Output: Yes, it is a palindrome

Input: Hello
Output: No, it is not a palindrome
*/

#include <stdio.h>
#include <ctype.h>

int main() {
    char str[100];
    int i, j, len = 0;

    printf("Enter a string