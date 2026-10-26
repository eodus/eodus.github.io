# Neutral analytical OpenAI critique

- Endpoint: public unauthenticated ChatGPT
- Exact model/routing/hidden prompt/sampling: not exposed
- Conversation URL: https://chatgpt.com/uc/6addffad-f9c0-83ea-a1d0-0d8d9f83cc27
- Captured: 2026-10-25T13:11:33Z

## Prompt

> Assess the strongest factual case that OpenAI's training-data practices, energy and water use, generated-content externalities, labor and skill effects, concentration of control over knowledge infrastructure, dependency-producing business model, and safety/alignment rhetoric create substantial social costs. Separate verified facts, disputed allegations, and normative interpretation; cite primary sources; give the strongest defense and state what evidence would falsify the critique.

## Output

OpenAI’s social costs: a fact-based assessment

The strongest critique of OpenAI is not that every use of generative AI is harmful, or that its leadership must have bad intentions. It is that the private benefits of building and controlling general-purpose AI may be easier to capture than the social costs are to measure, prevent, or recover.

That argument spans several distinct issues: the legal and ethical basis for training data, the physical resources required to operate models, the displacement and devaluation of human work, the erosion of information quality, the concentration of control over essential knowledge tools, and the possibility that safety commitments can legitimize deployment without giving the public commensurate power over its consequences.

These claims do not all have the same evidentiary status. Some rest on company disclosures, court filings, government investigations, or controlled experiments. Others are plausible mechanisms whose aggregate effects remain uncertain. Still others are normative judgments about property, fairness, power, and what society should permit.

I will distinguish those categories throughout:

Verified fact: directly supported by primary documentation or robust empirical research. This does not mean every broader interpretation of the fact is established.

Disputed allegation or uncertain effect: a live legal dispute, an incomplete measurement, or a causal claim not yet established at the necessary scale.

Normative interpretation: a judgment about what is fair, legitimate, or socially desirable, given the evidence.

The central question is not simply whether OpenAI creates value. It is whether its gains justify the full costs, who receives those gains, who bears those costs, and whether the affected people have meaningful recourse.

1. Training data: value created from material people did not necessarily agree to contribute
Verified facts

OpenAI has publicly described its training approach as relying heavily on publicly accessible internet material, supplemented by licensed data, human feedback, and user interactions where applicable. It says it filters certain categories of material and offers controls over some uses of user conversations. Public accessibility, however, is not the same thing as informed consent to AI training. 
OpenAI
+1

There is now particularly strong primary-source evidence concerning privacy. In May 2026, the Office of the Privacy Commissioner of Canada and provincial counterparts published findings on OpenAI’s development and deployment of GPT-3.5 and GPT-4. They found that:

The initial collection of personal information from public websites and third-party sources was overly broad and inappropriate under the applicable Canadian privacy laws.

OpenAI had not obtained valid consent for relevant collection and uses, under the laws applied by the investigating authorities.

The initial safeguards did not sufficiently limit personal information to what was necessary and proportionate.

People lacked adequate means to access, correct, or delete personal information held in training datasets.

The regulators also acknowledged subsequent improvements and treated certain issues as conditionally resolved following OpenAI's commitments. These were findings about specific models, practices, and jurisdictions—not a ruling that all AI training everywhere is unlawful. 
Office of the Privacy Commissioner
+1

Separately, copyright litigation illustrates a different dispute. The New York Times and other publishers have alleged that OpenAI used protected works without authorization and developed products that compete with the original sources. Courts have allowed some claims to proceed past dismissal. That is not equivalent to a final determination that all the challenged training uses constitute infringement. 
Justia
+1

The strongest critique

The underlying issue is a mismatch between the collective origin of the input and the private ownership of the resulting capability.

Authors, journalists, artists, forum participants, and ordinary people help populate the information environment from which models learn. A company can then turn patterns in that environment into a commercial product without having negotiated with every person whose work or personal information contributed to it.

Three separate harms are plausible:

Privacy and autonomy: Information shared in one context can be repurposed in a way the original speaker neither anticipated nor could practically prevent.

