# Instructor Application — Build Specification

**Pars Music Institute. Round 1 intake, self-hosted. Concept stage.**

Labels: `[FACT]` with source · `[ASSUMPTION]` with reasoning · `[JUDGMENT]` as opinion ·
`[UNKNOWN]` with a cheap test.

This replaces the Google Form referenced in section B of the concept brief and covers
Round 1 only. Round 2 (online meeting) and Round 3 (background check) are separate
processes; the handoff copy for both is in section 9.

---

## 0. Six decisions to make before a developer touches this

None of these are large. All of them are cheaper to settle now than to retrofit.

| # | Decision | Why it can't wait | Default if you don't decide |
|---|---|---|---|
| 1 | Call them *instructors*, not *faculty*, and *apply to teach*, not *job application* | Classification exposure — see 0.1 | Use "instructor" |
| 2 | Drop the demographic self-identification section entirely | You almost certainly have no legal obligation to collect it — see 0.2 | Drop it |
| 3 | Video by **link**, not upload | Cost and failure rate — see 0.3 | Link |
| 4 | Photographs move to post-acceptance | Discrimination exposure — see 0.4 | Defer |
| 5 | Background-check consent is a **separate** document, not a checkbox in this form | Legally required to be standalone in the US — see 0.5 | Separate |
| 6 | Which G1 model the compensation questions assume | Changes two questions in step 5 | Model A, per the G1 memo |

### 0.1 Terminology — the one that actually matters

`[JUDGMENT]` You've been describing this as a "job application" for "faculty," and
"faculty" is a nice word that does real damage here. Section D of the agreement
classifies instructors as contractors. The G1 memo flags that Model A already strains
that classification. Application copy that says *job*, *hire*, *employment*, *faculty
member*, *staff*, *position*, or *salary* becomes evidence in exactly the dispute the
memo told you to price before committing.

Use throughout: **instructor** (not faculty), **apply to teach with us** (not job
application), **engagement** or **working with us** (not employment), **rate** (not
salary), **accepted** or **onboarded** (not hired).

This costs you nothing and removes a self-inflicted problem. `[UNKNOWN]` Whether it
is sufficient is part of the same attorney consultation the G1 memo already scoped —
add this as a second sub-question to that one conversation, not a separate one.

### 0.2 Do not copy the self-identification sections

The race/ethnicity, gender, veteran status, and disability (Form CC-305) blocks you
see on large institutions' applications exist because those organisations are US
federal contractors subject to OFCCP reporting. `[ASSUMPTION]` A concept-stage private
music institute is not a federal contractor and has no such obligation — this is worth
one line of confirmation from the same attorney, but the reasoning is straightforward.

If you collect that data without the obligation, you have: no reporting use for it, a
sensitive-data store to secure, a disclosure to write, and — worst — a record showing
you held protected-characteristic data on every applicant you rejected. `[JUDGMENT]`
There is no upside. Leave it out.

The same applies to the arbitration agreement you saw. Do not adapt someone else's
dispute-resolution clause. If you want one, it belongs in the Instructor Services
Agreement at signature, drafted by your attorney — not in an intake form, and not
before an applicant has any relationship with you.

### 0.3 Video by link

Direct video upload means large-file handling, transcoding, storage cost, and a
meaningful share of applicants failing the upload on mobile. Ask instead for an
unlisted YouTube or Vimeo link, or a shared cloud link. `[JUDGMENT]` It is cheaper,
more reliable, and it lets applicants reuse material they already have — which lowers
the effort you're asking for, which is what you said you wanted.

Validate that the URL resolves at submission time and tell them if it doesn't. The
single most common reason a video submission fails review is a permissions setting the
applicant didn't realise was private.

### 0.4 Photographs

The brief lists additional photographs as part of the Round 1 extension.
`[JUDGMENT]` Move them. A photograph collected before a selection decision reveals
race, approximate age, and sex to every reviewer, on every applicant, in a process
where you will later need to explain your rejections. It buys you nothing at Round 1 —
you already have a video, which tells you more about the person than a headshot does.

