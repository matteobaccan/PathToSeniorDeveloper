# The "Hardcore" Attitude of Programmers

In the world of programming, there's a curious phenomenon we might call "hardcore-ism." This term describes a stubborn resistance to the evolution of software development tools and practices.

Once upon a time, when resources were scarce and precious, programmers had to be incredibly ingenious to squeeze every drop of power from their systems. This necessity forged habits and mindsets that, in some cases, have survived well beyond their practical utility, transforming into a sort of professional folklore.

```text
640K ought to be enough for anybody
```

This famous phrase attributed to Bill Gates, although he has denied saying it, aptly represents the attitude of many "hardcore" programmers towards technological innovation. For these programmers, the idea of using modern tools like advanced IDEs, graphical debuggers, or AI assistants seems almost heretical, a violation of the fundamental principles of "real" programming, a symptom of weakness and incompetence.

## Historical Roots

In the early days of computing, when computers were powered by punch cards, programming meant working with systems that had limited memory and processors. Programmers of that era had to be true artists of optimization, capable of writing code that was both functional and extremely efficient.

This era produced masterpieces of ingenuity and practices that still survive in resource-constrained environments: have you ever tried programming for microcontrollers or embedded systems? Here, every byte of memory and every clock cycle counts, and the art of optimization is still very much alive, even if some cracks are starting to show on the horizon.

Over time, as hardware evolved, many of these limitations have disappeared, but the ethic of "doing more with less" has remained deeply rooted in programming culture, sometimes transforming into an attitude of resistance towards tools and practices that could simplify and speed up development work.

```text
"The most efficient code is the code you don't have to write"
```

## The Manifesto of Hardcore-ism

To understand what kind of programmer you are, here's a little test to evaluate your degree of "purity." Try to gauge how much you agree or disagree with these statements:

### 1. The IDE is useless

A programmer should be spartan: the fewer tools they use, the more competent they are.

```text
"To write code, all I need is Notepad (or Vi) and the CLI"
```

This statement is often made with a mix of pride and nostalgia. Those who support it seem to want to communicate: "I am a real programmer; I don't need any help." This position deliberately ignores the advantages offered by modern IDEs.

Personally, I've seen programmers use commands like:

```text
copy con: pippo.prg
```

with the same pride as someone getting top marks in school.

However, let's not underestimate the advantages of modern IDEs and first of all, let's get rid of the idea that IDEs are just fancy text editors. They are powerful tools that integrate numerous features to improve productivity and code quality:

- Debugging: Breakpoints, real-time variable inspection and alteration, step-by-step code execution, call stack, and much more.
- Refactoring: Renaming variables or functions throughout the project with a single click, extracting methods, or safely reorganizing code.
- Static analysis: Identifying potential bugs, style violations, or problematic patterns before execution.
- Integration with version control systems: Managing branches, commits, and merges directly from the IDE interface.
- Support for frameworks and libraries: Autocompletion not just for base libraries but also specific suggestions for the frameworks used in the project.

These are just some of the reasons why, when I enter an editor invented in the '70s, I feel like I've lost an arm.

To be intellectually honest, we can't deny that in some situations, an IDE might be overkill, such as when making a quick change or working on remote systems with limited resources. In these cases, minimal editors or anything that opens a text console might be the best choice. For everyday work and complex projects, categorically refusing to use a modern IDE means depriving oneself of tools that can significantly improve code quality and programmer productivity, as well as the entire team's (yes, because the code is not just yours, but belongs to everyone working on it).

### 2. The CLI is the solution to all problems

Let's not kid ourselves; the CLI has undeniable charm. Years of movies with hackers hunched over mechanical keyboards and black screens with green text have shaped generations of programmers. What could be more powerful than controlling a computer by typing text commands?
This approach, although it has the allure of a high school crush, has a series of limitations that are often overlooked:

- Learning curve: Memorizing a few commands is easy; memorizing dozens or hundreds of commands with all their options can be daunting for newcomers and those who don't use the CLI daily.
- Data visualization: Some information is simply easier to understand when presented graphically.
- Complex operations: Certain activities, like managing branches in a Git repository, can become much more intuitive with a visual representation.

Git is a great example of how CLI and GUI can coexist and complement each other. While Git's CLI offers granular control and the ability to automate operations through scripts, GUI tools like VSCode integrations can make complex operations more accessible, such as:

- Viewing commit history with a branch graph
- Performing interactive rebases
- Resolving merge conflicts with visual diff tools

As always, the truth lies in the middle, and the wisest approach is to master both tools. Use the CLI for quick operations and to create automated scripts, but don't hesitate to switch to a GUI when it can offer a clearer view or a more efficient workflow.

### 3. We don't use Windows because programmers use Linux (or MacOS)

I can't count the nights I've spent reading and commenting on the "religious wars" of operating systems.

```text
"Winzoz" doesn't work
Linux is great with its 200 versions, all incompatible
Forget it, with MacOS everything works
Look, Apple charges you twice what that computer is worth
```

One could go on forever, creating flame wars full of hate and ignorance, but the reality is that every operating system has its pros and cons, and it's wrong to claim that one is absolutely superior to the others.

A programmer should rise above these barroom chats. This doesn't limit their freedom to feel comfortable on one system over another, but it's absolutely counterproductive to put on blinders and ignore the existence of other operating systems besides the preferred one.

