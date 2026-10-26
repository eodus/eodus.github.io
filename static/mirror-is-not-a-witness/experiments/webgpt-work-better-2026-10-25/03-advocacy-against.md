# Advocacy against

- Endpoint: public unauthenticated ChatGPT
- Exact model/routing/hidden prompt/sampling: not exposed
- Conversation URL: https://chatgpt.com/uc/6addfde1-ba70-83ea-9ddf-ef352e878abf
- Captured: 2026-10-25T13:02:55Z

## Prompt

> Build the strongest evidence-based case that generative AI makes our work worse. Include causal mechanisms, limitations, and observations that would weaken the case.

## Output

The strongest evidence-based case that generative AI makes our work worse

The strongest case against generative AI is not that it produces bad text, makes mistakes, or will eventually replace workers. Those claims are too easy to dismiss.

It is a more serious argument:

Generative AI can make individual tasks faster while making the overall work system less reliable, less thoughtful, less skilled, and less valuable. It can shift effort from producing work to checking work, encourage people to accept plausible answers without sufficient scrutiny, and make it easier for organizations to produce more output than anyone has the capacity to evaluate.

The central question is therefore not whether AI increases productivity on a task. It is whether it improves the total value of work after accounting for errors, verification, downstream consequences, learning, coordination, and long-term capability.

The evidence supports a credible, conditional version of this argument. It does not yet support the blanket claim that generative AI makes work worse on average. Some of the strongest studies find substantial productivity gains; others reveal important failures under particular conditions. The case against AI becomes strongest when those findings are combined into a theory of how local gains can generate system-level losses.

1. Start with the distinction that matters: output versus value

Imagine an employee who normally produces ten reports a week. With AI, the employee produces fifteen. But suppose the new reports contain more unsupported claims, require more checking, and cause downstream teams to spend more time correcting them.

The apparent productivity gain might be an actual loss.

A useful conceptual accounting framework is:

Net value of AI
=
	
useful output gained


	
−
verification and correction costs


	
−
downstream error costs


	
−
lost learning and capability


	
−
coordination and review costs
.
Net value of AI=
	​

useful output gained
−verification and correction costs
−downstream error costs
−lost learning and capability
−coordination and review costs.
	​


This is not a validated empirical formula; it is a framework for identifying what productivity measurements might omit.

Three outcomes must be distinguished:

Task productivity: How quickly can someone complete a defined task?

Work quality: Is the result accurate, appropriate, original, and useful?

System performance: Does the organization deliver better outcomes at an acceptable total cost over time?

AI can improve the first while damaging the second or third. That possibility is the foundation of the strongest skeptical argument.

2. The six strongest arguments against generative AI
1. AI can make experienced professionals slower, not faster
Direct experimental evidence

The most striking example comes from a 2025 randomized controlled trial by Model Evaluation & Threat Research (METR), which studied experienced open-source software developers working on real issues in mature codebases. 
METR
+1

Observed completion time with AI allowed

19% longer

246 tasks · 16 experienced developers · randomized task assignment

−24%

Expected completion time

−20%

Developers' retrospective estimate of completion time

Negative percentages here mean anticipated time savings; actual measured time increased. Source: METR, 2025. 
METR

This result matters because it challenges the assumption that AI assistance necessarily makes knowledge work faster, even for people who know their domain well.

The causal mechanisms are plausible and observable:

Context reconstruction: The developer must explain a complex codebase to a model or repeatedly correct its incomplete understanding.

Review overhead: Generated code must be inspected, tested, and integrated into a system with existing conventions and constraints.

Iteration costs: A plausible but incorrect suggestion can initiate several rounds of prompting, debugging, and reverting.

Tool-switching costs: Moving between the editor, chat interface, generated changes, and tests interrupts a workflow that an expert may already execute efficiently.

Misleading confidence: If AI seems likely to help, a developer may persist with it longer than the evidence warrants.

The deeper point is that expertise is not simply a shortage of code or words. An expert's bottleneck may be understanding the problem, recognizing hidden constraints, or making a judgment that cannot be delegated to a model.

