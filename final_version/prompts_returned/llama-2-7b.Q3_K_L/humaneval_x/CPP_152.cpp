/*
I think we all remember that feeling when the result of some long-awaited
event is finally known. The feelings and thoughts you have at that moment are
definitely worth noting down and comparing.
Your task is to determine if a person correctly guessed the results of a number of matches.
You are given two vectors of scores and guesses of equal length, where each index shows a match. 
Return a vector of the same length denoting how far off each guess was. If they have guessed correctly,
the value is 0, and if not, the value is the absolute difference between the guess and the score.


example:

compare({1,2,3,4,5,1},{1,2,3,4,2,-2}) -> {0,0,0,0,3,3}
compare({0,5,0,0,0,4},{4,1,1,0,0,-2}) -> {4,4,1,0,0,6}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<int> compare(vector<int> game,vector<int> guess){
	int total_guess=game.size();
	if(guess[0]==game[0]){
        return {0};
	}else{
		//printf("guess %d \n",guess[0]);
		for (int i = 1; i < total_guess - 1; ++i){
			if(guess[i]==game[i]){
            printf("%s",game.at(i).toString().c_str());
        }else if(guess[i]<game[i]){
            total_guess-=1;
            int sum = guess[0]+guess[1];
			//printf("sum %d \n",sum);
			if(sum==game.at(i).val())
               return {0};
			else{
			    //sum=game[i].val()-guess[0]+guess[1];
            int total_guess_after = game[i].size();