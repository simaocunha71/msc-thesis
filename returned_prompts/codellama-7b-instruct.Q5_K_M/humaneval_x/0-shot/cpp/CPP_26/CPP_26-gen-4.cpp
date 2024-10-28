/*
Write a function to compute the best time to buy and sell a stock
such that you can make a profit of at least $100.
>>> stocks = [10, 20, 30, 40, 50]
>>> best_time_to_buy_and_sell_stock(stocks)
4
>>> stocks = [10, 20, 30, 40, 50, 100]
>>> best_time_to_buy_and_sell_stock(stocks)
5
*/
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int best_time_to_buy_and_sell_stock(vector<int> stocks){

