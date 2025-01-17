# "Let's See Who's Got the Biggest One: Let's Do a Code Review"

Code review is one of the most delicate and important phases of a software project. Any software project we've developed or will develop over time has been or will be subjected to a code review.

It's unimaginable for code written by anyone not to undergo changes over time. While this might apply to individual parts of a project, when we look at the entirety of a software project, code review becomes a significant step between staying small and playing with dolls, or stepping out and becoming adults.

This step is therefore crucial to ensure code quality, to prevent errors from compromising the software's functionality, and to broaden the team's understanding of the code. Yes, because evolving the team is more important than indulging one's ego by looking at a few lines of code that only the author can understand.

## Code Review is Annoying

However, there's a fundamental problem: programmers find code review annoying, they don't like it, they consider it unnecessary or wrong if done by others, and believe it should be done and decided only by them.  
For some, it's like losing a child:

```text
That code was written that way for a very specific reason: Mario didn't want anyone to touch it, but now that he's left, no one understands it anymore.
```

A good time to do a code review is when fixing a bug. However, it's necessary to break away from the approach often adopted by programmers, who tend to be surgical and address the single issue without leveraging holistic thinking.

```text
I've been told there's an error when clicking a button, so I'll make sure there isn't.
```

In reality, the problem could be much deeper and require broader reflection. We should question why that button was clicked, if it was clicked by a user, if it was clicked by a user who shouldn't have clicked it, if it was clicked by a user who shouldn't have clicked it at that time, if it was clicked by a user who shouldn't have clicked it at that time and in that context.

Expanding the thought, we might also ask if the problem extends to other buttons, how and if it's reported, if it makes sense to have that button or those buttons performing that operation, if the operation that button performs is necessary, if the operation that button performs is necessary in that context.

Broadening the context, however, means spending time, using resources, questioning one's work and that of others, questioning one's ego and that of others, but by doing so, the code improves, the system improves, the team improves.

Therefore, it's necessary not to look at the single issue reported to us, but to try to understand the context in which it was made and if there are other parts of the code that could be improved.

Holistic thinking, even in code, is important: if we don't understand that a single change impacts the entire system, we can't understand the system, and if we don't understand the system, we can't improve it.

As Plato said:

```text
Refactoring is the art of removing the bad and adding the good to the code.
```

Perhaps the author wasn't Plato, but the concept is clear: the code needs to be improved, made more readable, more maintainable, more testable.

## Unused Code

If you've worked on the same project for more than five years, the phrase:

```text
We wrote that code for an "Important Client," who is no longer our client, but we don't remove it because it "might" be needed.
```

is almost a mantra that I'm sure you've heard at least once.  
Layering thoughts like this over time leads to having code that is incomprehensible, whose purpose is unknown, and whose workings are unclear: the specifications were intertwined with the client's needs, the team's requirements, and the technical choices of the moment.

Meanwhile, the code has changed, the team has changed, the client has changed, the needs have changed, the technical choices have changed: it's right for the code to change or be removed from the project. Maintaining unused code is costly and over time represents an unnecessary technical debt.

Some companies have realized how costly and pointless it is to maintain projects that are no longer used: code is a cost, not a value, if it's not used.

Google, for example, has a rich history of projects that have been abandoned. You can find traces of it on Wikipedia:

```text
https://en.wikipedia.org/wiki/Category:Discontinued_Google_services
```

## I Use Tabs, Those Who Use Spaces Aren't Good Programmers

In an episode of "Silicon Valley," the protagonist Richard discovers that his girlfriend Winnie uses spaces instead of tabs to indent code and breaks up with her: it's a cinematic exaggeration, but I know people who would never agree to work with someone who uses spaces instead of tabs and vice versa.

Breaking this habit, and this is coming from someone who has used spaces since they first touched a keyboard, is difficult but necessary: the code must be uniform, consistent, and readable. Having different styles within the team is counterproductive, slows down work, increases the possibility of errors, and makes maintenance difficult.

Within a code review, it's necessary to discuss these things too: it's not about imposing one's style, but finding a compromise that can be accepted by everyone and hopefully isn't a burden for anyone.

Once an agreement is reached, it's important to respect it: if it's decided to use spaces instead of tabs, you can't go back.

However, this is something difficult to accept and implement, both because some programmers consider code like a child that can't be changed, and because even when imposing a uniform style, sooner or later someone won't understand the specification, others will configure the IDE incorrectly, or lose settings after the first update.

In these situations, where the language itself doesn't help us maintain a uniform style (yes, there are languages that do this for us in an absolutely dictatorial way), it's important to use tools that allow us to automate code formatting as much as possible.

In one of the largest projects I follow, it was decided to adopt OpenRewrite, a tool that automatically reformats code in a uniform and consistent way, reducing differences between different programming styles: standardizing not only makes the code more consistent but also speeds up the onboarding of new team members and the transfer of a component from one team to another.

## Resistance to Change

