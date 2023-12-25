/*
You will be given a number in decimal form and your task is to convert it to
binary format. The function should return a string, with each character representing a binary
number. Each character in the string will be '0' or '1'.

There will be an extra couple of characters "db" at the beginning and at the end of the string.
The extra characters are there to help with the format.

Examples:
decimal_to_binary(15)   // returns "db1111db"
decimal_to_binary(32)   // returns "db100000db"
*/
#include<stdio.h>
#include<string>
using namespace std;
string decimal_to_binary(int decimal){
	if(decimal == 0) return "";
	else{
	unsigned long long int binary = decimal;//unsigned long long int: to represent decimal numbers in base 10.
	int reminder = binary % 2; //reminder is a remainder of binary divided by two (0 or 1). We are dividing the number by 2 and getting the remainder of the operation, hence 'reminder'.
	unsigned long long int new_decimal;//new decimal will hold the remainder.
	int j = 0;//j is to count the number of digits in binary representation.
	if(binary != 0){
		while(binary!=0) {
			long long decimals = binary % 10; //decimals will hold the 'digits' part of binary, for example if you were to convert a number like '523467810960' as binary, decimals will have values ranging from decimal(0) to 6.
			reminder = binary % 2;//to get the remainder we are dividing decimal by 2 and getting its reminder.
			binary = bindec(decimals + reminder); //addition of decimals with its reminder will be taken as binary and converted to decimal again, which will give us a new number.
			if(decimals != 0) {//if our result from addition is not zero then the remainder can hold another digit, else it will end there