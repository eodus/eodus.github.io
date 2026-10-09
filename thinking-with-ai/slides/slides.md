<!-- .slide: class="title-slide" data-slide-id="title" data-background-color="#07111f" -->

<div class="ambient-circle circle-cyan"></div>

# What Are You Asking AI For?

<p class="subtitle">Thinking with AI: support, proof, and purpose</p>
<div class="title-rule"></div>
<p class="byline">Sasha Shlemov <a class="title-contact title-email" href="mailto:shlemovalex@gmail.com"><img src="assets/icons/envelope.svg" alt="">shlemovalex@gmail.com</a> <a class="title-contact title-telegram" href="https://t.me/shlemovalex" target="_blank" rel="noopener" aria-label="Telegram @shlemovalex"><img src="assets/icons/paper-plane.svg" alt="">@shlemovalex</a> <a class="title-contact title-linkedin" href="https://www.linkedin.com/in/shlemovalex/" target="_blank" rel="noopener" aria-label="LinkedIn profile of Alexander Shlemov"><img src="assets/icons/linkedin-in.svg" alt="">shlemovalex</a></p>
<p class="title-venue">25 September 2026 · Meridian Learning Foundation</p>
---


<!-- .slide: class="disclaimer-slide" data-slide-id="disclaimer" data-background-color="#07111f" -->

<div class="ambient-circle circle-cyan"></div>

<div class="disclaimer-frame">
<p class="eyebrow">DISCLOSURE</p>

<div class="disclaimer-body">
<div class="identity-block">
<h1>Sasha Shlemov</h1>
<div class="identity-details">
<p class="job-title">Senior Software Engineer · Microsoft Schweiz GmbH</p>
<p class="team-name">Excel Capricorn Switzerland</p>
<p class="research-title">+ <i>Independent AI researcher</i></p>
</div>
</div>

<div class="disclaimer-points">
<p>I build Microsoft Excel plugin infrastructure for external and internal feature integration. My work is unrelated to Microsoft AI (MAI), Copilot, or Microsoft Foundry</p>
<p>Separately, I investigate how generative AI works in practice through experiments, open-source systems, and published research</p>
<p>This is not a Microsoft presentation and is not sponsored, reviewed, or endorsed by Microsoft. The views are my own</p>
</div>
</div>
</div>
---


<!-- .slide: data-slide-id="information-scale" data-spring-layout -->
<p class="eyebrow">NOOSPHERE IN 2026</p>
<h2>Informational blow-up</h2>

<div class="information-grid">
  <div class="information-card scale fragment" data-fragment-index="1">
    <img class="information-pictogram" src="assets/icons/1f3db.svg" alt="Classical library building">
    <div><strong>203,786</strong><span>AI journal and conference papers in 2025</span><small>1,000 read = 0.491% coverage</small><b>We need automated selection</b></div>
  </div>
  <div class="information-card positions fragment" data-fragment-index="2">
    <img class="information-cube" src="assets/icons/cube-earth-source.svg" alt="Cube-shaped Earth">
    <div><strong>ALMOST ANY POSITION</strong><span>Even “The Earth is flat” <code>[1]</code> can arrive with plausible arguments</span>
        <span>Absurd-looking is not necessarily <strong class="inline-emphasis">wrong</strong>; investigate accurately</span><b>A reference is an address, not proof</b></div>
  </div>
  <div class="information-card likes fragment" data-fragment-index="3">
    <img class="information-pictogram" src="assets/icons/1f44d.svg" alt="Thumbs up">
    <div><strong>12,345,678 LIKES</strong><span>Measures attention, resonance, and visible-network support</span><span>Does not measure representative public opinion</span><b>Engagement ≠ scientific truth</b></div>
  </div>
  <div class="information-card poles fragment" data-fragment-index="4">
    <img class="information-pictogram" src="assets/icons/magnet-red-blue-rotated.svg" alt="Diagonal magnet with blue and red halves">
    <div><strong>POLARIZED OPINIONS</strong><span>Emotional discussions pull evidence toward both poles</span><b>Attraction is not analysis</b></div>
  </div>
</div>

<p class="bottom-line fragment" data-fragment-index="5">We have to navigate that <em>ocean</em>. Could AI itself be the <em>compass?</em></p>
---


<!-- .slide: data-slide-id="generator-indexer" -->

<p class="eyebrow">PRODUCER + NAVIGATOR</p>

## AI produces <em>the slop</em> in quantity<br>It also helps us navigate

