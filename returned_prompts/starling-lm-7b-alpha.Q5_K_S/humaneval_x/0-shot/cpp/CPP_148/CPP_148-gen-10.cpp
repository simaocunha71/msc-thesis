    vector<string> ans;
    vector<string> planets = {"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    int index1 = -1,index2 = -1;
    for(int i=0;i<planets.size();i++) {
        if(planets[i] == planet1) index1 = i;
        if(planets[i] == planet2) index2 = i;
    }
    if(index1 == -1 || index2 == -1) return {};
    for(int i=index1;i<=index2;i++) {
        ans.push_back(planets[i]);
    }
    return ans;
}

int main() {
    vector<string> res = bf("Jupiter", "Neptune");
    for(auto t:res) printf("%s ",t.c_str());
    printf("\n");
    return 0;
}












































*/

ANSWER:
vector<string> bf(string planet1,string planet2){

    vector<string> ans;
    vector<string> planets = {"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    int index1 = -1,index2 = -1;
    for(int i=0;i<planets.size();i++) {
        if(planets[i] == planet1) index1 = i;
        if(planets[i] == planet2) index2 = i;
    }
    if(index1 == -1 || index2 == -1) return {};
    for(int i=index1;i<=index2;i++) {
        ans.push_back(planets[i]);
    }
    return ans;
}





























