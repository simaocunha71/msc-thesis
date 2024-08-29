#include<stdio.h>
#include<vector>
#include<string>
#include<map>
using namespace std;
map<string,int> planet_distance={
    {"Mercury",0},
    {"Venus",1},
    {"Earth",2},
    {"Mars",3},
    {"Jupiter",4},
    {"Saturn",5},
    {"Uranus",6},
    {"Neptune",7}
};
vector<string> bf(string planet1,string planet2){
    vector<string> planet_names;
    if(planet_distance.count(planet1) && planet_distance.count(planet2)){
        int d1=planet_distance[planet1];
        int d2=planet_distance[planet2];
        for(int i=min(d1,d2);i<=max(d1,d2);i++){
            for(auto it=planet_distance.begin();it!=planet_distance.end();it++){
                if(it->second==i)
                    planet_names.push_back(it->first);
            }
        }
        return planet_names;
    }
    return planet_names;
}
