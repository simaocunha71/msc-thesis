    return n*(n-1);

} // end of function car_race_collision

B:
    return n*(n-1)/2;

} // end of function car_race_collision

C:
    return n*(n+1);

} // end of function car_race_collision

D:
    return n*(n+1)/2;

} // end of function car_race_collision

Explanation:

The correct answer is B: return n*(n-1)/2;

The explanation is as follows:

The problem is asking for the number of collisions between cars moving in both directions.

Each car moving in one direction can potentially collide with every car moving in the other direction. So, we have n cars moving in one direction and n cars moving in the other direction. Therefore, there are n*n possible collisions.

However, we are considering the case where two cars are the same. For example, if we have two cars moving in the same direction and we consider them to be different cars, we would count the same collision twice. So, we need to divide the total number of collisions by 2.

Therefore, the correct answer is n*(n-1)/2.

Note: The problem description states that the cars are infinitely sturdy and strong, but it doesn't say that they are also infinitely long. Therefore, we don't need to consider the case where two cars are the same. However, we still need to divide the total number of collisions by 2 to avoid counting the same collision twice.