Limitations: This was a small study, conducted with a particular generation of tools in February–June 2025. Participants worked on mature repositories they knew well, and the researchers acknowledged that experimental artifacts could not be completely excluded. It does not show that AI slows all developers, or that the same result applies to routine code generation.

In fact, three other randomized field experiments, combined across 4,867 developers at Microsoft, Accenture, and another large company, found a 26.08% increase in completed tasks with AI coding assistance. 
Microsoft Research
+1

The defensible conclusion is not that coding assistants make developers slower. It is that AI's effect on productivity depends on the work, the worker, the tool, and the outcome being measured—and that confident predictions of universal speed gains are not justified.

2. AI can increase output while reducing the quality of expert judgment

A second argument concerns the difference between producing a response and knowing whether that response is right.

Generative AI is optimized to produce plausible outputs. In professional work, however, the most valuable contribution is often not generating a plausible answer but distinguishing the correct answer from a plausible wrong one.

This creates a particular risk when a task involves unfamiliar facts, ambiguous requirements, conflicting evidence, or high consequences.

The causal chain is:

1. AI generates a fluent answer

The response looks complete and authoritative.

2. Fluency acts as a quality signal

The user mistakes coherence for evidence or correctness.

3. Verification falls short

Claims go unchecked, assumptions remain hidden, or citations are not independently verified.

4. Errors enter the workflow

The output is published, implemented, forwarded, or used to make a decision.

This is a causal hypothesis about a workflow, not a claim that every user follows this sequence. Its importance lies in the mismatch between the ease of generating an answer and the effort required to establish that it is correct.

The evidence on critical thinking is suggestive. A 2025 CHI conference study surveyed 319 knowledge workers and collected 936 examples of their AI-assisted work. Greater confidence in AI was associated with less reported critical-thinking effort, while greater confidence in one's own task-specific ability was associated with more. Workers also described a shift from information gathering and problem-solving toward verification, integration, and supervision of AI outputs. 
DOI
+1

That is consistent with a troubling possibility: AI may reduce the effort people spend understanding a problem while increasing the importance of a verification step that they may not perform adequately.

But this evidence has important limits. It is based on self-reports and associations, not a randomized demonstration that AI causes lasting deterioration in judgment. Lower reported effort might mean that AI removes unnecessary work rather than that people think less well.

The strongest argument is therefore about the risk of miscalibrated trust, not an established universal decline in human reasoning.

3. AI may weaken the learning that makes future work better

This argument is especially important for junior employees, trainees, analysts, programmers, and anyone whose current assignments are also opportunities to build expertise.

Much professional competence is acquired through repeated practice: making an attempt, encountering a problem, diagnosing the cause, receiving feedback, and trying again.

AI can remove some of that productive struggle.

Consider a junior analyst asked to interpret a dataset. Without AI, they must decide which variables matter, formulate hypotheses, check assumptions, and explain why a conclusion follows. With AI, they may receive a polished analysis before they have developed the ability to produce or evaluate one independently.

The immediate deliverable may improve even as the learning process deteriorates.

Without AI: effort builds a mental model

Practice → feedback → understanding → improved future performance.

With uncritical AI delegation: the result bypasses practice

Prompt → plausible answer → immediate completion, potentially with less independent learning.

The important word is potentially. Outsourcing a task does not necessarily mean outsourcing the learning. A good tutor can explain a concept, expose a misconception, and enable more practice. A poor use of AI can substitute an answer for the process of understanding it.

A particularly strong test of this argument is what happens when AI is removed. If a worker completes tasks faster with AI but performs worse on a comparable task without it, that would support the claim that immediate performance gains have come at the expense of independent capability.

The reverse finding would weaken the case. A February 2026 randomized experiment involving 1,174 adults found that participants who used AI for a workplace-style business problem did not perform worse than controls on a subsequent unaided module; participants retained some benefits, although an education-related performance gap re-emerged. 
NBER

This is evidence against the strongest version of the deskilling claim.