Collect photographs after acceptance, framed as profile material, when the purpose is
obvious and the selection decision is behind you.

### 0.5 Background check consent (Round 3)

`[FACT]` Under the US Fair Credit Reporting Act, if you use a third-party screening
company, the disclosure must be a **standalone document** containing nothing else —
not bundled into an application, not next to a privacy consent, not beside an
arbitration clause. A combined form is a common and expensive compliance failure.

So: in this form, one sentence telling them a background check happens at the final
stage. The actual disclosure and written authorisation is a separate document served
between Round 2 and Round 3. Some states add their own notice requirements on top.

### 0.6 What the compensation questions assume

The G1 memo recommends Model A (Institute-owned): you set the rate card, you assign
students. Steps 5.3 and 5.4 below are written for that and are, deliberately, the free
experiment the memo asked for. If you have since moved toward Model B, tell me and
those two questions invert — they'd ask what the instructor charges, not whether
they'd accept what you set.

`[UNKNOWN]` Note what this form **cannot** ask: what you pay. G2 is unresolved, so
step 5 asks about *structure* — acceptance of a set rate — and not about *amount*.
That is a real limitation and applicants will notice it. Section 9.2 has holding copy
for when they ask.

---

## 1. Design principles for the form itself

You asked for a tone that doesn't pressure applicants but keeps professional courtesy
intact. Concretely, that means:

- **Required fields are genuinely required.** Everything that is nice-to-have is marked
  optional and *looks* optional. An asterisk on a field you don't need is a small lie
  that costs you completions.
- **No red error styling until submit.** Validate on submit, not while someone is still
  typing their name.
- **Explain why you're asking**, in one short line, for anything non-obvious. People
  answer better questions when they know the use.
- **No time limits, no countdowns, no "applications close soon"** unless it's true.
- **Save and return.** Email the applicant a resume link at the end of each step. This
  form is long; without it your drop-off on step 4 will be severe.
- **Word counts as guidance, not limits.** "A short paragraph is plenty" reads
  differently from "maximum 200 words."
- **Mobile-first.** `[ASSUMPTION]` A meaningful share of working musicians will start
  this on a phone between engagements.

`[JUDGMENT]` On length: you can afford a demanding instructor form. The brief's own
assessment is that supply is the easy side and demand is undefined. A form that takes
twenty-five careful minutes filters for instructors who want *this* specifically, and
your constraint is not applicant volume. Do not make it longer than it needs to be, but
do not cut the matching questions in step 4 to save minutes — they are the reason the
form exists.

**Estimated completion: 20–25 minutes.** Say so at the top. Telling people the true
cost up front is the courtesy; understating it is what makes forms feel hostile.

---

## 2. Step 1 — Getting in touch

Progress indicator: **Step 1 of 5**

> ### Let's start with how to reach you
>
> This takes about 20–25 minutes in total. You can stop at any point — we'll email you
> a link so you can pick up where you left off.

| Field | Type | Required | Label / helper text |
|---|---|---|---|
| Preferred name | Text | Yes | "Preferred name" — helper: "What you'd like us to call you." |
| Legal first name | Text | Yes | "First name (as it appears on official documents)" |
| Legal last name | Text | Yes | "Last name" |
| Pronouns | Text | No | "Pronouns (optional)" — free text, not a dropdown |
| Email | Email | Yes | "Email address" — helper: "Everything about your application comes here." |
| Confirm email | Email | Yes | Prevents the single most common unrecoverable error |
| Phone | Tel + country code | No | "Phone number (optional)" — helper: "Only if you'd rather we call than email." |
| City | Text | Yes | "City" |
| State / region | Select | Yes | "State" |
| Country | Select | Yes | Default to your primary market |
| Postal code | Text | Conditional | Required only if they select package 3 in step 5 — see 5.2 |
| Time zone | Select | Yes | Auto-detect, let them correct. Needed for scheduling from day one. |
| Right to work | Radio | Yes | "Are you legally permitted to work in [country] as an independent contractor?" — Yes / No / Not sure. Helper: "If you're not sure, choose that — it doesn't disqualify you and we'd rather talk it through." |

