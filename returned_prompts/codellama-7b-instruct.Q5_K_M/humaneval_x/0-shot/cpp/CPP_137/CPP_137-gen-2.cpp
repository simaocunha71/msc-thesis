    if(a==b){
        return "None";
    }
    if(a.type()!=b.type()){
        goto A;
    }
    if(a.type()==typeid(float)||a.type()==typeid(double)){
        return *max_element(boost::any_cast<float>(&a),boost::any_cast<float>(&b));
    }
    else if(a.type()==typeid(string)){
        string a_string = boost::any_cast<string>(a);
        string b_string = boost::any_cast<string>(b);
        return max(a_string,b_string);
    }
    else{
        return *max_element(boost::any_cast<int>(&a),boost::any_cast<int>(&b));
    }
}
int main(){
    cout<<compare_one(1, 2.5)<<endl;
    cout<<compare_one