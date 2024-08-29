#include<stdio.h>
#include<vector>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                vector<int> coord = {i, j};
                result.push_back(coord);
            }
        }
    }
    return result;
}

B:
#include<stdio.h>
#include<vector>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                vector<int> coord = {i, j};
                result.push_back(coord);
            }
        }
    }
    return result;
}

C:
#include<stdio.h>
#include<vector>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                vector<int> coord = {i, j};
                result.push_back(coord);
            }
        }
    }
    return result;
}

D:
#include<stdio.h>
#include<vector>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                vector<int> coord = {i, j};
                result.push_back(coord);
            }
        }
    }
    return result;
}

E:
#include<stdio.h>
#include<vector>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x){
    vector<vector<int>> result;
    for(int i = 0; i < lst.size(); i++){
        for(int j = 0; j < lst[i].size(); j++){
            if(lst[i][j] == x){
                vector<int> coord = {i, j};
                result.push_back(coord);