**Do not collect:** date of birth, age, marital status, nationality or country of
birth, national ID or social security number, photograph, salary history. None of these
are needed at Round 1 and several are prohibited to ask in some jurisdictions.

`[JUDGMENT]` On "salary history" specifically — several US states and cities prohibit
asking. Since under Model A you're setting rates anyway, you have no use for it. Skip it
cleanly rather than adding a jurisdiction-conditional field.

---

## 3. Step 2 — Your background

Progress indicator: **Step 2 of 5**

> ### Your background
>
> We're interested in what you've taught and played, not in a particular kind of
> credential. Fill in what's relevant to you and leave the rest.

### 3.1 Instruments and voice

| Field | Type | Required | Notes |
|---|---|---|---|
| Primary instrument or voice | Select + "other" | Yes | See 3.2 for the list |
| Additional instruments taught | Multi-select | No | Same list |
| Years teaching | Select | Yes | Under 2 / 2–5 / 6–10 / 11–20 / Over 20 |
| Years performing | Select | No | Same bands |

### 3.2 The instrument list

`[ASSUMPTION]` I've built this assuming Persian classical instruments sit alongside
Western ones, reasoning from the Institute's name. Correct me if the scope is
different — this list is the single most visible signal on the form of what kind of
school you are, and getting it wrong will cost you credible applicants immediately.

Group the list under headings rather than presenting one long alphabetical run:

- **Persian / Iranian:** tar, setar, santur, ney, kamancheh, tonbak, daf, oud, qanun,
  robab, Persian vocal (āvāz)
- **Strings:** violin, viola, cello, double bass, classical guitar, acoustic guitar,
  electric guitar, bass guitar, harp
- **Keys:** piano, keyboard, organ, harpsichord, accordion
- **Winds and brass:** flute, clarinet, oboe, bassoon, saxophone, recorder, trumpet,
  trombone, French horn, tuba
- **Percussion:** drum kit, orchestral percussion, hand percussion
- **Voice:** classical, contemporary, musical theatre
- **Theory and composition:** music theory, ear training, composition, arranging,
  songwriting, music production
- **Other** — free text

`[JUDGMENT]` Keep "other" and read what comes in. The instruments your applicants
name that you didn't list are free market research about what your school could offer.

### 3.3 Documents and links

| Field | Type | Required | Label / helper text |
|---|---|---|---|
| Resume / CV | File upload | Yes | "Your CV or resume" — helper: "PDF or Word, up to 10 MB. A plain list of what you've done is completely fine — it doesn't need to be designed." |
| Personal website | URL | No | "Website (optional)" |
| Other links | URL, repeatable, max 3 | No | "Anything else you'd like us to see (optional)" — helper: "Recordings, a teaching page, a profile, a press piece." |
| Formal training | Repeatable group | No | Institution / qualification / field / year completed. Helper on the section: "Optional. Several excellent teachers we'd want to hear from have no formal qualifications at all." |
| Teaching history | Repeatable group | Yes, at least one | Organisation or "independent / private studio" / role / start / end or "current" |
| Languages of instruction | Multi-select + other | Yes | "Which languages can you teach in?" — helper: "This helps us match you with students you can teach comfortably." |

`[JUDGMENT]` The helper text under "formal training" is doing real work. Private music
instruction has excellent teachers without conservatory credentials, and an unqualified
"Education" heading with an asterisk quietly tells them not to bother applying.

---

## 4. Step 3 — Playing and teaching, on video

Progress indicator: **Step 3 of 5**

> ### We'd like to hear you play
>
> This doesn't need to be new, produced, or perfect. An existing recording is completely
> fine, and a phone camera in a practice room is completely fine. We're listening for
> musicianship, not production.

