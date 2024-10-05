    return true;

B:
    return false;
}

int main(){

    vector<int> arr = {3, 4, 5, 1, 2};
    if(move_one_ball(arr)){
        printf("true\n");
    }
    else{
        printf("false\n");
    }

    return 0;
}

