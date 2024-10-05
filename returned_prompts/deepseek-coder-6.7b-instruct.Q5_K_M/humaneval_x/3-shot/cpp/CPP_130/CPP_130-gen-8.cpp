    vector<int> tri;
    if(n<0)
        return tri;
    if(n>=0)
        tri.push_back(3);
    if(n>=1)
        tri.push_back(2);
    if(n>=2)
        tri.push_back(8);
    for(int i=3;i<=n;i++){
        if(i%2==0)
            tri.push_back(1+i/2);
        else
            tri.push_back(tri[i-1]+tri[i-2]+tri[i+1]);
    }
    return tri;
}
```

## Submission

Submit your answers for all three questions in one submission.

You can submit your solutions by clicking on the "Submit" button on the bottom right corner of the page. Make sure to provide clear and detailed explanations for your code.

If you have any issues or doubts, feel free to ask in the comments section. We are here to help you.

Good luck with your coding journey and happy learning 🥳🎉

### Note:

- You can write your code in any programming language you are comfortable with.
- The time complexity of your code is considered. So, write your code in such a way that it will be efficient.
- The expected output is given in the question. So, make sure your code is producing the expected output.
- The code should be simple, easy to understand and follow good coding practices.
- Please ensure that you follow the instructions carefully.
- Make sure to provide clear and concise explanations for your code.
- Make sure to test your code thoroughly.
- You can ask for help if you need it.
- Do not forget to submit your code.

Remember, practice makes perfect. Happy coding 🥳

### Note:

- You can write your code in any programming language you are comfortable with.
- The time complexity of your code is considered. So, write your code in such a way that it will be efficient.
- The expected output is given in the question. So, make sure your code is producing the expected output.
- The code should be simple, easy to understand and follow good coding practices.
- Please ensure that you follow the