    for(auto itr:dict){
        if( (itr.first[0]>='a' && itr.first[0]<='z') != (itr.second[0]>='a' && itr.second[0]<='z')){
            return false;
        }
    }
    return true;
}


int main(){
    map<string,string> dict;
    dict["A"] = "1";
    dict["B"] = "2";
    dict["C"] = "3";
    dict["D"] = "4";
    dict["E"] = "5";
    dict["F"] = "6";
    dict["G"] = "7";
    dict["H"] = "8";
    dict["I"] = "9";
    dict["J"] = "0";
    dict["K"] = "A";
    dict["L"] = "B";
    dict["M"] = "C";
    dict["N"] = "D";
    dict["O"] = "E";
    dict["P"] = "F";
    dict["Q"] = "G";
    dict["R"] = "H";
    dict["S"] = "I";
    dict["T"] = "J";
    dict["U"] = "K";
    dict["V"] = "L";
    dict["W"] = "M";
    dict["X"] = "N";
    dict["Y"] = "O";
    dict["Z"] = "P";
    printf("%d\n",check_dict_case(dict));
    return 0;
}


















*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    map<string, string> mp;
    mp["A"] = "1";
    mp["B"] = "2";
    mp["C"] = "3";
    mp["D"] = "4";
    mp["E"] = "5";
    mp["F"] = "6";
    mp["G"] = "7";
    mp["H"] = "8";
   