    for (int i=0;i<l.size();i++){
        for (int j=0;j<l.size();j++){
            if (l[i]+l[j]==0){
                return true;
            }
        }
    }
    return false;
}

int main(int argc, char** argv){
    vector<int> l = {1, 3, 5, 0};
    cout << pairs_sum_to_zero(l) << endl;
    return 0;
}

