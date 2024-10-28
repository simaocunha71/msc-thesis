    return n*(n-1)
}
// The reason is that each car is colliding with the other n-1 cars that are moving in the opposite direction. If there are n cars, there are n*(n-1) collisions.