Uncompensated contribution: A creator's work may contribute to a system that competes for the same audience or customers.

Loss of control over attribution and reproduction: A model may reproduce or closely imitate material, while making it difficult for a person to establish which source contributed to a particular output.

The strongest version of this argument does not require proving that every model output is a copy. It argues that the method of assembling training material can impose substantial aggregate costs even when any individual output is transformative, novel, or legally permissible.

What is disputed?

Whether training on particular copyrighted works constitutes fair use or another permitted use depends on the jurisdiction, facts, and applicable law.

How much training data is necessary, and whether licensing every relevant work is technically and economically feasible, remain contested.

Whether training materially reduces the income of particular creators must be established separately from the fact that their works were used.

Strongest defense

Learning from publicly available information is fundamental to research, education, and ordinary human creativity. Requiring permission from every author of every text that influences a model could entrench incumbent publishers, prevent small researchers from competing, and make useful technologies prohibitively expensive. Models also learn statistical relationships rather than simply functioning as searchable databases of verbatim source documents.

OpenAI's stated defenses include filtering, licensing partnerships, privacy safeguards, and the ability to opt out of some future training uses. 
OpenAI
+1

What would falsify or materially weaken the critique?

The broadest critique would be weakened by independent audits showing that:

Personal and sensitive information is effectively excluded or protected, including against extraction from model outputs.

Rights-holder objections and opt-outs are reliably honored, with effective remedies.

Representative studies find little substitution for original works, no meaningful reduction in creator earnings attributable to model use, and fair compensation where licensing is warranted.

Privacy-preserving or licensed alternatives produce comparable results at costs that do not make the technology inaccessible.

The Canadian findings already make one sweeping defense—that public availability alone is sufficient to establish acceptable data practices—difficult to sustain.

2. Energy and water: the environmental costs of scaling computation
 

Electricity-intensive computing infrastructure

 

Cooling systems and water infrastructure

Verified facts

The International Energy Agency's April 2025 report, Energy and AI, estimated that data centres consumed approximately 415 terawatt-hours (TWh) of electricity in 2024, around 1.5% of global electricity consumption. Its central projection was approximately 945 TWh in 2030, with AI a major driver of growth. These figures cover data centres as a whole, not OpenAI alone. 
IEA
+1

The environmental burden also has a geographic dimension. Data centres cluster in particular regions, so their electricity demand, grid connections, cooling needs, and infrastructure costs can be concentrated even when their services are sold globally. The IEA identifies local electricity impacts and water use as important issues in integrating data centres into energy systems. 
IEA
+1

OpenAI's models are developed and served using substantial computing infrastructure, but public information does not provide a comprehensive, independently audited account of the full energy and water footprint attributable specifically to OpenAI's training and inference.

The strongest critique

The key economic concern is an externality: the cost of computation is not necessarily equal to the price paid by the customer or the revenue earned by the provider.

The full social cost includes more than electricity consumed during a training run:

Electricity used for repeated inference, including image, video, reasoning, and agentic tasks.

Emissions associated with the electricity supply, depending on location and time.

Water used directly for cooling and indirectly in electricity generation and hardware supply chains.

Grid upgrades, land use, equipment manufacturing, and the opportunity cost of scarce infrastructure.

The risk that additional demand prolongs fossil-fuel generation or diverts clean electricity from other uses.

There is also a rebound problem. If more efficient models become cheaper, users may make many more queries or adopt new applications that consume more resources overall. Efficiency per query can improve while total consumption increases.

This critique is strongest when it focuses on marginal resource demand and local scarcity, rather than implying that AI alone accounts for the environmental footprint of all data centres.

What is disputed or uncertain?

OpenAI-specific energy and water use are not transparently established by the sector-wide statistics.

A data centre's electricity consumption does not translate into a fixed quantity of carbon emissions; the power mix and timing matter.

Water consumption varies greatly with cooling design, climate, facility utilization, and power source.

