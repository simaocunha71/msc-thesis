    int collisions=0;
    for (int i=0;i<n;i++)
    {
        for (int j=i+1;j<n;j++)
        {
            if (i+j==n-1)
                collisions++;
        }
    }
    return collisions;
} // Time complexity is O(n^2), not the best.  Can it be improved?  Yes, by 
   // using a hash map to store the numbers, and then iterate over the map 
   // to find the collisions. This will reduce the time complexity to O(n) 
   // by using the hash map. 
   // int car_race_collision(int n){
   //     unordered_map<int,int> num_map;
   //     int collisions=0;
   //     for (int i=0;i<n;i++)
   //     {
   //         num_map[i]=1;
   //     }
   //     for (auto it=num_map.begin();it!=num_map.end();it++)
   //     {
   //         if (num_map.find(n-it->first-1)!=num_map.end())
   //             collisions++;
   //     }
   //     return collisions;
   // }  // This code will work fine for small inputs. But for large inputs, 
   //    // it will exceed the memory limit as it tries to store all the numbers 
   //    // in the map. So, we need to optimize it further. We can do this 
   //    // by only storing the numbers that are less than n/2 in the map. 
   //    // This is because the other numbers will have a collision with 
   //    // the numbers that are greater than n/2. 
   //    // int car_race_collision(int n){
   //    //     unordered_map<int,int> num_map;
   //    //     int collisions=0;
   //    //     for (int i=0;i<n;i++)
   //    //     {
   //    //         if (i<n/2)
   //    //             num_map[i]=1;
   //    //     }
   //    //     for (auto it=num_map.begin();it!=num_map.end();it++)
   //    //     {
   //    //         if (num_map.find(n-it->first-1)!=num_map.end())
   //    //             collisions++;
   //    //     }
   //    //     return collisions;
   //    // }  //