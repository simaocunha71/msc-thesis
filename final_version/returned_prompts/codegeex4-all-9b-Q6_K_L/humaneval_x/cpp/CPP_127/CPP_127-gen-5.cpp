/*
#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string intersection( vector<int> interval1,vector<int> interval2){
    int start=0,end=0;
    if(interval1[0]>interval2[0]){
        start=interval1[0];
    }else{
        start=interval2[0];
    }
    if(interval