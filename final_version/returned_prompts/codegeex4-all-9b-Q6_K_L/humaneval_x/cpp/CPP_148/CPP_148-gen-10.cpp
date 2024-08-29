#include<stdio.h>
#include<math.h>
#include<string>
#include<vector>
using namespace std;
#define PI 3.14159265358979323846
vector<string> bf(string planet1,string planet2){
    vector<string> v;
    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    for(int i=0;i<planets.size();i++){
        if(planet1==planets[i] || planet2==planets[i]){
            for(int j=0;j<i;j++){
                v.push_back(planets[j]);
            }
        }
    }
    if(v.size()==0){
        return v;
    }
    else{
        return v;
    }
}