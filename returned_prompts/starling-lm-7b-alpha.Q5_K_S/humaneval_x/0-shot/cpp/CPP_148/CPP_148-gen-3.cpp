    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    if(planet1=="Mercury"||planet1=="Venus"||planet1=="Earth"||planet1=="Mars"||planet1=="Jupiter"||planet1=="Saturn"||planet1=="Uranus"||planet1=="Neptune"){
        if(planet2=="Mercury"||planet2=="Venus"||planet2=="Earth"||planet2=="Mars"||planet2=="Jupiter"||planet2=="Saturn"||planet2=="Uranus"||planet2=="Neptune"){
            vector<string> ans;
            int i;
            for(i=0;i<planets.size();i++){
                if(planets[i]!=planet1&&planets[i]!=planet2){
                    if(planets[i]<planet1){
                        continue;
                    }
                    if(planets[i]>planet2){
                        break;
                    }
                    ans.push_back(planets[i]);
                }
            }
            return ans;
        }else{
            goto A;
        }
    }else{
        goto A;
    }
}
int main(){
    vector<string> ans=bf("Jupiter","Neptune");
    for(int i=0;i<ans.size();i++){
        printf("%s ",ans[i]);
    }
    return 0;
}



































































