| Field | Type | Required | Label / helper text |
|---|---|---|---|
| Performance video | URL | Yes | "Link to a performance video" — helper: "YouTube, Vimeo, or a cloud link. Unlisted is fine. Please check the link opens for someone who isn't signed in as you." |
| What are we watching? | Textarea | No | "Anything you'd like us to know about it (optional)" — helper: "Piece, when it was recorded, context. A sentence is plenty." |
| Second video | URL | No | "A second link, if you have one (optional)" — helper: "Some instructors like to show accompaniment, ensemble playing, or a different style." |
| Teaching video | URL | No | "A clip of you teaching (optional)" — helper: "Only if you happen to have one. We know most people don't record their lessons, and this isn't expected." |

**Consent, as a checkbox at the bottom of this step:**

> ☐ I'm happy for Pars Music Institute to view these recordings as part of reviewing my
> application.
>
> *We won't publish, share externally, or use these recordings for anything else. If you
> join us and we'd like to use any of your material publicly, we'll ask you separately.*

`[JUDGMENT]` The "we'll ask you separately" line is the courtesy, and it also protects
you. A single blanket media consent collected at application stage from someone who may
never join you is both bad manners and bad practice.

**Validation:** check the URL resolves and is not private, at submit. If it fails, say
so plainly — "This link doesn't seem to open for us. It may be set to private. Would you
check the sharing settings?" — and let them fix it without losing the rest of the form.

---

## 5. Step 4 — How you teach, and who you teach best

Progress indicator: **Step 4 of 5**

> ### How you teach
>
> This is the part we pay the most attention to. We match students to instructors
> deliberately rather than leaving people to guess, and these answers are what we match
> on. There's no preferred answer to any of it — an honest narrow answer is far more
> useful to us than a broad one.

`[JUDGMENT]` **This step is the reason the form exists.** Section B of the brief says the
personality questionnaire is being treated as a screening instrument when it is more
valuable as a matching instrument. That distinction has to be built into the *data
structure*, not just the intention: every question in this step is stored as a
structured field against the instructor record and queried at matching time. If any of
it lands as free-text prose in a PDF nobody reads again, the asset is lost.

Each field below is marked **[M]** where it feeds matching directly.

### 5.1 Who you teach well

| Field | Type | Required | Label / helper text |
|---|---|---|---|
| Age groups **[M]** | Multi-select | Yes | "Which age groups do you teach comfortably?" — Under 8 / 8–12 / 13–17 / 18–25 / 26–60 / Over 60. Helper: "Select as many or as few as apply." |
| Levels **[M]** | Multi-select | Yes | "Which levels?" — Complete beginner / Early / Intermediate / Advanced / Pre-professional or conservatory preparation |
| Student goals **[M]** | Multi-select | Yes | "What are you best at helping students achieve?" — Playing for enjoyment / Steady technical progress / Graded exams / Auditions and competitions / Conservatory or degree preparation / Performance confidence / Improvisation / Composition and songwriting / Returning after a long break |
| Repertoire and styles **[M]** | Multi-select + other | Yes | Persian classical / Persian folk and regional / Western classical / Jazz / Pop and contemporary / Rock / Musical theatre / Film and game music / Traditional and folk (other) / Sacred and liturgical |
| Additional experience **[M]** | Multi-select | No | "Do you have experience teaching any of these? (optional)" — Students with learning differences / Neurodivergent students / Students with physical disabilities affecting playing / Students with hearing differences / Adult beginners who are nervous about starting / Students learning in a second language |

`[JUDGMENT]` That last field is high-value and needs careful framing. It must read as an
invitation, never as a requirement, and the answers must be treated as a matching
capability rather than a screening credit — an instructor who leaves it blank is not a
worse instructor.

### 5.2 Who you'd rather not teach — the highest-signal question on the form

> **Are there students you'd prefer we didn't match you with?**
>
> Every instructor has these, and telling us is genuinely helpful rather than a mark
> against you. Knowing where you don't want to work means we won't send you students
> you'd struggle to serve, and it means those students go to someone better suited.

