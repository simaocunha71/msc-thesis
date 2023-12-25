/*
Return median of elements in the vector l.
>>> median({3, 1, 2, 4, 5})
3
>>> median({-10, 4, 6, 1000, 10, 20})
15.0
*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
float median(vector<float> l){
	if(l.size()==0)return 0.f;
	struct comparer{
		int left,right;
        bool operator()(const vector<float>& a, const vector<float>& b){
            if (a[0] < b[0]) return -1; // left side of partition
            else if (a[0] > b[0]) return 1; // right side of partition
            else{                         // elements are equal, find index i such that a[i].min(b[i]).
                int j=i;
                while (j>0 && l[j] == l[j-1]) j--;
                if (j<l.size()){
                    return -1; // left side of partition
                } else {
            return 1 ;// right side of partition
        }}
	};
float* temp=new float[2];
for(int i=0;i<l.size();i++){
temp[0]=l[i].min(left);
float n= l[i-1]> left? n: l[i] ;
if (n != 0) {
        float x = n, y = med, px = left, py = med;
	int ip, jp = -2; // j for partition
	while ((ip=jp+=2)!=j){
            int i0=i-1, i1=i+1; // indices of the partitions
            while (px < x && i0 >= 0 ){
                px = l[i0].min(temp[0]);
                if (px == y) { jp--; break;}
                else if (px > x) { jp++; continue; } // pivot is larger than