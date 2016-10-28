## SOLID - Principles that Apply

This page is designated to collect some good resources (IMHO) in order to give
an overview over good priciples that should be applied to software design.

- [Intro to `SOLID`](http://www.wikiwand.com/en/SOLID_(object-oriented_design))
    - `S`: Single Responsibility Principle.
        - [link](http://www.oodesign.com/single-responsibility-principle.html)
    - `O`: Open/Close Principle.
        - [link](http://joelabrahamsson.com/a-simple-example-of-the-openclosed-principle/)
    - `L`: Liskov Substitution Principle.
        - [link](http://www.objectmentor.com/resources/articles/lsp.pdf)
        - [Stack Overflow](http://stackoverflow.com/questions/56860/what-is-the-liskov-substitution-principle)
        - [Circle-Ellipse Problem](https://en.wikipedia.org/wiki/Circle-ellipse_problem)
        - **Moral of the story: model your classes based on behaviours not on properties; model your data based on properties and not on behaviours. If it behaves like a duck, it's certainly a bird.**
        - **This strongly suggests that inheritance should never be used when the sub-class restricts the freedom implicit in the base class, but should only be used when the sub-class adds extra detail to the concept represented by the base class as in 'Monkey' is-an 'Animal'.**
    - `I`: Interface Segregation Principle
        - [link](http://www.oodesign.com/interface-segregation-principle.html)
        - [Wiki](https://en.wikipedia.org/wiki/Interface_segregation_principle)
    - `D`: Dependency Inversion Principle
        - [link](http://www.oodesign.com/dependency-inversion-principle.html)
        - [Code Tutorials](http://code.tutsplus.com/tutorials/solid-part-4-the-dependency-inversion-principle--net-36872)
        - **Program to an interface, not an implementation.**

## Running the Code

All the submodules are managed in the same way, which means you can run the code using the same syntax. For example, if you want to see the result of the sample code for Open/Close principle, just run:

```
python -m python_code.bad.open_close   # See the result of bad implementation
python -m python_code.good.open_close  # See the result of good implementation
```

Or, you can run `python -m python_code --list` or `python -m python_code -l` to see all the available submodules.

However, it is recommanded to see the source code and get an understanding of what the issue is and possible way to solve it.

Enjoy coding!

## Other Interesting Articles

- [Programming Done By Superstition](https://utcc.utoronto.ca/~cks/space/blog/programming/ProgrammingViaSuperstition)
- [Object Mentor](http://www.objectmentor.com/resources/publishedArticles.html)
- [Clean Coder](http://cleancoders.com/category/fundamentals)
- [Code Tutorials](http://code.tutsplus.com/series/the-solid-principles--cms-634)
- [搞笑談軟工](http://teddy-chen-tw.blogspot.tw/2012/01/5dependency-inversion-principle.html)