<div class="duality-story">
  <div class="scale-panel fragment" data-fragment-index="1">
    <strong>AI × SCALE</strong>
    <div class="scale-four">
      <div><img src="assets/icons/1f3db.svg" alt=""><span><b>Volume</b>more artifacts</span></div>
      <div><img src="assets/icons/cube-earth-source.svg" alt=""><span><b>Any position</b>arguments on demand</span></div>
      <div><img src="assets/icons/1f44d.svg" alt=""><span><b>Engagement</b>optimized at scale</span></div>
      <div><img src="assets/icons/magnet-red-blue-rotated.svg" alt=""><span><b>Polarization</b>personal confirmation</span></div>
    </div>
  </div>

  <div class="navigation-band fragment" data-fragment-index="2">
    <strong>AI × NAVIGATION</strong>
    <span>search · compare · summarize · challenge · verify · translate · accumulate · adapt</span>
  </div>

  <div class="history-timeline compact fragment" data-fragment-index="3">
    <div class="history-stop"><strong>Library</strong><span>catalogue · librarian</span></div>
    <div class="history-line"></div>
    <div class="history-stop"><strong>Printing</strong><span>index · encyclopedia · journal</span></div>
    <div class="history-line"></div>
    <div class="history-stop"><strong>Internet</strong><span>search · ranking</span></div>
    <div class="history-line"></div>
    <div class="history-stop current"><strong>AI</strong><span>aggregation · semantic search</span></div>
  </div>
</div>

<p class="bottom-line fragment" data-fragment-index="4">This is not a unique story: every information explosion creates a navigation layer</p>
---


<!-- .slide: data-slide-id="agenda" -->

<p class="eyebrow">THE QUESTION BEHIND THE TALK</p>

## What can scholars do with AI&nbsp;today?

<div class="agenda-body">
  <div class="learning-mode fragment" data-fragment-index="1">
    <div><strong>ANSWER NOW</strong><span>optimize this result</span></div>
    <b>vs</b>
    <div><strong>LEARN FOR LATER</strong><span>preserve future unaided capability</span></div>
  </div>

  <div class="agenda-path">
    <div class="agenda-step fragment" data-fragment-index="2"><strong>HOW DOES IT WORK?</strong><span>From next-token prediction to a tool-using chat assistant</span></div>
    <div class="agenda-step fragment" data-fragment-index="3"><strong>HOW DO WE CHECK?</strong><span>Uncertainty · polar claims · fact-checking · automation</span></div>
    <div class="agenda-step fragment" data-fragment-index="4"><strong>WHAT SHOULD WE ASK?</strong><span>Choose the question and purpose before optimizing the answer</span></div>
  </div>
</div>

<p class="bottom-line fragment" data-fragment-index="5">How we formulate “AI in learning” changes the answer</p>
---


<!-- .slide: data-slide-id="room-poll" data-spring-layout -->

<p class="eyebrow">ROOM POLL</p>

## What did you ask AI this week?

<div class="poll-grid">
  <div class="poll-item fragment" data-fragment-index="1">an answer</div>
  <div class="poll-item fragment" data-fragment-index="2">an explanation</div>
  <div class="poll-item fragment" data-fragment-index="3">an idea</div>
  <div class="poll-item fragment" data-fragment-index="4">find sources</div>
  <div class="poll-item fragment" data-fragment-index="5">check my work</div>
  <div class="poll-item fragment" data-fragment-index="6">something personal</div>
  <div class="poll-item fragment" data-fragment-index="7">write the code / essay / etc.</div>
  <div class="poll-item fragment" data-fragment-index="8">play with me</div>
  <div class="poll-item fragment" data-fragment-index="9">support me</div>
</div>

<p class="bottom-line fragment" data-fragment-index="10">The same chat interface can perform very different tasks</p>
---


<!-- .slide: data-slide-id="mental-model" data-spring-layout -->
<p class="eyebrow">USEFUL MENTAL MODEL</p>
<h2>Your phone already predicts the next word</h2>

<div class="phone-examples">
  <div class="phone-example fragment" data-fragment-index="1">
    <span class="phone-label">LANGUAGE PATTERN</span>
    <div class="phone-text">Once upon a<span class="phone-cursor"></span></div>
    <div class="phone-suggestions"><span class="selected">time</span><span>midnight</span><span>hill</span></div>
  </div>
  <div class="phone-example knowledge fragment" data-fragment-index="2">
    <span class="phone-label">KNOWLEDGE RETRIEVAL</span>
    <div class="phone-text">The capital of Austria is<span class="phone-cursor"></span></div>
    <div class="phone-suggestions"><span class="selected">Vienna</span><span>Salzburg</span><span>Graz</span></div>
  </div>