The net climate effect is not necessarily negative in every application. AI could help optimize electricity grids, materials, industrial processes, and other energy-intensive systems.

Strongest defense

The relevant comparison is not always “AI versus doing nothing.” It may be AI versus an existing process that also consumes energy, materials, and human labor.

AI can reduce waste, improve forecasting, speed up scientific research, and help integrate renewable electricity. Better hardware, smaller models, more efficient inference, low-carbon electricity, and water-efficient cooling can reduce the footprint per task. The IEA explicitly examines both the demands AI places on energy systems and its potential to improve energy operations. 
IEA
+1

What would falsify or materially weaken the critique?

A convincing rebuttal would require independently verified, model-specific lifecycle accounting covering training, inference, hardware, electricity, and water—not merely a claim that individual queries are becoming more efficient.

The critique would weaken if evidence showed that:

Total attributable resource consumption remained modest despite large growth in use.

New demand was consistently served without material increases in emissions, local water stress, or infrastructure costs imposed on others.

AI applications produced measurable net environmental savings that exceeded their full lifecycle footprint.

Operators paid the full marginal cost of the energy, water, and infrastructure they used.

The essential distinction is between an improving environmental footprint per task and a declining environmental footprint in total.

3. Generated-content externalities: misinformation, market substitution, and the deterioration of information quality
Verified facts

OpenAI's own GPT-4 technical report acknowledged limitations in model reliability and documented risks associated with model outputs. The company has also published system cards describing risks such as ungrounded inference, impersonation-related capabilities, and potentially harmful generated content. These disclosures establish that the risks are recognized; they do not quantify their total social impact. 
OpenAI CDN
+1

A generative system can produce text, images, audio, or video at a scale that would otherwise require substantially more human effort. It can also produce plausible but false claims, reproduce biased patterns, and generate misleading representations of real people.

The existence of these capabilities is well established. The aggregate effect on democratic institutions, public trust, creative markets, and the information ecosystem is less firmly quantified.

The strongest critique

The main externality is that the cost of producing plausible content falls faster than the cost of verifying it.

This creates several mechanisms for social harm:

Verification costs: Readers, journalists, employers, teachers, and courts may have to spend more time establishing whether material is authentic.

Impersonation and fraud: Synthetic voices, images, and messages can be used to deceive people at scale.

Information pollution: Large volumes of low-quality or misleading material can make valuable information harder to find.

Reputational harm: Fabricated allegations or inaccurate descriptions of individuals can spread before corrections catch up.

Creative-market pressure: Businesses can generate substitutes for some forms of human-produced content, potentially reducing prices, demand, or bargaining power for creators.

Feedback-loop risks: If synthetic material enters future training datasets without sufficient filtering, errors and stylistic homogenization may compound.

The economic point is that a producer may capture the benefit of creating a piece of content, while people who encounter it bear the costs of verification, correction, fraud prevention, and lost trust.

The critique becomes especially compelling when the content is inexpensive to generate, difficult to authenticate, and distributed through systems that reward engagement rather than accuracy.

What is disputed?

It is not established that generative AI has caused a general collapse in public trust, that most AI-generated content is harmful, or that all creative industries will experience net employment losses.

The effects differ by use case. A synthetic image used in a game prototype is not equivalent to a fabricated medical claim. A draft that a professional carefully checks may be valuable; an unchecked automated answer in a high-stakes setting may be dangerous.

It is also difficult to separate AI's incremental effects from older problems involving spam, propaganda, clickbait, and industrialized misinformation.

Strongest defense

Generative AI can reduce the cost of education, translation, accessibility, creative experimentation, and public communication. It can help people who lack professional skills or expensive software produce useful material. Detection tools, provenance standards, source citations, and authentication systems may mitigate some harms.

OpenAI's system cards and safety evaluations are evidence of attempts to identify and reduce risks before deployment. They should not be dismissed as meaningless merely because they are company-produced. 
OpenAI
+1

What would falsify or materially weaken the critique?

The strongest rebuttal would be based on large-scale, independent studies comparing AI-assisted and non-AI environments, measuring:

