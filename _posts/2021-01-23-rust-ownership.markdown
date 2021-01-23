---
layout: post
title: Rust Ownership
---

*This post is not finished yet, come back later when I finish it up

Rust has a concept of ownership which is unique from other languages I have seen before. Only one variable can own a piece of data. For example, you cannot store a piece of data in an array, and then extract it into a variable, without also completed invalidating the data inside the array. This is called a 'move', similar to 'move semantics' in c++. If afterwards you try to reference the data in the array, there is a compile time error.

This ends up working very well. There are two things in the following example I want to point out.

1) Intent to 'move' a value is explicity expressed in the function types.
2) Intent to modify a value is explicity expressed in the function defintion.
3) Intent to copy a value is explicity expressed in the function types.

Check out the following example.

{% highlight rust %}
fn largest<T: PartialOrd + Clone>(list: &Vec<T>) -> T {
    let mut largest: &T = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest.clone()
}
{% endhighlight %}

This function finds the largest element in an array, and returns it. It also works on generic types, which shows the flexibility of Rust. Let's focus on the three points above. In this implementation, we DONT want to alter the vector 'list'. We enter to a contract with the caller where we state we will not alter the state of "list". This is expressed in the function definition by the lack of "mut" keyword. If we try to alter the state, we will get a compile time error. Rust prevents a very insidious bug here. If we try to aquire a value in the vector, with something like --- let mut largest = list[0]; ---, Rust will throw a compile error. This prevents us from gaining write access to the data inside the array at all. We have to explicity say we are grabbing a read reference. Then in the return, we HAVE to call clone, following our contract. In order to return that mutable type T, we must clone the data. So, to summarize, we see the following.

1) the ampersand in &Vec<T> shows we don't want ownership
2) the lack of 'mut' shows we won't alter list
3) requiring T to implement Clone prevents people using our function on unclonable values, which would be a bug (since instead we would have to remover ownership of the data from 'list')
4) the above contract has guarantees that are enforced by the compiler. We can't take ownership of data in the list, and we can't mutate it

Now let's change our contract. Let's say that it is ok to take ownership of the data.