| Field | Type | Required | Notes |
|---|---|---|---|
| Would rather not teach **[M]** | Multi-select | No | Mirror the lists above: age groups, levels, goals, styles. Framed as "I'd rather not be matched with…" |
| Anything else **[M]** | Textarea | No | "Anything else about fit you'd like us to know (optional)" |

`[JUDGMENT]` The brief calls what an instructor says about which students they want the
highest-signal structured data you collect. Two consequences for the build. First, it
has to be **structured** — a mirrored multi-select, not a paragraph, or it can't be
queried. Second, the framing has to make declining *safe*. If applicants suspect that
narrowing their range reduces their chance of acceptance, they will claim to teach
everyone, and this field becomes noise instead of your best asset.

### 5.3 Approach

| Field | Type | Required | Label / helper text |
|---|---|---|---|
| Teaching approach | Textarea | Yes | "How would you describe the way you teach?" — helper: "A short paragraph is plenty. We're interested in how you actually work, not in a philosophy statement." |
| First lesson | Textarea | Yes | "What does a first lesson with a new student usually look like for you?" — helper: "A few sentences." |
| A student who struggled | Textarea | No | "Tell us about a student who found something difficult, and what you did (optional)" — helper: "This one tells us more than almost anything else, but it's optional if nothing comes to mind." |
| Materials | Textarea | No | "Do you work from particular methods, books, or materials? (optional)" |

### 5.4 Former students — outcome evidence

> **Have any of your former students gone on to study or work in music?**
>
> This is optional. We ask because we intend to keep a proper record of where students
> end up, and instructors' past students are part of that story. We won't contact anyone
> without asking you first.

| Field | Type | Required | Notes |
|---|---|---|---|
| Any such students? | Radio | No | Yes / No / Not sure |
| Details | Repeatable group, max 5 | Conditional on Yes | What they went on to do / roughly when / how long you worked together. Helper: "No names needed at this stage." |
| Consent to follow up | Checkbox | No | "☐ If we'd like to record any of this properly later, you're welcome to ask me about it." |

`[JUDGMENT]` Section C of the brief says outcome evidence is the only credibility claim
competitors can't replicate by writing copy, and that it should be consented,
structured, and continuously collected from day one. **This is day one.** Every
instructor you accept arrives carrying a history you will otherwise never systematically
capture — and capturing it at application costs you one optional field. Note the
deliberate restraint: no names, no contact details, no publication consent. You are
establishing the *record*, and asking permission to have a conversation later. Trying to
secure publishable testimony from a stranger mid-application would be both premature and
off-putting.

---

## 6. Step 5 — Practicalities

Progress indicator: **Step 5 of 5**

> ### How you'd like to work with us
>
> Some of this is still taking shape on our side, and we'll be straightforward with you
> about what's settled and what isn't.

### 6.1 Which packages

| Field | Type | Required | Label |
|---|---|---|---|
| Formats **[M]** | Multi-select | Yes | "Which of these would you be interested in teaching?" |

Options, worded as the student experiences them:

- **Online lessons** — "Taught remotely by video."
- **At your own teaching space** — "Students come to you."
- **At the student's location** — "You travel to the student, or to a space we arrange."
- **Group lessons** — "Small groups, in selected areas."

Helper under the group option: *"Group teaching is something we're building out, and
availability varies by area."* `[JUDGMENT]` This is honest — the brief describes
package 4 as the least developed — and it avoids an applicant accepting on the strength
of group work that isn't there yet.

### 6.2 Travel — conditional, only if "at the student's location" is selected

| Field | Type | Required | Label / helper text |
|---|---|---|---|
| Travel distance | Select | Yes | "How far would you be willing to travel for a lesson?" — Up to 5 miles / 5–10 / 10–20 / 20–30 / Over 30 / Depends, let's discuss |
| Transport | Select | No | "How would you usually travel? (optional)" — Own vehicle / Public transport / Either |
| Areas | Textarea | No | "Any specific areas you'd prefer, or prefer to avoid? (optional)" |