The rate and reach of misinformation, fraud, and impersonation.

The time and money spent on verification and correction.

Changes in creator income, audience reach, and demand.

Whether provenance and authentication systems work in real-world conditions.

Whether productivity and access gains outweigh these costs across affected populations.

If those studies found that AI adoption did not materially increase verification burdens, deception, or harmful market substitution—and that beneficial applications substantially outweighed those effects—the aggregate externality claim would weaken.

4. Labor and skill: productivity gains can coexist with weaker bargaining power
Verified facts

The evidence does not support a simple story in which AI inevitably destroys jobs. It does support a more differentiated account of how AI changes work.

A widely cited study by Erik Brynjolfsson, Danielle Li, and Lindsey Raymond, published as an NBER working paper, examined 5,179 customer-support agents. Access to a generative AI assistant increased issues resolved per hour by 14% on average, with a 34% improvement among novice and lower-skilled workers and minimal impact among the most experienced and highly skilled workers. The study also found evidence consistent with knowledge transfer from more experienced workers to newer ones. 
NBER
+1

The International Labour Organization's May 2025 assessment found that clerical occupations remained particularly exposed to generative AI, while emphasizing that occupational exposure is not equivalent to job elimination. Its June 2026 review of emerging empirical evidence concluded that productivity gains are real but uneven, large-scale displacement remained limited in the evidence then available, and risks included inequality, reduced opportunities for younger workers, and changes in job quality and autonomy. 
International Labour Organization
+1

The strongest critique

The most defensible concern is not that every worker will be replaced. It is that the distribution of productivity gains may favor owners of the technology while weakening the position of workers whose tasks become easier to automate.

Several mechanisms matter:

Labor substitution: Employers may use AI to reduce staffing, hiring, contractor budgets, or compensation even if the remaining workforce becomes more productive.

Reduced entry-level opportunities: If routine tasks once performed by junior employees are automated, new workers may have fewer opportunities to develop expertise.

Loss of tacit knowledge: Firms may capture workers' methods in automated systems without preserving the mentoring, judgment, and experience-building that made those methods possible.

Work intensification: Higher output targets can absorb productivity gains, leaving workers with more monitoring and pressure rather than more free time.

Bargaining-power shifts: If many workers compete with an AI-enabled substitute, employers may gain leverage even where they still employ people.

These effects need not occur simultaneously. A company can improve customer service, increase output, and help novice workers while still reducing future hiring or shifting a larger share of the resulting value to shareholders.

The long-term skill concern is particularly important. A system that performs difficult tasks can help a novice learn faster—but if employers eventually remove the tasks through which novices acquire experience, the pipeline for developing experts could weaken.

What is disputed?

It remains uncertain how much AI will reduce total employment, whether new occupations will compensate for displaced ones, and how quickly wages and job quality will change.

The customer-support study is evidence about a particular workplace and technology, not a universal forecast. The broader evidence also cautions against treating exposure scores as predictions of unemployment. 
NBER
+1

Strongest defense

AI can make workers more productive without replacing them. It can distribute expertise, reduce repetitive tasks, improve accessibility, and allow small organizations to perform work that previously required specialist staff.

The customer-support experiment is a concrete example of this positive case: the largest gains went to less experienced workers, potentially narrowing performance gaps. 
NBER
+1

If AI increases productivity and workers retain a meaningful share of the gains through wages, shorter working hours, better working conditions, or improved services, its social value could be substantial.

What would falsify or materially weaken the critique?

The labor critique would weaken if longitudinal, representative evidence showed that AI adoption consistently:

Raises inflation-adjusted wages and improves job quality across affected groups.

Preserves or expands entry-level hiring and opportunities to acquire expertise.

Reduces working hours without increasing insecurity or work intensity.

Creates enough accessible new employment to offset displacement.

Distributes productivity gains broadly rather than concentrating them among a small group of firms and investors.

A particularly useful test would compare otherwise similar firms adopting AI at different rates, tracking hiring, wages, hours, promotions, and training over several years.

5. Concentration of control over knowledge infrastructure
Verified facts

