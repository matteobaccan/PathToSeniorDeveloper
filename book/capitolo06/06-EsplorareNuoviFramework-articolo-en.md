# Adopting New Frameworks Could Jeopardize Your Project

In the world of software development, the allure of new technologies is always strong. It's tempting to get your hands on a new product, especially one that promises to solve a series of problems that other frameworks can't address.

These new projects often boast a small but energetic community, promise to speed up development times, and offer interesting innovations compared to their competitors. All of this sounds very promising, but is it really the right choice for a long-term project?

Donald Knuth, one of the fathers of modern computing, commented on his own code this way:

```text
Beware of bugs in the above code; I have only proved it correct, not tested it.
```

If this had been written by a junior programmer, it might seem like a joke. But coming from Knuth, it’s not only humorous but might also indicate that the code was syntactically correct but not testable.

Sometimes, it's much easier to demonstrate a concept, describe its functionality, and document it, rather than actually applying it, which might involve a series of unforeseen aspects.

This concept can be paraphrased as: "A brilliant idea doesn't always work in reality." Thinking about this, I can't help but consider the world of blockchain: excellent tools on paper, but often criticized in practice for performance and resource usage.

Stepping outside the software world, think about products like the Segway, which, despite being a brilliant idea, didn't achieve the expected success. Or Google Glass, which, despite being an innovative product, never took off.

## And the Frameworks?

Frameworks and, more generally, software technologies often suffer from initial hype that excites programmers, distracting them from a solid analysis of their long-term effectiveness. Are the concepts used in that new software applicable to all projects? Are they easily integrable with other technologies? Are there solid companies investing in that technology? Is the community active and supportive?

The so-called "early adopters" are often attracted to novelties but frequently don't realize the risks involved in this choice. If everything goes well, they've made a lucky choice that leads to the success of their software. But if the chosen product fails to deliver on its promises, they end up with software that doesn't work as it should and requires much more maintenance and refactoring than anticipated.

For those who have been developing software for over 30 years, the name Visual Objects might ring a bell: it was supposed to be the new Clipper and bring millions of DOS programmers into the Windows environment. A fantastic idea, but it didn't work: too many problems, too many bugs, too many limitations. At the time, it had the backing of a company like Computer Associates, which could afford to invest millions of dollars in a product, but despite this, it never took off.

That's why, when it comes to choosing a framework or technology for a project, it's important to consider not only its technical features but also its long-term sustainability.

![Frameworks](06-EsplorareNuoviFramework-articolo-1-leonardo-ai.jpg)

## The Time Horizon: A Crucial Dimension

Whenever I evaluate a project, I try to anticipate its lifecycle, or at least what it should be, based on my experience and the information at my disposal. The crystal ball doesn't exist, and the future is unpredictable, but there are signs that indicate whether a project will be short, medium, or long-term.

To understand how long a project might last, it's important to consider various aspects:

- **Long-term objectives**: What are the project's goals? Is it a product that solves a single problem or something structured to last years or just a few months?
- **Market stability**: Is the market in which the project operates stable or rapidly evolving? The dynamism of a market can lead to rapid changes that require greater flexibility from the project.
- **Competition**: What is the level of competition in the sector in which the project operates? Working in an arena where other players might come from larger, more structured companies can require greater attention to the quality and sustainability of the project.
- **Industry trends**: What are the current trends in the sector in which the project operates? Some projects are born outdated because they are based on obsolete technologies or outdated business models.
- **Available resources**: What resources are available for the development and maintenance of the project? Are these "one-man show" projects, or are there structured teams behind them?

These are just some of the possible indicators, but relying solely on the name and what is promised often underestimates the risk.

When using young frameworks or technologies, it's important to consider that they might not be supported long-term or might not adapt to market changes. This can lead to high maintenance costs, compatibility issues, and increased code complexity.

On the other hand, it's also necessary to evaluate the projects you intend to undertake. They might be projects born and completed over a weekend: in this case, the primary need is problem-solving. Others might need to last a few months to meet a specific need. Finally, there are projects destined to last years, on which a company intends to build its operational base: in these situations, the choice of framework and project architecture becomes crucial and cannot be based solely on the trend of the moment.

The time horizon is a dimension that every software architect should consider because it significantly influences the expectations and choices that can be made.

For a "one-shot" project, you can safely adopt the CIRO framework, created by a nomad from Tanzania, used only by his group of friends, with a single release made a few years ago, if it astonishingly solves a crucial problem for the project. If, however, I need to create something that must last beyond the expiration date of a dessert, perhaps I should moderate my aggressiveness in choosing the software components to use and base my decisions on different KPIs.

## The Risk of Abandonment

I've used both "closed source" and "open source" products whose creators disappeared into thin air, as did the community that was part of it. If this happens with "closed" products, it's certainly very worrying, but don't fall into the illusion that everything is rosy if it happens with "open" products. Using a product is one thing; developing it and knowing it inside out is another.

The mind of someone who designs a solution is usually trapped between the lines of code of the product itself and is certainly more immersed in its internal logic than someone who uses it, who often exploits only a part of its potential. So don't think that "open" means "there's a problem: I'll fix it," because it's not always the case.

Linus Torvalds, creator of Linux, has a strong opinion on this subject:

```text
Software is like sex: it's better when it's free.
```

Although Torvalds uses this quote to promote open-source software, it's important to remember that "free" doesn't necessarily mean "without costs" and that the freedom to access a project's source code doesn't necessarily mean being able to maintain and evolve it.

## The Importance of Periodic Analysis

This is one of the reasons why we should always perform an analysis of the life of the products we adopt. An analysis to be repeated periodically, taking into account the current context, the project's maturity, and its future prospects.

If this aspect can be ignored for short projects, for those that exceed years of development, the problem becomes pressing: either the product and its dependencies are updated, or you find yourself in a dead end due to the countless entanglements of your code.

A periodic analysis allows us to evaluate whether the framework or technology we are using is still suitable for our needs, if it is actively supported by the community, and if it can adapt to market changes.

## The Risk of Non-Standard Services

This also applies to all the problems that can arise from adopting a non-standard service, which could be withdrawn from the market or double its prices from one season to the next.

Jeff Bezos has an interesting view on how companies should approach technology:

```text
You have to be stubborn on the vision and flexible on the details.
```

This philosophy can also be applied to the choice of frameworks, services, and software development: while technical details can change, fundamental principles like scalability, maintainability, and interoperability should remain constant.

For this reason, creating software that is tightly coupled with a framework could lead to maintenance and scalability issues in the future. If the framework is no longer supported or cannot adapt to market changes, we might find ourselves in a situation where we need to rewrite much of the code to adapt it to a new technology.

I've seen products make technical choices that, on paper, seemed the best, only to realize over time that the software coupling was so strong that changing one part meant having to change everything else. This problem can also be avoided with proper analysis and a thoughtful choice of components used, decoupling usage from implementation and accepting the need to change part of the software if necessary.

## Conclusion

When it comes to young solutions or frameworks, the risk of wasting time and resources is considerable. If you love uncertainty and the project's duration is not a factor you want to consider, you are free to make any choice and build a product full of unanswered questions.

In case of errors, keep in mind that you might need to start from scratch unless your software is sufficiently modular to allow the replacement of a component without having to rewrite everything else.

The choice of a framework or technology should be guided not only by enthusiasm for innovation but also by a careful evaluation of long-term risks and benefits. Sustainability, maintainability, and scalability should always be at the top of our priorities when making architectural decisions.
