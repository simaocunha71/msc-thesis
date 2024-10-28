
	result := make(chan int)
	go fib(n, result)
	return <-result
}

func fib(n int, result chan int) {
	if n <= 1 {
		result <- n
		return
	}

	r1 := make(chan int)
	r2 := make(chan int)
	go fib(n-1, r1)
	go fib(n-2, r2)

	result <- (<-r1) + (<-r2)
}
```

## Conclusion

In this tutorial, we have learned how to use Go routines to solve problems concurrently. We have also learnt to use channels to pass the results back and forth between Go routines. This is a very powerful feature of Go and can greatly increase the performance of our code.

## References

1. [Go by Example](https://gobyexample.com/)
2. [Go Tour](https://tour.golang.org/)
3. [Go Documentation](https://golang.org/doc/)

You should check them out to learn more about the language.

## Further Reading

1. [Concurrency is not parallelism](https://www.oreilly.com/content/concurrency-is-not-parallelism/)
2. [Go Concurrency Patterns: Pipelines and Cancellation](https://blog.golang.org/pipelines)
3. [Go Concurrency Patterns: Context](https://blog.golang.org/context)

These are in-depth articles on concurrent programming in Go. They will give you a deeper understanding of the concepts we discussed in this tutorial.

## Note

This tutorial assumes you have basic knowledge of Go programming. If you are new to Go, I would recommend learning the basics of the language before starting this tutorial.

Happy coding 🥳

---
Peer Review Contributions by: [Lalithnarayan C](/engineering-education/authors/lalithnarayan-c/)

<!-- MathJax script for rendering equations -->
<script type="text/javascript" async
    src="https://cdnjs.cloudflare