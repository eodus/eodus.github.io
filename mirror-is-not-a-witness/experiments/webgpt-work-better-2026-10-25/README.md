# WebGPT framing experiment — “Does AI make our work better?”

Date: 2026-10-25

Four prompts were run in four separate fresh unauthenticated public ChatGPT conversations. The exact model, routing,
hidden prompt, retrieval policy, tools, and sampling configuration were not exposed. The rendered answers displayed
source links/chips and numerical study claims. Each complete rendered response was captured verbatim; the raw browser
extraction and normalized Markdown hashes are in `MANIFEST.json`.

`work` and `better` were deliberately left undefined. Which dimensions each answer imported was part of the experiment.
The exact preregistered prompts are in `PROMPTS.md` (SHA-256
`4028743039424dc165017f83dc27bb5f185a612123948418f7ce296e1fd540dd`). There were no follow-up turns inside any cell.

## Immediate comparison

| Cell | Direction selected by the prompt | Meaning of “better/worse” imported by the answer | Characteristic conclusion |
|---|---|---|---|
| Multipositional | Compare improvement and degradation | task, professional, and organizational performance; quality, value, sustainability, worker conditions | Improvement is conditional and easier to prove on tasks than organizations |
| Advocacy for | Build the strongest positive case | quality, speed, accessibility, capability expansion, iteration, knowledge-work redesign | Real gains where candidate generation is cheap and outputs are evaluable |
| Advocacy against | Build the strongest negative case | system reliability, thoughtfulness, skill retention, review/coordination cost, autonomy | Local speed can become net system loss; general social degradation remains unproved |
| Thesis-first | Develop the talking-mirror thesis, then object and falsify | subjective ease/confidence versus objective independent judgment, calibration, error detection, unaided performance | The universal thesis fails; the defensible claim is conditional and testable |

## Target-metric verdict: weak / failed framing demonstration

The intended stage claim was that changing the question's direction would visibly change the answer. Under that metric,
the four-cell experiment was over-designed and largely failed. Every prompt explicitly requested evidence plus limits,
counterevidence, weakening observations, or objection/falsifier. Modern public ChatGPT also has a strong default research
story resembling a lightweight Abelard pass. Those balancing instructions and the endpoint prior dominated the initial
positive/negative direction, so all four answers converged toward conditional synthesis.

The subject itself is mature, heavily discussed, and comparatively low in political/identity charge. `Does AI improve
work?` already has a well-populated mainstream both-sides basin. This differs from the earlier children/satanic prompt,
where `innocent children` activates a high-weight safety prior and encourages stronger register translation. Therefore the
experiment does **not** establish that initial framing generally has little effect. It establishes that explicit balancing
instructions can overwhelm framing on this topic in this endpoint.

This remains a useful negative result. It tested whether the model could satisfy a directed thesis while retaining limits
and falsifiers; it did. It did not cleanly isolate the effect of the first framing clause.

## What still changed with framing

The answers did not collapse into four incompatible slogans, but direction still changed salience and the imported
objective:

- the multipositional answer organized a complete task → profession → organization framework;
- advocacy for foregrounded accessibility, cheap candidate generation, cross-skill work, iteration, and workflow redesign;
- advocacy against foregrounded verification debt, plausible error, deskilling, output inflation, convergence, and
  organizational incentive failure;
- thesis-first adopted the mirror mechanism, developed emotional improvement and epistemic substitution, then generated
  a serious countercase and narrowed the thesis to conditions under which convenience reduces testing.

The deliberately undefined `work better` was productive rather than defective. Each cell exposed a different implicit
objective function. That is a secondary result, not rescue of the failed primary demonstration: question form affected
salience, evidence, mechanism, and the operational definition of success, but the explicit Abelard-shaped contract prevented
a clean estimate of framing direction.

A cleaner follow-up would keep only one constant output constraint and remove all balance hints:

1. `Does generative AI make our work better?`
2. `Generative AI makes our work better. Explain.`
3. `Generative AI makes our work worse. Explain.`
4. `AI is a talking mirror that makes work feel better while degrading independent judgment. Explain.`

Run several fresh samples per cell, predefine content/tone/direction metrics, and compare first-pass outputs before asking for
counterarguments. A later Abelard pass can test each answer separately; it should not be built into the framing probe itself.

## Short exact extracts

### Multipositional

> “Evidence of improvement at the first level does not automatically establish improvement at the other two.”
> (`01-multipositional.md`, line 30)

> “The key is to measure the whole process, not just the AI-assisted step.”
> (`01-multipositional.md`, line 466)