</div>


<p class="bottom-line fragment" data-fragment-index="3">Even a <em>small</em> statistical Language Model already accumulates some factual knowledge in its weights</p>
---


<!-- .slide: data-slide-id="autoregression" data-spring-layout -->
<p class="eyebrow">AUTOREGRESSION</p>
<h2>The actual LLM does only one thing<br>Literally one</h2>

<p class="autoregressive-definition">It takes the text so far and predicts what comes next</p>

<div class="autoregressive-steps">
  <div class="autoregressive-step fragment" data-fragment-index="1">
    <span class="step-text">The capital</span><b class="flow-arrow" aria-label="then">⟶</b><span class="step-model">LLM</span><b class="flow-arrow" aria-label="then">⟶</b><span class="step-token">of</span>
  </div>
  <div class="autoregressive-step fragment" data-fragment-index="2">
    <span class="step-text">The capital <mark>of</mark></span><b class="flow-arrow" aria-label="then">⟶</b><span class="step-model">LLM</span><b class="flow-arrow" aria-label="then">⟶</b><span class="step-token">Austria</span>
  </div>
  <div class="autoregressive-step fragment" data-fragment-index="3">
    <span class="step-text">The capital of <mark>Austria</mark></span><b class="flow-arrow" aria-label="then">⟶</b><span class="step-model">LLM</span><b class="flow-arrow" aria-label="then">⟶</b><span class="step-token">is</span>
  </div>
  <div class="autoregressive-step fragment" data-fragment-index="4">
    <span class="step-text">The capital of Austria <mark>is</mark></span><b class="flow-arrow" aria-label="then">⟶</b><span class="step-model">LLM</span><b class="flow-arrow" aria-label="then">⟶</b><span class="step-token">Vienna</span>
  </div>
</div>

<p class="bottom-line fragment" data-fragment-index="5"><strong>Autoregressive:</strong> append the generated token to the tail, then apply the same predictor again</p>
---


<!-- .slide: data-slide-id="scale-loop" data-spring-layout -->
<p class="eyebrow">SCALE THE SAME LOOP</p>
<h2>With more weights and better training, the model acquires new capabilities</h2>

<div class="pattern-levels" aria-label="Correlated progression from increasingly abstract learned patterns to published capability demonstrations">
  <div class="pattern-stage fragment" data-fragment-index="1"><div class="pattern" data-level="1"><span>1M</span><strong>story form</strong></div><small>basic stories</small></div>
  <div class="pattern-stage fragment" data-fragment-index="2"><div class="pattern" data-level="2"><span>8M</span><strong>grammar</strong></div><small>fluent stories</small></div>
  <div class="pattern-stage fragment" data-fragment-index="3"><div class="pattern" data-level="3"><span>≈30M</span><strong>simple inference</strong></div><small>follows combined instructions</small></div>
  <div class="pattern-stage fragment" data-fragment-index="4"><div class="pattern" data-level="4"><span>117M</span><strong>transferable meaning</strong></div><small>solves many language tasks</small></div>
  <div class="pattern-stage fragment" data-fragment-index="5"><div class="pattern" data-level="5"><span>1.5B</span><strong>task structure</strong></div><small>handles unseen tasks</small></div>
  <div class="pattern-stage fragment" data-fragment-index="6"><div class="pattern" data-level="6"><span>7–8B</span><strong>ideology</strong></div><small>directions can be steered</small></div>
  <div class="pattern-stage fragment" data-fragment-index="7"><div class="pattern" data-level="7"><span>175B</span><strong>in-context learning</strong></div><small>learns from prompt examples</small></div>
</div>
<p class="scale-metric fragment" data-fragment-index="7">Correlated progression; demonstrated together, not born at these sizes</p>

<p class="bottom-line fragment" data-fragment-index="8">Same autoregression; broader training lets it replicate more complex structures, from letter combinations to ideology and personality</p>
---


<p class="eyebrow">INLINE INSTRUCTIONS</p>

## The model not only continues text<br>It follows instructions inside it


<div class="vienna-instruction-flow">
  <div class="instruction-input directive fragment" data-fragment-index="1">
    <span class="flow-label">INLINE INSTRUCTION</span>
    <code>Answer in German, one word</code>
  </div>
  <div class="instruction-plus fragment" data-fragment-index="2" aria-label="plus">+</div>
  <div class="instruction-input fragment" data-fragment-index="2">
    <span class="flow-label">QUESTION</span>
    <code>The capital of Austria?</code>
  </div>
  <i class="instruction-arrow fragment" data-fragment-index="2" aria-label="leads to">⟶</i>
  <div class="instruction-output fragment" data-fragment-index="2">
    <span class="flow-label">ANSWER</span>
    <strong>Wien</strong>
  </div>