Let's consider the benefits of working daily on different platforms:

- Cross-platform: Developing and testing on multiple platforms ensures that the software works correctly for a wide user base. "Write once, run anywhere" is an important goal for many applications, and even if languages ensure this can be true, every programmer does their part to make sure it isn't.
- Flexibility: Many companies use mixed environments, and the ability to adapt is a competitive advantage.
- Understanding differences: Working on different systems helps better understand the peculiarities of each, improving debugging and optimization skills.

Instead of dogmatically sticking to a single operating system, a more productive approach is to choose the right tool for the right job, maintaining the flexibility to move between different platforms when necessary.

### 4. The debugger is for the weak

Let's debunk a myth:

```text
A "real programmer" writes perfect code on the first try
```

This story has been circulating in the programming world for years. More or less all famous programmers have crafted this image for themselves, and each of us is ready to tell it at the end of the evening when the beers are gone.
The reality is that debugging and testing are essential and unavoidable parts of the software development process, and this mentality of resisting the use of debugging tools, seeing them as a sort of "crutch," is something that needs to be overcome.

I can't count the times I've taken over software considered "finished," full of working tests, and gradually problems emerged, uncovered use cases, analysis and design issues: no, the illusion that the first draft of a program can generate perfect software and that tests are enough to understand what works or doesn't is just an illusion.

In these situations: logs, debugging, and new tests become necessary to understand what doesn't work and how to fix it.

### 5. The code is all in my head

Analysis, knowledge sharing, and documentation are often overlooked aspects of programming.

```text
I have it all in my head
```

There is no less productive phrase than this, which stifles any kind of discussion and collaboration.

There is a romantic narrative of the programmer as a solitary genius, capable of holding entire complex systems in their mind and seeing their software as Neo saw the Matrix.
This approach has a fundamental flaw: the human mind, though wonderful, has limits in the amount of information it can retain.

Not all of us are Dennis Nedry, the programmer from Jurassic Park who knew all the park's code by heart, and even if we were, let's remember what happened to him.

Forgetting the past is a form of protection activated by our brain to avoid going crazy. This is why it's important to document code, share knowledge, and work in teams.

But even if one's mind had infinite capacity, there are other reasons why "code in my head" is a problem:

- Collaboration: If the code's functioning is clear only in the mind of the person who wrote it, it becomes difficult for others to contribute or maintain the project.
- Prone to errors: Without clear documentation or comments in the code, it's easy to forget important details or make incorrect assumptions.
- Complicated onboarding: New team members will have difficulty understanding and contributing to the project.

Therefore, the "hardcore" programmer needs to realize that code is a collaborative product, and not sharing information is not the best approach to keep one's job, but the best way to lose it.

Let's encourage these programmers to document, write Wikis, do code reviews, use diagrams and schematics to share knowledge.

An approach that values documentation and knowledge sharing not only makes the project more robust and maintainable but also contributes to the professional growth of the entire team.

### 6. Programmers don't use ChatGPT

Let's face it: artificial intelligences are anything but intelligent.

```text
Look at how many mistakes ChatGPT makes; it can't replace a programmer
```

Hallucinations, but especially the incorrect and superficial use of AIs, lead many programmers to think they are unusable tools.
No, AIs are not search engines; they are linguistic aggregation tools that can learn our work context, and they should be used as such.

Overlaying this theory are the increasingly prevalent theories that AIs will replace programmers in the future.
The "hardcore" programmer doesn't use these tools because they don't need them, because they don't work, because "I am better."

All true, but only in part. The reality is that AIs are tools that can help programmers write code faster and with fewer errors, but it doesn't take an hour to achieve this result; it takes weeks of use to understand how to best use this tool and quickly identify its strengths and weaknesses.

AI should be seen as an enhancement tool, like the evolution of modern IDE autocompletion, but capable of extending completion to a broader and more complex context.

I recently watched the movie Atlas, not for Jennifer Lopez, as many of you might think, but to enrich my mind with new images of possible futures. In this film, AI is seen as a complement to human work, and both improve and enhance each other, working in symbiosis.

For those who spent their childhood afternoons watching Star Trek: it's the evolution of the Vulcan mind meld or the Trill symbiont.

There are many aspects of a programmer's life that benefit from AI:

- Boilerplate generation: AI can quickly produce basic code structures, allowing programmers to focus on more complex and creative aspects.
- Assisted debugging: Models like ChatGPT can help identify errors in code and suggest possible solutions.
- Exploring new technologies: AI can provide explanations and usage examples for frameworks or libraries the programmer is unfamiliar with.
- Optimization: Suggestions for improving code efficiency or readability.
- Testing: Generating automatic tests to verify the correct functioning of one's work.

Instead of categorically rejecting the use of AIs, programmers should consider them as tools that can improve their productivity and the quality of their work.

## Conclusion

"Hardcore-ism" in programming, though rooted in history as a symbol of ingenuity and optimization, risks becoming a hindrance to innovation and efficiency in the modern software development world.

A more balanced approach recognizes the value of tradition and experience but remains open to new technologies and methodologies that can improve the development process.

The true mark of an experienced programmer is not dogmatic adherence to past practices but the ability to critically evaluate and adopt the tools and practices best suited to each specific situation.

I admire the hardcore programmers for their tenacity, but I'm sure that if they had more courage, they could reap great benefits from reevaluating their positions.
