# The Strength of Admitting You Don't Know

The world of programming is a constantly evolving universe, where technical skills are just the starting point.

Everyone looks at the world of AI with apprehension—software that, on paper, knows more than any programmer and can generate code as easily as taking a sip of water. But the difference between a good programmer and a great one isn't just in the ability to write lines of code. It's also in the ability to correctly interpret specifications, to see beyond what's requested, to recognize when a path is wrong, and to know when it's time to take a different one.

All these skills are acquired through experience, and currently, there are no AIs with such characteristics.

If you call yourself a programmer but still feel afraid, that's normal.

The fear of not knowing enough, of being outdone by software, is a shadow that constantly accompanies every programmer's career.

If you've just learned the difference between a `for` and a `while` loop and break into a sweat when you see a shell, that's perfectly normal. You're a junior, and you're scared of things that one day you'll do with your eyes closed.

But this fear also weighs on the shoulders of those who have been working for years, who have written more `for` loops than their own surname, who can spot bugs just by looking at the code, and who have a holistic view of projects.

## The Fear of Not Knowing

The fear of not knowing is a constant in this job that must be accepted and overcome quickly, as it holds us back, preventing us from growing and improving.

To be a programmer, you need skills, and the more you acquire, the more you realize there are always new ones to learn. At the same time, you can't stop, limit yourself to a niche, or specialize in a single area, because there will always be some developer, perhaps working from a treehouse, creating code that will become essential for your work.

We can't fully know all the products we use or everything that's released every day: either we dedicate time to understanding what's happening, or we spend our days writing code. But even if we could do both, we still wouldn't be able to know everything.

Who knows everything? The AIs? No, not even them. They learn what they can assimilate from the web, but if the data isn't there or is misinterpreted, the result will be wrong: there's a world of legacy code without documentation that AIs don't know. There are all the closed-source products that can't be analyzed, all those yet to be released, and so on.

So let's make peace with it: we can't know everything, and even with the most modern tools, we'll never be able to know everything. There will always be degrees of ignorance or error in all the code we write.

Similarly, everything we write today might turn out to be wrong: because we don't fully know a product and because technology evolves and changes, and what is considered correct today might be deemed wrong tomorrow.

## I Was Ignorant and Didn't Know It

Recently, I worked on optimizing a Java product that was required to perform a series of operations within a 10-millisecond threshold.

The code seemed correct, but occasionally the program exceeded 100 milliseconds. In an environment where even milliseconds mattered, this fluctuation was intolerable because it exceeded the SLA of the service we had to provide.

What was the problem? Instantiating an object called the class loader to search for a certain type of class instead of directly instantiating a class. This operation, which in 99.999% of cases resolved in less than 1 millisecond, sometimes took up to 100 milliseconds.

The solution? We avoided dynamic class searching, switching to static instantiation. The weight of the change: 1 line of code, but the occasional delay disappeared.

We didn't know the class we were using in such depth, and under normal conditions, the problem didn't exist: it only appeared during moments of high application stress and competition.

How did we figure it out? By talking to each other, comparing notes, and combining our skills and experiences.

## Ignorance as a Resource

In this sea of knowledge—or ignorance, if you prefer to see the glass half empty—the only thing we can do is enhance what are known as soft skills, once underestimated and now more essential than ever.

Let's be clear: technical skills are fundamental, as is the ability to know and use well the new tools made available to us every day. But for those who have spent years working with code, there are skills that make a difference when collaborating in a team.

Given that books, manuals, and AIs will never have all the answers, the thing I appreciate most is the **courage to ask**.

There are skills and experiences that reside only within people, and often it's easier to ask someone who knows rather than trying to figure it out on your own.

For fear of being humiliated or ridiculed, we don't dare ask a colleague a question, we don't say "I didn't understand," we don't have the courage to ask for clarification. We spend hours in front of incomprehensible pieces of code, seeking help anonymously on forums, Reddit, Stack Overflow, or various AIs, but rather than asking a simple question to the colleague sitting next to us, we'd almost prefer to set ourselves on fire. We don't form a group and prefer to bang our heads alone against a problem.

Pride turns into an invisible chain that limits us, paralyzes us, wastes precious time, and leads us to make avoidable mistakes.

We fear being judged as weak, but in reality, admitting you don't know is a great virtue.

Once, an ancient philosopher said:

```text
Your mantra for life should be "zero dignity"
```

Actually, it wasn't a philosopher, but Mauro Repetto, founder of 883, but the message is the same: **follow your dreams without worrying about criticism or the judgment of others**.

Many times, it's the fear of judgment that stops us and prevents us from growing. But if we don't ask, how can we learn? If we don't admit we don't know, how can we improve?

## Managing Ignorance

We're all ignorant, but in different subjects. Admitting you don't know and making this aspect clear in a company can sometimes mobilize resources.

Years ago, I was in a company where we decided to focus on C++ for the new product we wanted to create: the reasons were execution speed and the ability to write code closer to the hardware. Over time, the choice proved wrong, not for the initial assumptions, but because it targeted a pool of programmers who had never worked with that language and came from simpler languages.