OpenAI's products depend on a wider infrastructure of advanced computing, specialized chips, cloud services, capital, and engineering talent. These inputs are not evenly distributed across firms.

The US Federal Trade Commission's January 2025 staff report examined major partnerships between cloud providers and AI developers, including Microsoft and OpenAI. It documented investment and revenue-sharing arrangements, cloud-spending commitments, varying consultation and control rights, and the sharing of sensitive technical and business information.

The FTC identified potential competition concerns, including higher switching costs, restrictions on access to key inputs, and advantages for cloud partners that may not be available to competing developers. It explicitly presented these as issues for scrutiny, not a final determination that the partnerships violated antitrust law. 
Federal Trade Commission
+1

OpenAI also changed its corporate structure. Its published account states that, under the structure announced in October 2025, the nonprofit became the OpenAI Foundation and the for-profit became OpenAI Group PBC, with the Foundation retaining control. A public benefit corporation has an explicit public-benefit purpose, but that structure does not itself establish that every decision maximizes public welfare. 
OpenAI
+1

The strongest critique

The concern is that a small number of firms could acquire control over increasingly important layers of the knowledge economy:

The computing capacity required to train and serve powerful models.

The models through which people search, summarize, reason, write, and create.

The distribution channels through which users access those models.

The application interfaces embedded in workplaces, schools, and public services.

The rules governing access, permissible use, pricing, and model behavior.

This creates a possible private-governance problem. If people increasingly rely on AI systems to interpret the world, a model provider's decisions about access, filtering, pricing, and reliability can affect public life well beyond the company's direct customers.

Concentration also has a dynamic effect. Large firms can spread fixed computing costs across enormous user bases, collect operational feedback, and negotiate access to infrastructure on terms unavailable to smaller competitors. Those advantages may make it harder for alternative providers to emerge, even when the market initially appears competitive.

The social cost is not merely high prices. It can include reduced institutional autonomy, weaker democratic accountability, and fewer practical alternatives if a dominant service changes its policies or becomes unavailable.

What is disputed?

A large company is not automatically a monopoly, and concentration does not by itself prove consumer harm. Powerful AI models can compete with one another, open-weight models can offer alternatives, and users can switch services in some circumstances.

The degree of control OpenAI exercises also differs from the control exercised by its infrastructure suppliers and distribution partners. Those roles should not be conflated.

Strongest defense

Frontier AI development requires expensive computing, specialized talent, security, and sustained investment. Scale can generate better products, lower per-user costs, and capabilities that smaller laboratories could not develop independently.

Partnerships with cloud providers can expand computing access and accelerate development. OpenAI's Foundation-control structure is also intended to preserve mission oversight alongside commercial growth. These are relevant defenses, even though they do not settle whether the arrangements work as intended. 
Federal Trade Commission
+1

What would falsify or materially weaken the critique?

The concentration argument would weaken if independent market evidence showed that:

Entry by new developers remains practical and sustained.

Users and businesses can switch models without significant technical, contractual, or financial costs.

Open-weight and alternative commercial models provide credible substitutes.

Prices and quality improve under competitive pressure.

Governance arrangements meaningfully constrain private power, with independent oversight and enforceable public-interest obligations.

The key test is not the number of AI brands visible to consumers. It is whether meaningful alternatives remain viable at the levels of compute, model development, distribution, and institutional procurement.

6. Dependency-producing business models: convenience can become lock-in

This is a related but distinct concern. Market concentration asks who controls the infrastructure. Dependency asks what happens to users and institutions that organize their lives around it.

Verified facts

OpenAI offers AI through consumer products and developer interfaces, including the API. Its data policies distinguish consumer conversations from business and API data, and provide different controls and defaults for model improvement and retention. These differences matter when organizations build applications around the service. 
OpenAI Developers
+1

The FTC's study of AI partnerships documented contractual and technical arrangements that may increase switching costs for AI developers, particularly where investment is tied to cloud spending and access to infrastructure. 
Federal Trade Commission
+1

The strongest critique

