    vector<float> derivative;
    derivative.push_back(0);
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(i * xs[i]);
    }
    return derivative;
}

B:
    vector<float> derivative;
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(i * xs[i-1]);
    }
    return derivative;
}

C:
    vector<float> derivative;
    derivative.push_back(xs[1]);
    for(int i = 1; i < xs.size()-1; i++){
        derivative.push_back(i * xs[i]);
    }
    return derivative;
}

D:
    vector<float> derivative;
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(i * xs[i]);
    }
    return derivative;

E:
    vector<float> derivative;
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(xs[i-1]);
    }
    return derivative;

F:
    vector<float> derivative;
    derivative.push_back(0);
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(xs[i-1]);
    }
    return derivative;

G:
    vector<float> derivative;
    derivative.push_back(xs[0]);
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(i * xs[i]);
    }
    return derivative;

H:
    vector<float> derivative;
    derivative.push_back(0);
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(i * xs[i]);
    }
    return derivative;

I:
    vector<float> derivative;
    derivative.push_back(xs[1]);
    for(int i = 1; i < xs.size()-1; i++){
        derivative.push_back(xs[i]);
    }
    return derivative;

J:
    vector<float> derivative;
    derivative.push_back(0);
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(xs[i-1]);
    }
    return derivative;

K:
    vector<float> derivative;
    derivative.push_back(xs[1]);
    for(int i = 1; i < xs.size(); i++){
        derivative.push_back(xs[i]);
    }
    return derivative;

L:
    vector<float> derivative;
    derivative.push_back(0);
    for(int i = 1; i < xs.size(); i++){
       