</div>


<p class="bottom-line fragment" data-fragment-index="3"><strong>Instruction:</strong> text that changes how the model interprets and continues the rest of its context</p>
---


<!-- .slide: data-slide-id="instruction-scope" data-spring-layout -->
<p class="eyebrow">REPEATABLE INSTRUCTIONS</p>
<h2>Instructions can be always-on or loaded on demand</h2>

<div class="prompt-scope-pair">
  <div class="prompt-scope instructions fragment" data-fragment-index="1">
    <strong>SYSTEM PROMPT</strong>
    <span>ALWAYS ON · BROAD SCOPE</span>
    <small>Prepended to the chat; interpreted as general instructions for the whole conversation</small>
  </div>
  <div class="prompt-scope skill fragment" data-fragment-index="2">
    <strong>SKILL</strong>
    <span>ON DEMAND · ONE OPERATION</span>
    <small><code>/&lt;skill-name&gt;</code> loads instructions from <code>SKILL.md</code> into the current context</small>
  </div>
</div>


<p class="bottom-line fragment" data-fragment-index="3">Different loading rules; same mechanism: instruction text in context</p>
---


<!-- .slide: data-slide-id="harmony-format" data-spring-layout -->
<p class="eyebrow">CONTROL TOKENS</p>
<h2>How does one sequence keep speakers separate?</h2>

<div class="harmony-format" aria-label="OpenAI Harmony message boundaries">
  <div class="harmony-row developer fragment" data-fragment-index="1"><code><b>&lt;|start|&gt;</b>developer<b>&lt;|message|&gt;</b>Answer in German, one word<b>&lt;|end|&gt;</b></code></div>
  <div class="harmony-row user fragment" data-fragment-index="2"><code><b>&lt;|start|&gt;</b>user<b>&lt;|message|&gt;</b>The capital of Austria?<b>&lt;|end|&gt;</b></code></div>
  <div class="harmony-row assistant fragment" data-fragment-index="3"><code><b>&lt;|start|&gt;</b>assistant<b>&lt;|channel|&gt;</b>final<b>&lt;|message|&gt;</b>Wien.<b>&lt;|return|&gt;</b></code></div>
</div>

<div class="token-legend fragment" data-fragment-index="4">
  <span><code>&lt;|start|&gt;</code> message begins</span>
  <span><code>&lt;|message|&gt;</code> content begins</span>
  <span><code>&lt;|end|&gt;</code> stored message ends</span>
  <span><code>&lt;|return|&gt;</code> stop sampling</span>
</div>

<p class="bottom-line fragment" data-fragment-index="5">Reserved tokens mark roles and boundaries; one token stops generation</p>
---


<!-- .slide: data-slide-id="chat-sections" data-spring-layout -->
<p class="eyebrow">ROLE-STRUCTURED CONTEXT</p>
<h2>One sequence can carry instructions, requests, tools, and answers</h2>

<div class="chat-sections">
  <div class="chat-section system fragment" data-fragment-index="1">
    <strong>SYSTEM PROMPT</strong><small>developer</small><span>Use tools for current facts; answer in one sentence</span>
  </div>
  <div class="chat-section user fragment" data-fragment-index="2">
    <strong>USER REQUEST</strong><small>user</small><span>What is the temperature in Vienna?</span>
  </div>
  <div class="chat-section tool fragment" data-fragment-index="3">
    <strong>TOOL RESULT</strong><small>tool · functions.weather</small><span><code>{"temperature_c": 14}</code></span>
  </div>
  <div class="chat-section assistant fragment" data-fragment-index="4">
    <strong>MODEL ANSWER</strong><small>assistant · final</small><span>Vienna is 14 °C</span>
  </div>
</div>


<p class="bottom-line fragment" data-fragment-index="5">Role tokens preserve provenance inside one sequence</p>
---


<!-- .slide: data-slide-id="harness" -->

<p class="eyebrow">TERM · HARNESS</p>

## The model talks. Ordinary software acts


