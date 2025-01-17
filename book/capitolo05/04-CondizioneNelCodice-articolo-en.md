# "Can you change this condition in the code? What does it take?"

What sets a senior programmer apart from a junior programmer? Many will say it's the ability to assess the consequences of a code change. In reality, it's the loss of carefreeness and a set of regressive fears.

## The fears of seniors

I used to be much quicker at changing an algorithm, modifying a function parameter, creating or destroying flows, and so on. The goal was, first and foremost, to do what the client asked for, and only secondarily to ensure that the code was maintainable or that the choice made was the best among a series of more or less considered options.

Then I aged and started using tests to understand if my code was still good after a change. I began writing documentation to understand why I had reasoned in a certain way, and started doing code reviews to improve code understanding and maintenance.

This new "complicated" approach made my work more complex, or rather: it elongated the processes that, from a request, led to the final solution. A change that I used to make in 10 minutes now takes a whole day because I have to evaluate all the impacts that change can have, run all automated tests, perform some manual tests where automation wasn't possible, write documentation, merge with the main code, wait for the build and integration tests, verify that everything works, and finally declare the issue resolved, hoping I haven't forgotten anything.

Years go by, and it's inevitable that there's an evolution from the carefree child who pushes without tests to the cariatide who also fixes spaces when adding code to the main branch (no, "master" is no longer used).

```text
What was once a happy and enthusiastic "yes," 
grows into a "yes, but I also do this," 
slowly becomes a "maybe," 
until it becomes a "no"
or worse, a "it depends."
```

## Seniors are not bad

It's not out of malice that all this happens, but out of an awareness of what revolves around a single line of code. It's an awareness of the error or impacts of a change and of an extensive regression that has too often undermined the certainty that a single condition can be changed without problems. This doesn't mean that changes shouldn't be made; it just means that impacts should always be evaluated so as not to create bigger problems than the ones you're trying to solve. Often, as one ages, the impacts multiply in the programmer's mind.

Think about the software's lifecycle and its design. Initially, developing a product is relatively easy: we see our goal, have an idea of how to achieve it, ensure that clients and stakeholders are satisfied, and if we're lucky, we manage to create a cohesive team both technically and humanly. This isn't always a given because sometimes just one outlier can destabilize an entire group. Once this goal is achieved, when a change is needed, all team members are aligned and aware of what needs to be done.

As you move away from this phase of collective euphoria and creative phase, the development team starts to change from its original form. At the same time, the client reduces the budget because it enters a maintenance phase, and if due attention isn't paid, mastery of the product begins to slip away.

```text
No, it's certainly not the tests that can govern the product,
but the minds that conceived it.
```

Project turnover is an inevitable process, unless you find yourself in an igloo in the middle of the pole, devoid of internet connection, and the poor programmers who developed the project can't even send a resume unless they attach it to a seal (although there's always the possibility that the programmer dedicates themselves to fishing, their great passion suppressed by code).

When a team member changes, a part of the product knowledge is lost, and mastery begins to slip away. Consequently, every intervention becomes more costly, lengthy, and risky.

## Does project maintenance change the rules?

In a normal product lifecycle, some parts require frequent updates, while many other parts, due to maturation, lack of requests, or stability, don't need changes. Making changes infrequently diminishes the programmer's knowledge of the code they wrote. This means that the person who wrote those lines of code two years ago is likely to not remember them and need to review them to recall the processes that led to their creation.

The more vertical the change, the harder it is to remember the reason behind it: you may not remember why you used one parameter over another within a connection to an external resource, why you use one encryption suite over another, or maybe you have an open branch for months, awaiting a client's verification on an urgent feature that suddenly became less important, but now you need to merge it into a baseline with 400 more pushes, and you wonder if it makes more sense to start over or apply the changes to a rebase.

Amidst these types of interventions are the day-to-day tasks, feature changes, bug fixes, requests for new features, bug fixes introduced while fixing a bug, code introduced by a colleague with little product knowledge, behavior changes introduced by an update or a new component that necessitates code changes and introduces an indirect anomaly.

You, who wrote that code, don't remember it. You understand that, in the face of several changes, the modification to be made is larger than anticipated, but you must figure out how to do it because you remember the rationale behind the previous code and understand it's not a simple change. Imagine someone who has to fix the same code and is touching it for the first time.

As Heraclitus said:

```text
No man ever steps in the same river twice,
for it's not the same river and he's not the same man.
```

This statement can easily be applied to code: every change, no matter how small, alters the code and the context in which it exists, which is different from the context in which it was created, and the person is also different from the person who wrote that code.

## Use case of a well-known Italian bank

For a moment, imagine being a senior programmer at a "random bank," where you were told to proceed with a system update and related firmware update, assuring that it wouldn't cause any harm and that the update would be done in production. Having seen these types of interventions many times in your life, the first thing that comes to mind is to run a test. However, there isn't a test environment that exactly mirrors the production environment, both in terms of scale and use cases. You advise against the massive update, but the solution provider assures that there won't be any issues. The security department informs you that the update must be implemented by a certain date to comply with company rules and that, in case of problems, a rollback is possible.

Reluctantly, you agree, partly driven by the fact that "we work with agile methodology and must be ready for change" and that "we can't always be negative."

```text
Disruptions to online services access (such as app, Invest app, Internet Banking, and Smart Business)
occurred following the installation of an operating system update
and related firmware update that led to an unstable situation.
We sincerely apologize and greatly appreciate your understanding.
```

A "simple" operating system and firmware update led to an unstable situation for a whole 5 days.

Clearly, in this hypothetical scenario, the issue wasn't the update itself but the lack of testing, the absence of a test environment covering production, the lack of an immediate rollback, and the absence of a disaster recovery plan or the underestimation of risk.

## How is the perception of changes outside the project?

Often, those outside the project have a completely different perception of software development and push for changes to be made as soon as possible.

```text
I need it yesterday.
```

This phrase is a classic, but often it's not understood that a change, even a simple one, can lead to a series of problems that go well beyond the change itself.

```text
I only asked to change one condition, why is Mario causing me all these problems?
Now I'll assign the task to Bruno, who will solve it in 2 minutes.
```

There are situations within projects that allow code alteration very quickly, and other situations where a change, even a simple one, may require much thought: even if it's just a few lines of code or even a single additional condition. Each programmer approaches the change differently based on their experience, product knowledge, and code understanding. The more experienced programmers are with the product, the more likely they are to carefully evaluate the change because they are aware of the potential consequences. The less a programmer knows about the product, the more likely they are to make changes quickly.

## Conclusions

Every change, no matter how simple, can lead to performance issues, regression, security concerns, maintainability challenges, code understanding difficulties, documentation gaps, testing problems, and deployment issues.

External alterations to the project can create the same problems: I updated the operating system, I updated a driver, I updated the firmware, and now nothing works.

The pressure on a programmer increases progressively over time because awareness grows of everything that can go wrong and how difficult it is to solve a problem once it occurs.

This can lead to situations where a senior programmer refuses to make a change because they know the risks are too high or because they know the change would require too much time and resources to be done correctly.

The next time you look at a programmer who has been working on the same code for many years and doesn't want to modify it, and warns you about every internal or external alteration to the project, don't think of them as incapable, but rather as an aware individual. Use their advice to avoid project collapse and weigh the risks and benefits of each change carefully because, as Isaac Asimov said:

```text
No sensible decision can be made any longer without taking into account
not only the world as it is, but the world as it will be.
```