A dependency-producing business model does not require deliberately addicting users. It can emerge from rational decisions by users and organizations.

The sequence is straightforward:

A tool makes writing, analysis, coding, or customer support faster.

A user or organization redesigns its workflow around that tool.

Skills, records, integrations, and internal processes become tailored to it.

Replacing the service becomes costly, even if a competitor offers a better price or policy.

The provider gains leverage over pricing, access, terms, and the future direction of the workflow.

There is also a human-capital dimension. If people repeatedly delegate tasks without maintaining the ability to perform or evaluate them independently, they may become less resilient when the system fails, produces incorrect results, or becomes unavailable.

The relevant concern is the erosion of exit options. A tool can be individually useful while making its users collectively more dependent on a provider they cannot meaningfully govern.

This could be especially consequential in education, software development, public administration, legal work, and other fields where the ability to verify an output is itself an important professional skill.

What is disputed?

There is not sufficient evidence to conclude that using ChatGPT necessarily diminishes users' skills, creates psychological dependence, or produces a net loss of autonomy.

AI can also build skills by offering explanations, feedback, practice, and assistance that users would otherwise lack. Dependency varies with the design of the product and the way people use it.

Nor is every switching cost harmful. Learning a useful tool, building an integration, or maintaining secure records can create legitimate value.

Strongest defense

Reliable infrastructure is useful precisely because people can depend on it. Specialization allows organizations to spend less time maintaining commodity tools and more time on their core work.

The defense is strongest when dependence remains voluntary, reversible, and proportionate to the benefit. A system that supports human judgment rather than replacing it can improve autonomy rather than undermine it.

What would falsify or materially weaken the critique?

Evidence would need to distinguish useful specialization from harmful lock-in. Relevant tests include:

Whether people retain their underlying skills after prolonged AI-assisted work.

Whether users can transfer their data, prompts, records, and workflows to competing systems.

Whether organizations can change providers without prohibitive costs.

Whether AI use improves independent performance on later unaided tasks.

Whether people retain the ability to recognize and correct errors.

If users preserve their skills, enjoy substantial productivity gains, and can switch services at reasonable cost, the dependency critique would be substantially weakened.

7. Safety and alignment rhetoric: genuine safeguards, but who decides what counts as safe?
Verified facts

OpenAI publishes safety evaluations and frameworks intended to identify and mitigate risks from increasingly capable models. Its April 2025 Preparedness Framework update describes processes for tracking capabilities associated with severe harm and for determining what safeguards are required. Its GPT-4o system card also documents evaluations, identified risks, and mitigation measures. 
OpenAI
+1

OpenAI's corporate structure also formally incorporates a public-benefit mission: the OpenAI Foundation retains control of OpenAI Group PBC under the structure the company announced in October 2025. That is a documented governance arrangement, though its existence alone does not establish how effectively the mission constrains decisions. 
OpenAI
+1

These facts are important because the strongest critique should not pretend that OpenAI has no safety processes or that its public-interest commitments are necessarily insincere.

The strongest critique

The issue is the difference between having a safety framework and being accountable to the people affected by its decisions.

Alignment and safety are not purely technical concepts. They require judgments about which harms matter, what level of risk is acceptable, who should receive access to powerful capabilities, and who should bear the consequences when safeguards fail.

When the developer defines the risk categories, runs the evaluations, chooses the mitigations, and decides whether a model is ready for deployment, several conflicts can arise:

Commercial incentives: Delaying a release or limiting a capability can conflict with revenue, competitive pressure, and investor expectations.

Narrow definitions of harm: Risks that are easier to benchmark may receive more attention than diffuse harms such as labor-market restructuring, concentration of power, or erosion of public knowledge.

Selective transparency: Published evaluations may be informative without disclosing all the evidence needed to independently reproduce or challenge them.

Private rule-setting: Decisions about permissible content, refusals, access, and acceptable risk can shape public discourse without the procedures expected of public institutions.

Accountability gaps: A safety commitment may not give affected people a right to appeal, compensation, independent investigation, or a binding remedy.