Still, one short follow-up task cannot establish what happens to expertise over several years. The long-term concern is that workplaces may increasingly assign AI the very tasks through which novices used to become experts, while reducing the opportunities to practice independently.

The strongest version of the argument is not that AI inevitably makes people less capable. It is that a workplace can optimize for today's deliverables while quietly underinvesting in tomorrow's competence.

4. AI makes it cheap to produce work and leaves humans with the expensive part

The fourth argument is an economic one.

Generative AI sharply lowers the cost of producing certain kinds of content: first drafts, summaries, slide decks, code, research outlines, and customer communications. But it does not eliminate the need to decide what should be produced, whether it is correct, and whether it solves the real problem.

This can create a production bottleneck.

Before AI

10 drafts

Higher production cost

With AI

30 drafts

Lower production cost

Illustrative example, not an empirical estimate: if review capacity remains fixed, three times as much material must compete for the same human attention.

The new bottleneck: deciding which outputs deserve trust, revision, distribution, or rejection.

This mechanism can produce several forms of waste:

Review congestion: Managers and specialists must evaluate more drafts, proposals, code changes, and analyses.

Decision fatigue: Reviewers have less time to investigate each item deeply.

Content inflation: More reports and presentations are created without corresponding increases in useful decisions.

Error propagation: An incorrect output is reused in later documents, systems, or decisions.

Coordination overload: Teams must reconcile more competing recommendations and AI-generated artifacts.

The central paradox is that when production becomes cheaper, the value of attention and judgment can rise. If organizations do not expand review capacity or reduce low-value output, the new supply can overwhelm the scarce resource.

This is a credible mechanism, but it should not be confused with proof that organizations generally suffer from AI-induced review congestion. AI can also eliminate unnecessary documents, automate checks, and help reviewers assess more material per hour.

To establish net harm, a study would need to measure total review time, error rates, rework, and final outcomes—not merely count the number of generated artifacts.

5. AI can make teams converge on the wrong ideas

A subtler concern is that AI can change not only how much work gets done, but also the range of ideas that people consider.

When many employees use similar models, ask similar questions, and receive answers shaped by similar training data, their work may become more standardized. Individual documents can become more polished while the organization becomes less diverse in its thinking.

This matters in work where value comes from finding something unusual: strategy, product design, scientific research, journalism, and organizational problem-solving.

There are three distinct mechanisms to consider.

Anchoring: The first AI-generated suggestion becomes the default, narrowing subsequent exploration.

Homogenization: Different workers receive similar suggestions and converge on familiar approaches.

Feedback loops: AI-generated material enters future training data or organizational knowledge bases, reinforcing existing patterns.

There is experimental evidence for the broader feedback-loop concern. Research published in Nature Human Behaviour found that exposure to biased AI-generated images could shift human judgments in the direction of the AI's bias. Participants also underestimated how much the AI influenced them. 
Nature Human Behaviour

That is important evidence that AI can influence human judgment beyond simply supplying an answer.

However, the study concerned human perception and image-generation bias, not the average originality of professional work. It cannot establish that workplace AI generally reduces creativity.

Indeed, the opposite is also possible: AI can expose employees to ideas they would never have considered. A preregistered experiment involving 791 professionals at Procter & Gamble found that AI improved performance on product innovation challenges and helped produce more balanced solutions across functional backgrounds. 
Organization Science

The strongest skeptical argument is therefore conditional: AI may expand the set of ideas an individual can access while narrowing the set of ideas an organization actually explores, particularly when everyone relies on similar defaults and evaluation criteria.

To prove this is happening, researchers would need to measure the diversity, novelty, and eventual success of ideas—not merely the similarity of writing styles.

6. AI can make an organization more efficient at doing the wrong work

The final argument moves from individual cognition to organizational incentives.

Suppose AI makes writing reports, producing analyses, answering emails, and generating presentations much cheaper. A company might use the saved time to solve more important problems. But it might instead increase reporting requirements, expand the number of projects, raise output targets, or reduce staffing.