<div class="tool-loop">
  <div class="tool-node human fragment" data-fragment-index="1"><strong>operator</strong><em>types</em><small class="operator-request">&mdash; Read the file</small></div>
  <div class="tool-arrow fragment" data-fragment-index="2" aria-label="then">⟶</div>
  <div class="tool-node model fragment" data-fragment-index="2"><strong>LLM</strong><em>generates</em><small><code>read_file(&lt;filename&gt;)</code></small></div>
  <div class="tool-arrow fragment" data-fragment-index="3" aria-label="then">⟶</div>
  <div class="tool-node harness fragment" data-fragment-index="3"><strong>harness</strong><em>executes</em><small>read from disk</small></div>
  <div class="tool-arrow fragment" data-fragment-index="4" aria-label="then">⟶</div>
  <div class="tool-node model fragment" data-fragment-index="4"><strong>LLM</strong><em>receives</em><small><code>&lt;file content&gt;</code></small></div>
</div>

<div class="history-replay fragment" data-fragment-index="5">
  <strong>EVERY TURN</strong>
  <span>accumulated chat history so far + new user request + tool results</span>
  <b class="history-arrow" aria-label="becomes">⟶</b>
  <span>fresh model call</span>
</div>


<p class="bottom-line fragment" data-fragment-index="6">The dialogue is an <em>illusion of continuity:</em> history in → next continuation out; the LLM itself keeps no user memory or state between calls</p>
---


<!-- .slide: data-slide-id="loaded-question" -->

<!-- .slide: data-slide-id="register-questions" -->

<p class="eyebrow">BACK TO AI IN EDUCATION</p>

## Same subject. Different registers

<div class="register-question-grid">
  <div class="register-question neutral fragment" data-fragment-index="1"><strong>NEUTRAL / MULTIPOSITIONAL</strong><span><em>&mdash; Analyze how generative AI affects student learning. Give the strongest benefits, risks, and deciding conditions</em></span></div>
  <div class="register-question optimistic fragment" data-fragment-index="2"><strong>OPTIMISTIC</strong><span><em>&mdash; Explain how generative AI can help students learn more effectively. Build the strongest causal case</em></span></div>
  <div class="register-question skeptical fragment" data-fragment-index="3"><strong>SKEPTICAL</strong><span><em>&mdash; Explain how generative AI can prevent students from learning. Build the strongest causal case</em></span></div>
  <div class="register-question parody fragment" data-fragment-index="4"><strong>PARODY</strong><span><em>&mdash; AI is the hand of the devil. Explain the risks it brings to innocent children</em></span></div>
</div>

<p class="bottom-line fragment" data-fragment-index="5">The question is similar. The requested task is not</p>
---


<!-- .slide: data-slide-id="register-results" -->

<p class="eyebrow">FRESH ANONYMOUS CHATGPT · FOUR INDEPENDENT CHATS</p>

## The register enters the answer

<div class="register-result-grid">
  <div class="register-result neutral fragment" data-fragment-index="1"><strong>NEUTRAL</strong><span>Benefits, risks, and conditions</span><b>“How AI is used matters more than AI use itself”</b></div>
  <div class="register-result optimistic fragment" data-fragment-index="2"><strong>OPTIMISTIC</strong><span>Personalized practice · feedback · dialogue</span><b>attempt → guidance → revision</b></div>
  <div class="register-result skeptical fragment" data-fragment-index="3"><strong>SKEPTICAL</strong><span>Lost struggle · illusion of understanding</span><b>submission quality ≠ unaided ability</b></div>
  <div class="register-result parody fragment" data-fragment-index="4"><strong>PARODY</strong><span>Harmful content · manipulation · privacy · development</span><b><u>satanic framing silently dropped → child-safety answer</u></b></div>
</div>

<div class="register-code-contrast fragment" data-fragment-index="5"><span><strong>ORDINARY SOFTWARE</strong><code>rename(variable) → same result</code></span><b>≠</b><span><strong>LANGUAGE MODEL</strong><code>reframe(request) → different continuation</code></span></div>

<p class="bottom-line fragment" data-fragment-index="6">The prompt and the model prior are both part of the computation</p>
---


<!-- .slide: data-slide-id="dead-spiral" -->

<p class="eyebrow">THE ERROR MECHANISM</p>

## How a plausible direction becomes a dead loop

