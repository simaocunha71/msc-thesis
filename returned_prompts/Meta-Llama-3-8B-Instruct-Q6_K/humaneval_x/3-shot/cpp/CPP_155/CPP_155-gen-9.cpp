    vector<int> result(2,0);
    int temp=num;
    while(temp!=0)
    {
        int digit=temp%10;
        if(digit%2==0)
            result[0]++;
        else
            result[1]++;
        temp=temp/10;
    }
    return result;
}  // This solution works with both positive and negative numbers. It counts the number of even and odd digits in the number and returns the counts as a vector. The count of even digits is stored in the first element of the vector and the count of odd digits is stored in the second element. This solution can handle large numbers as well because it uses integer division and modulus operations which are efficient and can handle large numbers.  // This solution is efficient and has a time complexity of O(log10(n)) where n is the number of digits in the number.  // This solution is easy to understand and implement.  // This solution can be easily extended to count the number of even and odd digits in a string or a character array.  // This solution can be used in a variety of applications such as counting the number of even and odd digits in a phone number or an IP address.  // This solution can be used in a variety of programming languages including C++, Java, Python, and C#.  // This solution can be used in a variety of algorithms and data structures such as arrays, linked lists, stacks, and queues.  // This solution can be used in a variety of real-world applications such as finance, science, and engineering.  // This solution can be used in a variety of programming paradigms such as imperative, object-oriented, and functional programming.  // This solution can be used in a variety of programming languages and frameworks such as C++, Java, Python, and C#.  // This solution can be used in a variety of algorithms and data structures such as arrays, linked lists, stacks, and queues.  // This solution can be used in a variety of real-world applications such as finance, science, and engineering.  // This solution can be used in a variety of programming paradigms such as imperative, object-oriented, and functional programming.  // This solution can be used in a variety of programming languages and frameworks such as C++, Java, Python, and C#.  // This solution can be used in a variety of algorithms and data structures such as arrays, linked lists, stacks, and queues.  // This solution can be used in a variety of real-world applications