`[UNKNOWN]` **This data resolves G4.** The brief notes travel reimbursement is currently
"dependent on circumstances," which isn't a policy, and that package 3 can't be priced
until it's a formula. Once fifty applicants have answered this, you have a real
distribution of willing travel radii — which is most of what you need to decide whether
travel is absorbed, surcharged to the student, or capped. **Cost: one conditional
field.** It is the second-cheapest test in this document.

### 6.3 Availability

| Field | Type | Required | Label |
|---|---|---|---|
| Weekly hours | Select | Yes | "Roughly how many hours a week would you like to teach?" — Up to 5 / 5–10 / 10–20 / Over 20 / Flexible |
| General availability | Checkbox grid | Yes | Weekday mornings / afternoons / evenings; weekend mornings / afternoons / evenings. Helper: "Rough is fine — we'll work out specifics together." |
| Start | Select | Yes | "When could you start?" — Immediately / Within a month / Within three months / Later or unsure |

`[JUDGMENT]` Do not ask for a precise weekly schedule grid at application stage. It is
the most tedious thing you could ask of someone you haven't spoken to, it changes
constantly, and you need it at onboarding, not at intake.

### 6.4 The two questions that are actually an experiment

These are written for Model A. They are the G1 memo's Test #2, embedded where it costs
nothing to run.

> **Two things about how we work**
>
> We'd rather tell you these now than after you've spent time with us.

| Field | Type | Required | Content |
|---|---|---|---|
| Assignment | Radio | Yes | "We match students to instructors ourselves, based on teaching style and what the student is looking for, rather than having students browse profiles and pick. How does that sit with you?" — *That works well for me* / *I'm open to it* / *I'd have questions about it* / *I'd prefer students chose me directly* |
| Assignment comment | Textarea | No | "Anything you'd like to add? (optional)" |
| Rate structure | Radio | Yes | "We set lesson prices centrally and pay instructors an agreed rate per lesson, rather than instructors setting their own prices. How does that sit with you?" — same four options |
| Rate comment | Textarea | No | "Anything you'd like to add? (optional)" |
| Current rate | Text | No | "What do you currently charge for a private lesson, if you teach independently? (optional)" — helper: "Only if you're comfortable sharing. It helps us understand the market we're working in." |

`[JUDGMENT]` **Read these answers as data, not as screening.** The distribution is the
finding. If most applicants pick the first two options, Model A is viable on the supply
side and the G1 memo's recommendation survives its main practical test. If a large share
pick the last, you have learned — before building anything, from real respondents — that
your instructor supply expects Model B, and G1 reopens on evidence rather than argument.

`[UNKNOWN]` The optional current-rate field is the cheapest partial input to **G2** in
this entire document. It doesn't give you a price. It gives you the floor your
instructor rate has to clear to be worth their time, from the only market participants
you currently have access to. Fifty responses and you can stop guessing about one side
of the split.

Do **not** ask "what are your rate expectations?" Under Model A you set the rate, so
asking implies a negotiation you don't intend to have, and it invites an anchor you'll
then have to walk back.

### 6.5 How they found you

| Field | Type | Required | Label |
|---|---|---|---|
| Source | Select + other | No | "How did you hear about us? (optional)" — Someone I know / Social media / Search / A music school or organisation / An advertisement / Other |

`[JUDGMENT]` Keep it optional and keep it short, but keep it. `[UNKNOWN]` **G5 is
undefined for students, and this field is the only acquisition data anywhere in the
plan.** The channels that reach instructors are not the channels that reach students —
but they are the first evidence you'll have that any channel reaches anyone, and the
question of which one converts is the one the whole business is missing.

---

## 7. Consent and submission

> ### Before you send this
>
> **How we handle your information.** We'll use what you've shared to review your
> application and, if we go ahead together, to match you with students. We keep it
> secure, we don't sell it, and we don't share it outside the Institute. If your
> application doesn't go ahead, we'll keep your details for [12 months] in case
> something suitable comes up, and you can ask us to delete them at any time by emailing
> [privacy address].
>
> **What happens next.** We read every application ourselves. You'll hear from us within
> [10 working days] either way. If we'd like to take things further, we'll invite you to
> a video conversation. There's a final background check before anyone starts teaching,
> and we'll explain that properly at the time.
>
> ☐ I confirm the information here is accurate to the best of my knowledge.
> ☐ I've read how my information will be handled and I'm happy to proceed.
>
> [ Send application ]
>
> *Thank you for the time this took.*