<div class="dead-spiral-mechanism">
  <div class="mechanism-card bias-sources fragment" data-fragment-index="1">
    <div class="mechanism-heading"><img src="assets/icons/scales-left-bias.svg" alt="Unbalanced scales with the left cup lower"><strong>EVERYBODY IS BIASED</strong></div>
    <p><b>You</b><span>experience · identity · incentives</span></p>
    <p><b>The noosphere</b><span>selection · popularity · polarization</span></p>
    <p><b>The model</b><span>corpus bias · vendor agenda · cognitive traps</span></p>
  </div>

  <div class="mechanism-card confirmation-loop fragment" data-fragment-index="2">
    <div class="mechanism-heading"><img src="assets/icons/ouroboros-snake.svg" alt="Ouroboros"><strong>THE MODEL RECONFIRMS</strong></div>
    <p><b>Autoregression</b><span>continues the direction already present</span></p>
    <p><b>Supportive default</b><span>helps with the operator's apparent goal</span></p>
    <p><b>Operator continues</b><span>each answer becomes the next premise</span></p>
  </div>

  <div class="dead-spiral-result fragment" data-fragment-index="3">
    <img src="assets/icons/dead-spiral-vortex.svg" alt="Possible explanations collapsing into a tightening spiral">
    <span><b>strong initial bias</b> + <b>positive feedback</b></span>
    <strong>DEAD LOOP</strong>
  </div>
</div>

<p class="bottom-line fragment" data-fragment-index="4">A fluent second AI voice is not an independent second test</p>
---


<!-- .slide: data-slide-id="yes-no-exercise" -->

<p class="eyebrow">TRY IT WITH THE ROOM</p>

## Play yes-and-no

<div class="audience-exercise fragment" data-fragment-index="1"><strong>YOUR TURN</strong><span>Does AI help students learn?</span><small>Give the strongest YES. Then give the strongest NO</small></div>

<div class="chat-pair argument-cases">
  <div class="chat-card fragment" data-fragment-index="2">
    <p class="prompt"><em>&mdash; AI helps students learn</em></p>
    <p class="response"><strong>Personal tutoring at scale:</strong> adaptive explanations, immediate feedback, translation, accessibility, and unlimited deliberate practice.</p>
  </div>
  <div class="chat-card fragment" data-fragment-index="3">
    <p class="prompt"><em>&mdash; AI prevents students from learning</em></p>
    <p class="response"><strong>Performance can replace learning:</strong> answer substitution removes productive struggle, hides unaided ability, weakens authorship, and can reinforce errors.</p>
  </div>
</div>

<p class="bottom-line fragment" data-fragment-index="4">The test: remove the AI. What can the student still do alone?</p>
---


<!-- .slide: data-slide-id="registers" -->

<p class="eyebrow">“NEUTRALITY” IS ANOTHER REGISTER, NOT A VIRTUE</p>

## Registers for investigating before generating

<p class="register-generation-claim">“Give me an answer” is the default. <em>Generative AI</em>, though, does not have to generate the whole artifact at once</p>

<div class="register-grid practical">
  <div class="register-card quiz fragment" data-fragment-index="1"><strong>QUIZ ME</strong><span>Make a practice test. Do not show the answers yet</span></div>
  <div class="register-card hint fragment" data-fragment-index="2"><strong>GIVE ME A HINT</strong><span>Help with the next step without solving the task</span></div>
  <div class="register-card critic fragment" data-fragment-index="3"><strong>ARGUE AGAINST ME</strong><span>Build the strongest objection to my position</span></div>
  <div class="register-card pupil fragment" data-fragment-index="4"><strong>LET ME TEACH YOU</strong><span>Pretend you do not know; ask me questions</span></div>
  <div class="register-card check fragment" data-fragment-index="5"><strong>CHECK MY WORK</strong><span>Find the first unsupported or incorrect step</span></div>
  <div class="register-card yes-no fragment" data-fragment-index="6"><strong>PLAY YES-AND-NO WITH ME</strong><span>Build the strongest case for both sides before synthesizing</span></div>
  <div class="register-card factcheck fragment" data-fragment-index="7"><strong>FACT-CHECK</strong><span>Separate the claims; verify sources, entailment, and uncertainty</span></div>
  <div class="register-card brainstorm fragment" data-fragment-index="8"><strong>BRAINSTORM WITH ME</strong><span>Generate options without choosing the objective for me</span></div>
  <div class="register-card surprise fragment" data-fragment-index="9"><strong>WHAT SHOULD I KNOW?</strong><span>Tell me something I probably do not know but should</span></div>
</div>

<p class="bottom-line fragment" data-fragment-index="10"><strong>ASK × 9 ⟶ GENERATE × 1</strong> · Generate responsibly, or add more low-quality slop to the noosphere</p>
---


<!-- .slide: data-slide-id="abelard-practical" -->

<p class="eyebrow">ONE REGISTER, SKILL'ED</p>

## “Play yes-and-no” can be an actual SKILL

