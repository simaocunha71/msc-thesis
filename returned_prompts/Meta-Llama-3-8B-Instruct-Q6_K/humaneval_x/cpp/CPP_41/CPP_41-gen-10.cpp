    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += i;
    }
    return collision;
}

B:
    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += n - i - 1;
    }
    return collision;

C:
    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += n - i - 1;
        collision += i;
    }
    return collision;

D:
    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += i;
        collision += n - i - 1;
    }
    return collision;

E:
    int i, collision = 0;
    for(i = n - 1; i >= 0; i--){
        collision += i;
        collision += n - i - 1;
    }
    return collision;

F:
    int i, collision = 0;
    for(i = n - 1; i >= 0; i--){
        collision += i;
    }
    return collision;

G:
    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += i;
    }
    return collision;

H:
    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += n - i - 1;
    }
    return collision;

I:
    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += i;
        collision += n - i - 1;
    }
    return collision;

J:
    int i, collision = 0;
    for(i = n - 1; i >= 0; i--){
        collision += i;
        collision += n - i - 1;
    }
    return collision;

K:
    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += i;
        collision += n - i - 1;
    }
    return collision;

L:
    int i, collision = 0;
    for(i = 0; i < n; i++){
        collision += i;
        collision += n - i - 1;
    }
    return collision;
}

M:
   