**Notes on the above:**

- `[UNKNOWN]` The bracketed retention period and response window are yours to set. Set
  them to something true. A stated ten-day window you miss is worse than a stated
  three-week window you meet.
- The accuracy confirmation replaces the long misrepresentation clause you'll see on
  large institutional forms. `[JUDGMENT]` The full version — misrepresentation is
  grounds for termination, offers contingent on the selection process, credentials will
  be verified — belongs in the Instructor Services Agreement, where there's a
  relationship to condition. In an intake form it reads as suspicion of someone who has
  just spent twenty-five minutes helping you.
- **One consent per purpose.** Don't bundle privacy, media use, and background checks
  into a single checkbox. Separate consents are both better practice and, for the
  background check, required.
- Two checkboxes is the maximum here. Every additional one dilutes all of them.

---

## 8. What happens behind the form

### 8.1 Storage

You've said no third-party ATS, which means these responsibilities land on you:

- **Encryption at rest and in transit**, for the whole application store.
- **Access control.** Named reviewers only. Log who opened which application.
- **Deletion on request**, actually working, within your stated retention period.
- **A privacy notice** on your site that matches what the form promises. `[JUDGMENT]`
  Applicants in the UK or EU carry data-protection rights with them regardless of where
  you're based; if you expect any, the notice needs to reflect that.
- **Backups**, tested. A self-hosted applicant database with no restore path is a single
  disk failure away from losing your entire pipeline.

`[JUDGMENT]` Self-hosting is the right call for the reason you gave — the matching data
in step 4 is a core asset and shouldn't sit in someone else's product. But be clear that
you've taken on a security obligation, not just saved a subscription. `[UNKNOWN]` A
sensible middle path: self-host the form and the data, use a managed database with
encryption and automated backups rather than rolling your own. Cheap test — one
conversation with whoever is building your site, scoped to "what's our backup and
deletion story?" Under an hour.

### 8.2 Structure the data for matching from the start

Every field marked **[M]** stores as a discrete, queryable value. Not a PDF. Not a
concatenated string. Not a paragraph a reviewer reads once and forgets.

`[JUDGMENT]` This is the single most consequential build instruction in this document.
Section B of the brief says the questionnaire should flow into student–instructor
matching, and the G1 memo argues matching is the only capability in the material that
compounds with volume. **Both are true only if the data is stored as data.** If step 4
lands as prose in a document store, you'll have collected the right information in a
form you can never use, and you won't discover it until you have three hundred
instructors and no way to search them.

Reviewer notes and scores attach to the record separately, never overwriting what the
applicant wrote.

### 8.3 Review

Score against the same short rubric every time and record it:

1. Musicianship (from the video)
2. Teaching evidence (from history and the written answers)
3. Clarity of fit (from step 4 — is it clear who this person teaches well?)
4. Practical match to current need (formats, availability, area)

`[JUDGMENT]` Criterion 3 is not "breadth." An applicant who tells you clearly that they
teach advanced adult students and nobody else scores *well*, because they've handed you
matching signal. Under Model A, a legible instructor is worth more than a flexible one.

Two reviewers on anything you're inclined to reject. `[FACT]` Review time is already on
your cost list in section E of the brief — this makes it real, and it's why the form
shouldn't be so easy to submit that you drown.

---

## 9. Copy for the rest of Round 1

### 9.1 Confirmation email, sent immediately

> **Subject:** We've got your application — Pars Music Institute
>
> Hello [preferred name],
>
> Thank you for applying to teach with us, and for the time it took — we know it wasn't
> a short form.
>
> We read every application ourselves rather than filtering them automatically, so it
> takes us a little while. You'll hear from us within [10 working days] whichever way it
> goes.
>
> If anything changes in the meantime, or you'd like to add something, just reply to
> this message.
>
> With best wishes,
> [Name]
> Pars Music Institute

