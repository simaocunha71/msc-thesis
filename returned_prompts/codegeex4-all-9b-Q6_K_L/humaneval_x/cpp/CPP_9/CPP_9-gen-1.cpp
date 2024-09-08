vector<int> result;
int max = numbers[0];
result.push_back(max);
for(int i=1; i<numbers.size(); i++){
    if(numbers[i] >= max){
        max = numbers[i];
    }
    result.push_back(max);
}
return result;

B:
vector<int> result;
int max = numbers[0];
result.push_back(max);
for(int i=1; i<numbers.size(); i++){
    if(numbers[i] > max){
        max = numbers[i];
    }
    result.push_back(max);
}
return result;

C:
vector<int> result;
int max = numbers[0];
result.push_back(max);
for(int i=1; i<numbers.size(); i++){
    if(numbers[i] <= max){
        max = numbers[i];
    }
    result.push_back(max);
}
return result;

D:
vector<int> result;
int max = numbers[0];
result.push_back(max);
for(int i=1; i<numbers.size(); i++){
    if(numbers[i] < max){
        max = numbers[i];
    }
    result.push_back(max);
}
return result;

E:
vector<int> result;
int max = numbers[0];
result.push_back(max);
for(int i=1; i<numbers.size(); i++){
    if(numbers[i] == max){
        max = numbers[i];
    }
    result.push_back(max);
}
return result;
答案：
A

###PATH:./data-structures-cpp-master/README.md
# data-structures-cpp
Data Structures in C++: Stack, Queue, Hash Table, List, Tree, Graph, etc.
###PATH:./data-structures-cpp-master/HashTable/HashTable.cpp
#include "HashTable.h"

HashTable::HashTable(int size)
{
    table.resize(size);
}

void HashTable::insert(const string &word)
{
    int index = hashFunction(word);
    table[index].push_back(word);
}

bool HashTable::contains(const string &word)
{
    int index = hashFunction(word);
    for (int i = 0; i < table[index].size(); i++)
    {
        if (table[index][i] == word)
        {
            return true;
        }
    }
    return false;
}

int HashTable::hashFunction(const string &word)
{
    int sum = 0;
    for (int i = 0; i < word.length(); i++)
    {
        sum += int(word[i]);
    }
    return sum % table