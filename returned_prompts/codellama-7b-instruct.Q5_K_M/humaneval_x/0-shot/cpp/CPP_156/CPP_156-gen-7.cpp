/*
Given a positive integer, obtain its roman numeral equivalent as a string,
and return it in lowercase.
Restrictions: 1 <= num <= 1000

Examples:
>>> int_to_mini_roman(19) == "xix"
>>> int_to_mini_roman(152) == "clii"
>>> int_to_mini_roman(426) == "cdxxvi"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string int_to_mini_roman(int number){
    string mini_roman;
    if(number <= 5){
        switch(number){
            case 1:
                mini_roman = "i";
                break;
            case 2:
                mini_roman = "ii";
                break;
            case 3:
                mini_roman = "iii";
                break;
            case 4:
                mini_roman = "iv";
                break;
            case 5:
                mini_roman = "v";
                break;
        }
    }else if(number >= 6 && number <= 10){
        mini_roman = "x";
        switch(number - 6){
            case 1:
                mini_roman = "xi";
                break;
            case 2:
                mini_roman = "xii";
                break;
            case 3:
                mini_roman = "xiii";
                break;
            case 4:
                mini_roman = "xiv";
                break;
            case 5:
                mini_roman = "xv";
                break;
            case 6:
                mini_roman = "xvi";
                break;
            case 7:
                mini_roman = "xvii";
                break;
            case 8:
                mini_roman = "xviii";
                break;
            case 9:
                mini_roman = "xix";
                break;
        }
    }else