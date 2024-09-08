    double cube_root = cbrt(a);
    if(cube_root == (int)cube_root)
        return true;
    return false;

}

int main()
{
    printf("%d\n",iscuber(1));  // Output: 1
    printf("%d\n",iscuber(2));  // Output: 0
    printf("%d\n",iscuber(-1)); // Output: 1
    printf("%d\n",iscube(64));  // Output: 1
    printf("%d\n",iscube(0));   // Output: 1
    printf("%d\n",iscube(180)); // Output: 0
    return 0;
}