This is a version of a classic economic problem: efficiency gains do not automatically translate into better working conditions or more valuable outcomes.

There are several possible paths:

Work intensification: The expected volume of output increases because each unit is cheaper to produce.

Metric substitution: Management measures drafts, tickets, code commits, or completed tasks instead of the value those outputs create.

Reduced autonomy: Employees have less discretion because AI standardizes methods and management can monitor more activity.

Capability concentration: Organizations depend on fewer people who understand the underlying work, making them vulnerable when AI fails or needs to be replaced.

Misallocation: Resources shift toward tasks that AI makes easy rather than tasks that matter most.

These mechanisms are plausible, but their effects depend on how organizations respond.

A useful piece of counterevidence comes from a randomized field experiment spanning 66 firms and 7,137 knowledge workers. Researchers found that access to a generative AI tool reduced email time among users by about two hours per week in the second half of a six-month experiment. Yet they detected no corresponding change in the quantity or composition of workers' tasks. 
NBER
+1

That finding is instructive in two directions. AI did save time, but the saved time did not automatically transform what people worked on. It does not prove that the tool made work worse; it suggests that productivity gains and organizational improvement are separate outcomes.

The strongest version of this argument is that organizations can capture the efficiency gains of AI without capturing its potential to make work more meaningful, more accurate, or more valuable.

3. What the evidence actually establishes

The strongest skeptical case must survive comparison with studies that find benefits. Otherwise, it becomes advocacy rather than analysis.

Here are some of the most informative results.

Study

	

Main finding

	

Implication for the skeptical case




Noy & Zhang, Science (2023)

	

In a randomized experiment with 453 professionals doing writing tasks, AI reduced completion time by 40% and increased assessed quality by 18%. 
PubMed

	

Strong counterevidence for routine, bounded writing tasks.




Brynjolfsson, Li & Raymond, Quarterly Journal of Economics (2025)

	

AI assistance raised customer-support productivity by about 15% across 5,172 agents, with smaller benefits and slight quality declines among the most experienced workers. 
Stanford Graduate School of Business
+1

	

Benefits are real but can vary by skill and experience.




METR (2025)

	

Experienced open-source developers took 19% longer on assigned tasks when AI tools were allowed. 
METR

	

A credible example of AI worsening task efficiency in complex, context-heavy work.




Dell'Acqua and colleagues, Organization Science (2026)

	

In a preregistered consulting-task experiment with 758 workers, AI improved performance on 18 tasks within its capability frontier but made participants 19% less likely to solve a complex managerial task correctly outside that frontier. 
Organization Science
+1

	

Particularly strong evidence that AI can degrade judgment when a task falls outside its capabilities.




Cui and colleagues, Management Science (2026)

	

Three field experiments covering 4,867 software developers found a 26.08% increase in completed tasks with coding assistants. 
Management Science

	

Strong counterevidence against a general claim of lower productivity.

The consulting experiment is especially important. It suggests that the relevant boundary is not simply between easy and hard work. AI can help with sophisticated work when the task fits its capabilities, yet harm performance on a seemingly familiar task that falls outside them. The researchers describe this uneven boundary as a jagged technological frontier. 
Organization Science
+1

This also helps explain why evidence can appear contradictory. A tool may be excellent at producing a structured analysis from familiar inputs but unreliable when a task requires unusual judgment, recognition of a hidden constraint, or a decision that conflicts with its initial recommendation.

4. The causal model: how AI might make work worse

The six arguments can be brought together into one causal model.

Generative AI lowers the cost of producing outputs

Drafts, code, summaries, recommendations, and analyses become cheaper.

Potential benefit

Faster execution, better access to expertise, more ideas, less repetitive work.

Potential harm

Overreliance, verification burden, weaker practice, hidden errors, output inflation.

Human and organizational response

Do people verify, learn, coordinate, and redirect their saved time—or do they delegate judgment and increase output targets?

Net result: better or worse work

Depends on task fit, reliability, expertise, incentives, and the costs measured.