Even though most programmers agree on the need for a code review, they often refuse to accept proposed changes, partly out of laziness, partly out of pride, and partly out of habit.

If you've been working the same way for years, and it works, why change?

```text
My code is born perfect
```

Unfortunately, no: it's not like that. Within a team, the aspect that must prevail is the readability of the code by everyone, the ease of onboarding a new resource, and the simplicity of modification even months after not touching certain lines.

It doesn't matter if the IDE you use formats the code in a certain way, it doesn't matter if you've always liked declaring variables with "_", adhering to a widespread standard, spontaneously or through automation, is an advantage, even if at first it may seem like a burden.

## Clean Code

One of the goals a code review should have is to write clean, readable, and maintainable code.

Sometimes I've faced the choice of whether to keep code that worked or dismantle it because, despite passing any functional test excellently, it was written in an obscure, difficult-to-read, and maintain way, and every time I put someone in front of that code, their expression was always the same:

```text
I don't understand what it does
```

Sometimes we believe that using the latest syntax proposed by a language is the solution to all our problems, but that's not always the case. Sometimes new constructs are based on concepts that are difficult to understand and explain, sometimes they're just sugar to make us feel more skilled: "sugar code" as some call it.

Not always is the most compact and concise code the best: sometimes it's better to write 10 lines of code that do what they need to do clearly and legibly, rather than a single line that does the same thing but that no one understands, gaining nothing in terms of performance and functionality.

## Automate What You Can

Strangely, programmers are more willing to accept something proposed by a program than something proposed by someone within the team.

If your team has the same atmosphere, you can propose introducing, within the project pipeline (hoping you have one), processes for code normalization and static analysis.

The former will help reduce style differences between programmers, while the latter will suggest changes, help us understand where bugs are hidden, where tests are missing, where cognitive complexity is too high, or where we can reduce code without losing clarity or effectiveness.

## But I Don't Care

Sometimes I spend my free time studying projects by other programmers, running some analyzers, and trying to fix some code: it's good practice and allows me to see how others tackle problems or underestimate the consequences of their code.

During these forays, I've encountered completely different approaches from individual programmers or teams of programmers to whom I submitted my Pull Requests.

Among all the projects I've analyzed, I'd like to talk about two that particularly struck me for how the team handled my contribution.

The first Pull Request concerns the JDK of OpenJDK. I noticed that, by mistake, 82 sources contained double ";" at the end of a line.  
You understand that it's not something important, we can even say it's something negligible, but I decided to make a Pull Request to fix the issue and see how the development team would react.

You can find the PR at this address:

```text
https://github.com/openjdk/jdk/commit/ccad39237ab860c5c5579537f740177e3f1adcc9
```

The approach, in my opinion, was interesting: first of all, 8 people were involved in analyzing the change, as the changes were horizontal across many Java packages.  
After a horizontal discussion among various maintainers and realizing that the issue was real, an issue was opened:

```text
https://bugs.openjdk.org/browse/JDK-8282657
```

There was also a discussion about a possible change to the build tools, which already removed spaces at the end of lines, introducing the removal of double ";" characters.

This approach denotes a team that analyzes every single change, discusses it, and tries to understand if the proposed change is actually useful or just someone's whim.  
In this case, they understood it was a trivial change but aimed at code cleanliness, and for this reason, it was accepted.

A second case involves a security tool developed by a single maintainer, also on GitHub.  
In that case, I had proposed a much more serious PR. There was redundant code, synchronized classes were used in processes where synchronization wasn't needed, some resources were opened without explicit closure, and so on.

It was therefore a change aimed at improving code quality and reducing the possibility of errors, not something trivial like removing a character.  
Moreover, switching to unsynchronized objects led to a performance increase of around 20%: all this without distorting the code, but simply using the right constructs and, with equal interfaces, the right classes.

In this case, I was convinced there would be no problems integrating this code into the project, but the response was negative.  
The maintainer replied that he didn't intend to integrate suggestions from a syntactic analyzer into his code and that I could use them on my fork, but he would never integrate them.

```text
If you don't like my code, fork it and modify it as you wish
```

This is the classic response of someone who doesn't want to change, who doesn't want to accept that their code can be improved, who doesn't want to accept that their code can be changed by others, even though the changes can improve readability and lead to tangible improvements.

## Conclusion

Even when everything works, reviewing code is important: it allows for project improvement, team improvement, and cutting down on technical debt.

Reducing technical debt, having the courage to dismantle even working code, discarding unused code, listening to static reviewers, standardizing programming style, automating code formatting as much as possible, are all steps that can improve the code and the team.

Don't be afraid to question what was written in the past and broaden your vision when you have to work on the code: don't just look at the single change, but try to understand the context in which it was made and if there are other parts of the code that could be improved.

A better product comes through many small steps, and even with hundreds of working tests, the code isn't necessarily perfect: code review is a fundamental step to ensure code quality and prevent errors from compromising the software's functionality.
