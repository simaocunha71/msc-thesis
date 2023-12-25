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
    vector<double> diff;
    for(int i=0;i<21;++i)
        if(!guess[i] && score[i]){
            diff.push_back(-score[i]);
            break;
        }else if(guess[i] && !score[i]){
            diff.push_back(score[i]+score[i]);//(score[i]-1);
            break;
        }else {diff.push_back(0);}
    return diff;
    
}
int main(){
	vector<int> game;
	game.push_back(5) ;
	game.push_back(2) ;
	game.push_back(-1) ;
	game.push_back(0) ;
	game.push_back(3) ;
	game.push_back(4) ;
	vector<int> guess;
        guess[0] = 1;
        guess[5] = 2;
        guess[-1] = 