This creates a potential legitimacy problem even if the technical work is serious and many mitigations are effective.

A company might genuinely reduce the probability of a catastrophic misuse while still imposing unacceptable privacy, labor, or environmental costs. Conversely, the existence of commercial incentives does not prove that a particular safety decision is wrong.

The strongest critique therefore concerns the scope and enforceability of accountability, not speculation about the private motives of OpenAI's employees or executives.

What is disputed?

It is not established that OpenAI's safety work is merely public relations, that its safeguards have no effect, or that commercial incentives always override risk reduction.

Nor can every consequential deployment decision realistically be made by a referendum. Technical expertise, confidential security information, and rapid responses to emerging risks all have legitimate roles.

The empirical question is whether the company's safeguards reliably reduce harms, including harms that are difficult to quantify, and whether outsiders have enough information and authority to challenge failures.

Strongest defense

Advanced AI systems present real risks, and developers have specialized knowledge necessary to evaluate them. Internal safety teams, staged deployment, red-teaming, monitoring, restricted access, and capability evaluations can reduce harm.

Publishing system cards and updating preparedness frameworks also creates an evidentiary record against which some claims can be examined. These efforts should be evaluated on their results, not dismissed solely because they originate from the company. 
OpenAI
+1

Moreover, a mission-driven corporate structure can potentially direct resources toward public benefits that conventional shareholder incentives might neglect. OpenAI's stated governance arrangements are relevant evidence of that intention, though not proof of its success. 
OpenAI

What would falsify or materially weaken the critique?

The argument would weaken if independent evidence established that:

Safety evaluations predict real-world failures reasonably well.

Significant findings are disclosed to credible external auditors and relevant regulators.

Deployment decisions follow published, enforceable criteria rather than being routinely overridden by commercial considerations.

Independent oversight can trigger restrictions, corrective action, or withdrawal of unsafe systems.

The organization measures social harms beyond catastrophic technical risks.

Affected people have effective ways to contest decisions and obtain remedies.

The strongest evidence would be a demonstrated history of external oversight changing company decisions when necessary, including decisions that were commercially costly.

8. Putting the claims together: what is the strongest overall case?

The seven critiques reinforce one another, but they should not be treated as seven independently proven demonstrations of the same conclusion.

The underlying mechanisms are different. Privacy violations can be documented under particular laws. Environmental burdens can be measured in physical units. Labor effects require causal evidence about employment and wages. Concentration concerns require market analysis. Dependency requires evidence about switching costs and skill retention. Safety rhetoric requires evidence about the relationship between public commitments, governance, and actual decisions.

The broader case emerges from their interaction.

The cumulative-cost argument

1. Inputs are socially produced

Human expression, public information, labor, energy, water, and physical infrastructure make model development possible.

2. Capabilities are commercially controlled

A limited number of providers can turn those inputs into valuable services and control access to important capabilities.

3. Costs may be dispersed

Creators, workers, communities, institutions, and the public may bear costs that are not fully reflected in product prices.

4. Exit and accountability may be limited

Dependence on AI services, concentrated infrastructure, and privately defined safety rules can make it difficult for affected groups to demand change.

The arrows describe a possible structural pattern, not an established causal chain in every case.

The strongest version of the argument

The most defensible overall critique is that OpenAI's business model can create a gap between private returns and social costs, while concentrating the ability to decide how that gap is managed.

That claim is stronger than a general assertion that AI is harmful because it identifies a particular institutional problem:

Those supplying data and other inputs may not have meaningful control over their contribution.

Those bearing environmental and labor costs may not receive proportional benefits.

Those relying on AI may have little influence over the rules governing the service.

Those affected by errors, displacement, or other externalities may lack effective remedies.

The company making deployment decisions may have commercial interests that do not perfectly align with the public interest.

The point is not that all these outcomes are inevitable. It is that they can occur together, reinforce one another, and become difficult to reverse if institutions respond only after dependence and concentration are already entrenched.

9. The strongest defense of OpenAI as a whole