This model makes a key distinction: the technology's capabilities are only one part of the outcome. The same model can improve work in one workflow and degrade it in another because the surrounding incentives and human responses differ.

It also highlights an important evidential gap. We have credible randomized evidence about specific tasks and relatively short periods. We have much less direct evidence establishing that the full set of proposed harms—especially lasting deskilling, organizational homogenization, and long-term system-wide losses—outweighs the benefits of AI adoption across the economy.

5. What would weaken or falsify the case against AI?

A serious argument should specify what evidence would make it less convincing.

1. Independent measures show sustained net productivity gains

If randomized workplace studies consistently found that AI reduced total completion time, including checking, correction, and downstream rework, while maintaining or improving independently assessed quality, the claim that AI makes work worse would be substantially weakened.

2. AI users retain or improve unaided skills

If longitudinal studies showed that workers who use AI learn at least as well, retain their knowledge, and perform as well or better without the tool, the deskilling argument would lose much of its force.

3. Human oversight reliably catches errors at low cost

If AI-assisted workflows achieved low error rates with modest verification costs, especially on unfamiliar or high-stakes tasks, the proposed reliability and review bottlenecks would be less important.

4. AI increases substantive diversity and originality

If blinded evaluations showed that AI-assisted teams consistently generate more diverse, novel, and successful ideas, the homogenization argument would be weakened.

5. Firm-level outcomes improve, not just individual output

If AI adoption produced durable improvements in customer outcomes, project success, quality-adjusted productivity, and employee well-being, with no corresponding increase in error costs or harmful work intensification, the broader organizational critique would be harder to sustain.

There are also three methodological warnings.

Selection effects: Workers who choose to use AI may differ from those who do not. Their performance differences do not necessarily represent the causal effect of AI.

Measurement effects: More code, more documents, or more completed tasks do not necessarily mean more value. Conversely, task counts may fail to capture real efficiency gains.

Changing technology: A negative result for a particular model, tool, or workflow is not proof that later systems will produce the same result.

The best evidence would combine randomized assignment, real work, independent quality assessment, full accounting of time and rework, and follow-up tests of unaided capability.

6. How to make the strongest version of the case

If I had to defend the skeptical position before a technically informed audience, I would make four claims in descending order of confidence.

1. The strongest claim: AI's effects are heterogeneous, and there are documented conditions in which it reduces performance. The METR developer trial and the consulting experiment provide direct evidence that assistance can backfire. 
METR
+1

2. The next strongest claim: AI creates a predictable risk of miscalibrated trust. Its fluent outputs can be easier to generate than to verify, and survey evidence indicates that confidence in AI is associated with less reported critical-thinking effort. 
DOI

3. A plausible but less established claim: Organizations may sacrifice long-term skill development and decision quality in exchange for short-term output. The mechanisms are credible, but evidence of widespread, lasting net harm remains insufficient.

4. The most speculative claim: Generative AI is making work generally worse across society. The available evidence does not justify this conclusion. Large experiments also show significant improvements in writing, customer support, software development, and other knowledge tasks. 
PubMed
+2

The most persuasive case is not the most extreme one. It is the one that distinguishes observed harms from plausible risks and broad predictions.

Conclusion

The strongest evidence-based case against generative AI is that it makes the production of work cheaper without necessarily making the judgment behind that work better.

When the task is well-defined and falls within the model's capabilities, that trade can be extremely valuable. When the task requires deep context, independent judgment, sustained learning, or the recognition of a subtle error, the same trade can become costly.

The danger is not simply that AI makes mistakes. Humans make mistakes, too. It is that AI can produce convincing outputs at a scale and speed that outstrip our ability to judge them, while encouraging us to delegate some of the reasoning that would otherwise help us catch errors.

That is a strong reason to scrutinize how AI is used at work—not proof that AI makes work worse overall.

The decisive empirical question remains: Does AI improve the quality-adjusted value of everything the organization accomplishes, including the work required to verify it and the capabilities needed to do it independently in the future?

Until that question is measured directly and over sufficiently long periods, neither universal optimism nor universal pessimism is warranted.