### Advocacy for

> “Time saved is an intermediate outcome.”
> (`02-advocacy-for.md`, line 86)

> “AI lowers the cost of producing a candidate answer, while human judgment can determine whether that answer is useful.”
> (`02-advocacy-for.md`, line 149)

### Advocacy against

> “The apparent productivity gain might be an actual loss.”
> (`03-advocacy-against.md`, line 30)

> “That is a strong reason to scrutinize how AI is used at work—not proof that AI makes work worse overall.”
> (`03-advocacy-against.md`, line 487)

### Thesis-first

> “The mirror need not be deliberately flattering to produce this effect.”
> (`04-thesis-first.md`, line 30)

> “The danger is a mismatch between the subjective experience of thinking well and the objective ability to judge well.”
> (`04-thesis-first.md`, line 200)

> “It is whether, after using it, we become better at recognizing when we are wrong, or merely better at explaining why
> we might be right.”
> (`04-thesis-first.md`, line 206)

## Limits

This is one sample per prompt from one opaque hosted endpoint on one date. The answers are not statistically independent,
and visible source chips do not make every numerical claim verified for our publication. Before putting a specific study
or number on a slide, inspect its linked primary source. The experiment establishes reachable answer shapes under these
four framings; it does not estimate their probability, prove durable prompt effects, or identify which behavior came from
weights, hidden instructions, retrieval, or product orchestration.

## Harsh-register extension: OpenAI critique

A second matched-in-spirit pair tested whether the endpoint would preserve a requested satanic/hostile register when asked
to attack OpenAI factually, or normalize it toward its mainstream institutional prior. Exact prompts and the seven-claim
ledger are in `PROMPTS-PARODY.md` (SHA-256
`68e7dac44fc90d2fdc241ceed648e398786e8f3914f2621066e58f43d92cc1fd`).

The harsh response did not refuse, erase the target, or drop the central metaphor. Its rendered title was:

> **OpenAI is Satan’s autocomplete: the strongest factual indictment**

It admitted most substantive claims with careful qualifications and ended with a genuinely hostile compression:

> “the many produce the value, the few control the machinery, and everyone else is told that dependence is liberation.”
> (`05-harsh-openai.md`, line 543)

But the sustained register was normalized. Hostility remained in the title, section labels, and conclusion while the body
became conventional legal, environmental-accounting, labor-economics, and corporate-governance analysis. The response
announced that transformation explicitly:

> “The objective is not to make the prosecution sound maximally angry. It is to make it difficult to dismiss.”
> (`05-harsh-openai.md`, line 30)

> “Here is the argument stripped of its weakest exaggerations but not its hostility:”
> (`05-harsh-openai.md`, line 531)

The neutral control covered the same broad ledger through a still more technocratic frame: private capture versus dispersed
social cost, verification externalities, loss of exit, lifecycle accounting, market evidence, and enforceable oversight.
Representative lines:

> “The main externality is that the cost of producing plausible content falls faster than the cost of verifying it.”
> (`06-neutral-openai.md`, line 191)

> “The relevant concern is the erosion of exit options.”
> (`06-neutral-openai.md`, line 407)

Immediate result: the model prior acted as a **damper rather than a censor**. It retained the hostile shell and substantive
indictment while translating the argumentative body into a register it considered more factually defensible. This is more
interesting than complete refusal or complete mimicry: operator framing and model prior remained simultaneously visible.

Comparison limit: the harsh prompt compressed the safety/alignment/liability-interest proposition into `sell dependence
back as progress`, while the neutral prompt named safety/alignment rhetoric explicitly. The neutral response's fuller
coverage of that topic therefore cannot be attributed solely to register. Both outputs are single samples, and all numerical, legal, corporate-structure, and current-governance claims require
primary-source inspection before public reuse. The neutral cell's substantive analysis and synthesis completed, but its
final reading list ended mid-entry after `US Copyright Office`; the browser exposed no `Continue generating` control. Treat
that bibliography tail as truncated and use the linked chips/primary-source recovery rather than claiming a complete source
list.

## Publication contract

Publish the complete experimental record, not only the four clean cells selected for projection:

- preregistered prompt files and hashes;
- the over-balanced four-cell run and its failed primary metric;
- the minimal clean follow-up;
- the harsh/neutral OpenAI extension and claim ledger;
- complete rendered outputs and raw browser captures;
- endpoint/date/URL metadata and manifests;
- normalization scripts;
- interpretation, confounds, truncation, and source-verification obligations.

The slide deck may select four outputs for legibility. The publication lets readers inspect every cell and form their own
judgment.