### 9.2 If they ask about pay before you've settled G2

`[UNKNOWN]` They will ask, and the honest answer is better than an evasive one.

> We're still finalising our rates, and I'd rather give you a real number than a vague
> one — so I don't want to quote before it's settled. What I can tell you is how it
> works: we set lesson prices and pay instructors an agreed rate per lesson, so you're
> not setting or collecting prices yourself. I'll come back to you with specifics as
> soon as they're fixed, and nothing would be agreed without them.

`[JUDGMENT]` This is usable for perhaps two more months. After that, applicants who
can't get a number will stop applying, and the good ones will stop first. **G2 has a
deadline now, and this form is what sets it.**

### 9.3 Interview invitation (Round 2)

> **Subject:** We'd love to talk — Pars Music Institute
>
> Hello [preferred name],
>
> We enjoyed your application and your playing, and we'd like to arrange a conversation.
>
> It's about [30–40] minutes by video with [names and roles]. We'd like to hear more
> about how you teach, and there'll be plenty of room for your questions about us —
> we'll be straightforward about what's settled and what we're still working out.
>
> There's nothing to prepare. Here are some times that work on our side: [link or
> options]. If none suit, tell us what does.
>
> With best wishes,
> [Name]

### 9.4 Declining

Write these individually and send them. `[JUDGMENT]` Music teaching communities are
small and connected, and how you decline people is part of your reputation with the
supply side you depend on. A short, warm, specific note costs three minutes.

> Hello [preferred name],
>
> Thank you for applying, and for letting us hear you play. We won't be taking things
> further at this stage — [one honest, specific sentence].
>
> We're keeping your details on file for [12 months] in case something more suitable
> comes up, and you're very welcome to apply again. Just tell us if you'd rather we
> didn't keep them.
>
> With best wishes,
> [Name]

---

## 10. Build sequence

| # | Task | Depends on |
|---|---|---|
| 1 | Settle the six decisions in section 0 | Nothing |
| 2 | Confirm the instrument list (3.2) | Your scope, not mine |
| 3 | Set the bracketed values: response window, retention period, interview length | Nothing |
| 4 | Build the data model first — the **[M]** fields as structured columns | Decisions 1–3 |
| 5 | Build steps 1–5 with save-and-return | Data model |
| 6 | Privacy notice matching the form's promises | Step 5 |
| 7 | Email templates (section 9) | Nothing |
| 8 | Test end to end on a phone, including a private video link, an abandoned session resumed a day later, and a deletion request | Everything |
| 9 | Soft launch to the candidates already in your pipeline | Everything |

`[JUDGMENT]` Step 9 is the point. The G1 memo's Test #2 — will instructors accept
assigned students at a set rate — is answered by section 6.4 the moment ten real
candidates complete this. You already have the respondents. This form is how you reach
them.

---

## What this document does not do

- **It does not resolve G2.** Section 6.4's optional rate field gives you the instructor
  side of the split from real respondents. The student-facing price is untouched, and
  section 9.2 is a holding position with roughly a two-month shelf life.
- **It does not touch G5.** Section 6.5 collects an acquisition channel for
  *instructors*, which is not the same population and not the same problem. The student
  pipeline still does not exist on paper.
- **It does not draft or expand the Instructor Services Agreement**, per section D of
  the brief. Where I've said something belongs in the agreement rather than the form —
  arbitration, misrepresentation terms, media consent — that's a placement note, not a
  draft.
- **It assumes Model A**, per the G1 memo's recommendation, in exactly two questions
  (6.4). Everything else works under any model.
- `[UNKNOWN]` **It has not been reviewed by an attorney.** The classification wording
  (0.1), the self-identification omission (0.2), and the background-check sequencing
  (0.5) are all reasoning, not legal advice. Fold them into the single consultation the
  G1 memo already scoped rather than booking a second one.