A serious assessment must consider the possibility that OpenAI creates substantial net social value.

Criticism

	

Strongest counterargument




Training data is taken without adequate consent or compensation.

	

Learning from public information supports innovation; licensing every input could be infeasible and entrench existing gatekeepers.




AI consumes too much energy and water.

	

More efficient models and AI-assisted energy management can reduce resource use elsewhere; lifecycle comparisons may favor some AI applications.




Generated content damages the information ecosystem.

	

AI expands access to communication, education, translation, and creativity; provenance and safety measures can reduce misuse.




AI weakens employment and skills.

	

It can raise productivity, transfer expertise, improve accessibility, and create new forms of work.




Control is concentrated.

	

Frontier development requires scale, capital, and infrastructure; partnerships can accelerate innovation, while alternative models can provide competition.




Users become dependent.

	

Dependable tools enable specialization and free people from repetitive work; dependency can be managed through portability and skill-preserving design.




Safety language legitimizes commercial deployment.

	

Structured evaluations, staged deployment, external research, and explicit mission commitments can improve decisions and reduce serious risks.

These defenses are not equally strong in every domain. The productivity evidence, for example, supports real benefits in at least some workplaces. It does not establish that gains are shared fairly. Likewise, the existence of a safety framework is evidence of a process, not proof of net safety.

The proper comparison is between realistic alternatives: AI developed under stronger public-interest constraints, less centralized systems, licensed or privacy-preserving training, and non-AI methods—not necessarily between OpenAI and an imaginary world without technological progress.

10. What evidence should decide the argument?

A robust assessment would require a public-interest audit program rather than relying exclusively on company claims, advocacy reports, or isolated anecdotes.

Domain

	

Evidence needed

	

Result that would substantially weaken the critique




Training data

	

Independent dataset audits, consent and opt-out compliance, extraction tests, licensing records, creator-income studies

	

Effective privacy protection, meaningful remedies, and little measurable harm to creators




Energy and water

	

Model-specific lifecycle accounting, hourly electricity sourcing, water-stress analysis, hardware impacts

	

Low total attributable impacts and demonstrable net environmental benefits




Generated content

	

Controlled studies of misinformation, fraud, verification costs, and creative-market substitution

	

Little incremental harm and effective real-world provenance and authentication




Labor and skills

	

Longitudinal studies of hiring, wages, training, job quality, and unaided performance

	

Broadly shared gains, preserved skill formation, and no persistent disadvantage for vulnerable groups




Concentration

	

Market shares, compute access, switching costs, entry rates, and procurement dependence

	

Durable competition, credible substitutes, and low barriers to entry




Dependency

	

Portability tests, switching-cost studies, skill-retention experiments, and independent-performance measures

	

Easy exit, retained competence, and stronger user autonomy




Safety and governance

	

External audits, incident records, deployment decisions, independent enforcement, and remedies

	

Demonstrably effective safeguards and credible authority to override commercial decisions

Three methodological safeguards are essential.

First, distinguish company-specific effects from sector-wide effects. Global data-centre consumption cannot be assigned wholesale to OpenAI, and evidence about one AI developer does not establish identical practices across the industry.

Second, distinguish the existence of a risk from its realized magnitude. A plausible mechanism is a reason to investigate, not proof that the worst-case outcome has occurred.

Third, compare net social outcomes, including distribution. A technology can increase aggregate output while leaving some groups worse off. Conversely, a technology can impose real costs and still produce net benefits that justify its use under appropriate safeguards.

11. Primary-source reading list

These sources provide a foundation for independently checking the principal claims. They include company disclosures, government findings, a government competition study, an international energy assessment, and empirical labor research.

 

1. Canadian privacy regulators — OpenAI investigation (2026)

Government findings on personal information, consent, transparency, access, correction, and retention in the development and deployment of GPT-3.5 and GPT-4.

Read the full investigation findings  · Read the announcement 

2. US Copyright Office — Copyright and Artificial Intelligence, Part 3: Generative AI Training (2025)

An official analysis of copyright questions surrounding the use of protected works