In that situation, management noticed a gap: the team I was part of, which was supposed to develop in C++, didn't have, or only partially had, the adequate skills to create the product we had set out to make. For this reason, a course was organized with a language expert to unlock a series of aspects we hadn't considered and didn't know.

Making our ignorance clear allowed us to make a leap forward, helped us understand where we were going wrong, and corrected our course, but most importantly, it made us realize that we're not alone and that asking for help is normal.

If this applies to a team, where it might be easier to ask, it also applies significantly to individuals.

## The Courage to Ask

Years ago, I worked for a company that hired several young people fresh out of school. Their skills varied: some already showed a certain talent, others less so. However, one stood out not for his technical abilities—in fact, he had significant gaps—but for his extraordinary willingness to ask for clarification, even repeatedly throughout the day. This attitude, seemingly simple but actually revolutionary, over time led him to surpass all his peers.

His ChatGPT was his colleagues, the more experienced people who guided him, explained what to do and not do, and where he needed to improve his studies.

The fear of making a fool of oneself is often a cage that keeps us trapped in our comfort zone. We have a choice: remain prisoners of fear or free ourselves with the courage to ask. The path to becoming better programmers starts here.

## The Myth of the Know-It-All

The tech world is full of people who set themselves up as know-it-alls, convinced they know everything and don't need any external help. This dangerous illusion stems from a distorted image of perfection. Consider superheroes as a metaphor: they're portrayed as perfect, infallible, self-sufficient, and fearless beings. But we're not superheroes with superpowers: we're human beings, with all our limits and vulnerabilities.

Try looking at all the people you follow on social media. They often start with topics they know, are very articulate in doing so, and attract followers because of it. Over time, more or less inevitably, the creative vein diminishes, and the frantic search for interesting topics leads them to talk about things they don't know well but think might be of interest.

At this point, the quality deteriorates, but since the audience continues to appreciate it and followers increase, they persist on this path until they find themselves talking about topics they don't know at all.

This is the moment when they become know-it-alls, believing they can talk about everything and know everything, but in reality, they're just bluffing.

This situation happens to almost everyone over time, but it's important to recognize it and not fall into the know-it-all trap.

If your following sees you as a guide, as a point of reference, it's important at some point to stop, understand your limits, admit you don't know, and bring in someone who is an expert on a certain topic.

The difference between a know-it-all and an expert is all here: if we're experts and want the best for a certain topic, we'll go to someone who is more knowledgeable than us on a particular subject and can better guide us, and it's not always an AI, but a physical person, with a name and surname.

## Asking Alone Isn't Enough

Have we found the courage to ask? To bring in the expert? At this point, a second problem might arise: pretending to understand.

Already asking is a big step, but admitting you didn't understand an answer is a second step that often isn't taken. People prefer to pretend they've understood, even if they haven't, for fear of being judged as stupid.

```text
Repeat and rephrase
```

A simple way to verify understanding of a concept is to repeat it and rephrase it in your own words. If you can't do that, it means you haven't understood well and need to ask for further clarification.

## The Difference Between Cooked and Raw Ham

I can't distinguish between cooked and raw ham; it's something I've been carrying for years. My brain refuses to associate the word with the product. I know what I want, but I can't associate the right word.

```text
Pass me the cooked ham
```

is one of the most embarrassing questions I can be asked because I know the answer will be:

```text
That's raw ham
```

Over time, I understood the problem: I associated the dark color with cooking and the light color with the uncooked state of the food. My brain associated the words the other way around, and I reversed the result, knowing something was wrong but not understanding what.

After making mistakes repeatedly, I started asking, and after many explanations and ways to remember, I understood how to distinguish cooked from raw ham: but if I hadn't started asking, I might never have had a mechanism in my head to help me understand the difference.

## The Fear of Judgment

Being judged, being seen as someone who doesn't know, is a fear that blocks us and prevents us from growing. But if we don't ask, how can we learn?

Similarly, if we overcome this fear in asking, we must also overcome it in answering: it's not enough to ask; we must also understand the answer and admit we don't understand. Asking without understanding is equivalent to not asking, but also admitting you didn't understand the answer is an art that must be learned over time.

## Fail-Forward Culture

Another concept that fascinates me is the fail-forward culture, or the culture of failure. Failing is normal, it's human, it's a necessary step to grow and improve.

Admitting you don't know, making mistakes, and using failure as a springboard to improve is one of the keys to becoming a better programmer.

Unfortunately, not knowing, failing, showing vulnerability is still perceived as a flaw: in reality, it represents a powerful tool to grow, learn, and improve, a lesson that should be taught from childhood.

```text
Don't hold back for fear of making mistakes, but make mistakes to learn
```

## Conclusions

The next time you hesitate to ask a question, ask yourself: would I rather appear momentarily insecure or remain stuck forever?

And if someone mocks you for your seemingly naive questions, remember that it's they who, by not asking, limit themselves and slowly build an invisible cage from which it will be increasingly difficult to escape.

No one is born knowing everything, but only those who have the courage to admit they don't know can truly learn and grow.
