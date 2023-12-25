/*
You'll be given a string of words, and your task is to count the number
of boredoms. A boredom is a sentence that starts with the word "I".
Sentences are delimited by '.', '?' or '!'.

For example:
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
*/
#include<stdio.h>
#include<string>
using namespace std;
int is_bored(string S){
	int i,j=0;
	for(i=1;*S!='\0';++i)
	{	if((*(S+i))=='I') j++;
	}
	return j;
}
int main(){
	printf("%d ",is_bored("Hello world"));
	printf("%d ",is_bored("The sky is blue. The sun is shining. I love this weather"));
	return 0;
}