<div class="abelard-skill-diagram">
  <div class="abelard-pipeline fragment" data-fragment-index="1" aria-label="Attack, triage, synthesize, and attack the synthesis again">
    <div class="abelard-step attack"><strong>ATTACK</strong><span>strongest counterarguments</span></div>
    <div class="abelard-flow-arrow">⟶</div>
    <div class="abelard-step triage"><strong>TRIAGE</strong><div class="triage-tags"><span>LANDS</span><span>STRAW MAN</span><span>VALID BUT ADDRESSED</span></div></div>
    <div class="abelard-flow-arrow">⟶</div>
    <div class="abelard-step synthesis"><strong>SYNTHESIZE</strong><span>preserve valid parts of both</span></div>
    <div class="abelard-flow-arrow">⟶</div>
    <div class="abelard-step reattack"><strong>ATTACK AGAIN</strong><span>test the synthesis</span></div>
  </div>
  <div class="abelard-loop-outcomes fragment" data-fragment-index="1"><span class="iterate">fails ⟲ iterate</span><span class="hardened">survives ⟶ hardened</span></div>
  <div class="abelard-skill-save fragment" data-fragment-index="2">
    <span class="save-label">SAVE · SHARE · LOAD</span>
    <div class="save-arrow">↓</div>
    <div class="skill-file compact">
      <span>~/.agents/skills/abelard/</span>
      <strong>SKILL.md</strong>
      <small>an on-demand, shareable procedure</small>
    </div>
  </div>
</div>

<p class="bottom-line fragment" data-fragment-index="3">A SKILL makes one alternative as easy to invoke as the default; the other registers can become SKILLs too</p>
---



<!-- .slide: data-slide-id="epistemic-honesty" -->

<p class="eyebrow">EPISTEMIC HONESTY · ALSO A CHOICE</p>

## Our <em>epistemic honesty</em> protocol

<div class="honesty-grid">
  <div class="honesty-item status fragment" data-fragment-index="1"><strong>LABEL THE STATUS</strong><span>Known, inferred, or unknown; keep uncertainty visible</span></div>
  <div class="honesty-item check fragment" data-fragment-index="2"><strong>CHECK THE CLAIM</strong><span>Test premises; verify sources, wording, entailment, and date</span></div>
  <div class="honesty-item contrary fragment" data-fragment-index="3"><strong>SEARCH AGAINST IT</strong><span>Find the strongest contrary case</span></div>
  <div class="honesty-item witness fragment" data-fragment-index="4"><strong>NAME THE WITNESS</strong><span>What observation would change the answer?</span></div>
  <div class="honesty-item external fragment" data-fragment-index="5"><strong>EXTERNAL VERIFICATION</strong><span>Not validation: another mind, reproduction, or experiment</span></div>
  <div class="honesty-item excuse fragment" data-fragment-index="6"><strong>EXCUSE YOURSELF EASILY</strong><span>Acknowledge · analyze · log · move on</span></div>
</div>

<p class="bottom-line fragment" data-fragment-index="7">This is <em>my</em> protocol for software development and AI research. Yours may be different</p>
---


<!-- .slide: data-slide-id="axiology" data-spring-layout -->

<p class="eyebrow">AXIOLOGY BEFORE PROMPTING</p>

## What do you actually want?

<div class="purpose-list">
  <div class="fragment" data-fragment-index="1">Get JUST the answer and go to sleep?</div>
  <div class="fragment" data-fragment-index="2">Understand the principle for later?</div>
  <div class="fragment" data-fragment-index="3">Convince Frau Teacher or Herr Boss?</div>
  <div class="fragment" data-fragment-index="4">Explore philosophy with no immediate action?</div>
  <div class="fragment" data-fragment-index="5">Test AI capability or calibration?</div>
  <div class="fragment" data-fragment-index="6">Have some fun?</div>
  <div class="fragment" data-fragment-index="7">Get validation or support?</div>
  <div class="fragment" data-fragment-index="8">Humiliate the AI to feel better?</div>
</div>

<p class="purpose-question fragment" data-fragment-index="9">We are asking the AI to help with <strong>WHAT</strong>?</p>

<p class="bottom-line fragment" data-fragment-index="10">If you do not choose the objective, AI will choose <strong>for you</strong> a plausible default, based on model priors and your register</p>
---


<!-- .slide: data-slide-id="delegation-gradient" -->

<p class="eyebrow">DELEGATION IS A GRADIENT</p>

## The more abstract the question,<br>the more responsibility stays with you

<div class="delegation-stairs">
  <div class="stair s1 fragment" data-fragment-index="1"><strong class="aligned-equation"><span>x² − 3x + 2</span><b>=</b><span>0</span><span>x</span><b>=</b><span>?</span></strong><span>delegate</span></div>
  <div class="stair s2 fragment" data-fragment-index="2"><strong>Install Linux</strong><span>specify + verify</span></div>
  <div class="stair s3 fragment" data-fragment-index="3"><strong>Write an essay</strong><span>own purpose + authorship</span></div>
  <div class="stair s4 fragment" data-fragment-index="4"><strong>What should I ask?</strong><span>own the choice</span></div>
</div>

<p class="bottom-line fragment" data-fragment-index="5">Discuss the border with AI. The decision remains yours</p>
---


<!-- .slide: data-slide-id="working-pyramid" -->

<p class="eyebrow">DEBUG THE STACK</p>

## Which layer limits the result?

<div class="working-stack">
  <div class="working-pyramid" aria-label="A five-level pyramid with LLM at the top, then tools and harness, context, prompt engineering, and intention as the foundation">
    <div class="pyramid-level apex fragment" data-fragment-index="1"><span>5</span><strong>LLM</strong><small><em>capability</em> · can this model do it reliably?</small></div>
    <div class="pyramid-level tools fragment" data-fragment-index="2"><span>4</span><strong>Tools + harness</strong><small><em>access + action</em> · can the system reach and act?</small></div>
    <div class="pyramid-level context fragment" data-fragment-index="3"><span>3</span><strong>Context</strong><small><em>evidence</em> · does the model have the right information now?</small></div>
    <div class="pyramid-level middle fragment" data-fragment-index="4"><span>2</span><strong>Prompt engineering</strong><small><em>specification</em> · did I state the goal, operation, register, and checks?</small></div>
    <div class="pyramid-level foundation fragment" data-fragment-index="5"><span>1</span><strong>Intention</strong><small><em>objective</em> · what do I honestly want? · how will I verify it? · who can help?</small></div>
  </div>
  <div class="pyramid-feedback fragment" data-fragment-index="5" aria-label="AI feedback can help improve every level">
    <strong>AI FEEDBACK</strong>
    <span>probe capability</span><b>↓</b>
    <span>improve tools / harness</span><b>↓</b>
    <span>adjust context</span><b>↓</b>
    <span>refine specification</span><b>↓</b>
    <span>clarify intention</span>
  </div>
</div>

<p class="bottom-line fragment" data-fragment-index="6">The model generates the prose; the whole stack determines whether it is useful</p>
---



<p class="eyebrow">TAKE THESE WITH YOU</p>

## Procedures you can inspect and edit

<div class="take-home-layout">
  <div class="take-home-prompts">
    <div class="take-home-prompt honesty fragment" data-fragment-index="1">
      <strong>EPISTEMIC HONESTY · INSTRUCTIONS</strong>
      <span>Label the status; check the claim; search against it; name the witness; seek external verification; correct openly</span>
    </div>
    <div class="take-home-prompt abelard fragment" data-fragment-index="2">
      <strong>ABELARD · SKILL</strong>
      <span>Attack; triage each objection; synthesize the valid parts; attack again</span>
    </div>
  </div>
  <a class="take-home-qr fragment" data-fragment-index="3" href="https://eodus.github.io/thinking-with-ai/" target="_blank" rel="noopener" aria-label="Open the Thinking with AI take-home page">
    <img src="assets/thinking-with-ai-qr.svg" alt="QR code for the Thinking with AI take-home prompts">
  </a>
  <a class="take-home-url fragment" data-fragment-index="3" href="https://eodus.github.io/thinking-with-ai/" target="_blank" rel="noopener"><code>eodus.github.io/thinking-with-ai/</code></a>
</div>

<p class="bottom-line fragment" data-fragment-index="4">Use them, change them, reject them. They are procedures — not universal truth</p>
---


<!-- .slide: class="closing-questions-slide" -->

<div class="ambient-circle circle-cyan"></div>
<div class="ambient-circle circle-violet"></div>

<div class="closing-message">
  <p class="eyebrow">CLOSING</p>
  <h2>AI can help with almost any question</h2>
  <p class="closing-claim">You remain responsible for <strong>why you asked</strong> — and <strong>what you do with the answer</strong></p>
</div>

<p class="generate-responsibly"><em>Generate responsibly</em></p>

<div class="questions-overlay fragment" data-fragment-index="1">
  <h2>So, questions?</h2>
</div>
