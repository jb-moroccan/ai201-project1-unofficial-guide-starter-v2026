# The Unofficial Guide

Jenna Bousellam, corpora: campus_life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

I picked the campus_life corpus because I liked that it has several source doucments and I wanted to build questions that required combining multiple sources to produce the correct answer. The kinds of questions my system should answer are related to quietness in dorms, wait times in dining halls, classes with the most work, and classes with the most exams. These are questions that the typical college pamphlets won't provide but are the things you actually care about as a college student. 

## Chunking Strategy

**Chunk size: 150**
**Overlap: 0**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

I chose a chunk size of 150 because I wanted a sentence based approach for my chunks as I noticed in the corpora, separate thoughts tended to be in their own senetence. I asked Claude if it had an idea for a specific number and it suggested 150 because it keeps most single sentences intact (your chunks range from ~50 to ~120 chars), it allows slightly longer thoughts to stay together if needed, and it maintains readability without becoming too large. I liked the chunks that it produced with 150 chars originally but wanted to check if a lower number like 80 or even 100 would give me similar results. When I did that, I got answers like: That's real time, not optimistic time. This is not a thought that can tell me anything independently, so I went back up to the original 150 characters. I used 0 overlap because of the same thought that each idea was in its own sentence, so I wouldn't actually want any overlap in thought from one sentence to another. 

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all five for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week.
```

**Chunk 2** — source: `course_cs_210.txt#2` — produced by: `chunker.py::split_documents`

```
Expect 8 to 10 hours a week outside class. The one piece of advice: do the labs even though they're only 10% — the exams reuse the lab problems.
```

**Chunk 3** — source: `course_phys_130_workload.txt#1` — produced by: `chunker.py::split_documents`

```
It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_verrill_street_grill.txt#0` — produced by: `chunker.py::split_documents`

```
Verrill Street Grill

I'm a junior and I've done this twice now. Wait times: up to 30 minutes on Friday evenings, otherwise under 10.
```

**Chunk 5** — source: `housing_morrow_house.txt#1` — produced by: `chunker.py::split_documents`

```
Rooms are singles and doubles, hall bathrooms. The good: cheapest housing tier by about $900 a year, and the singles are real singles.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question: Which classes have the most amount of outside class work each week?**

**Answer:**

```
Based on the documents, BIOL 160 has the most outside class work, requiring 9 to 11 hours a week. This comes from the document `course_biol_160.txt`.

Sources retrieved: advising_registration.txt, course_biol_160.txt, course_cs_210.txt, course_cs_210_workload.txt, course_econ_101.txt, course_econ_101_workload.txt, course_stat_150.txt, course_stat_150_workload.txt, money_jobs.txt

1 model calls this session, 490 tokens (444 in, 46 out)
```

**My relevance cutoff: 0.45**

I used 0.45 as the cutoff because any question from outside the corpus has a distance value of 0.765 or higher while anything within the corpus has a distance value of 0.425 or lower. The 0.45 value keeps all questions that have answers in the corpus within range while keeping a wide enough gap between non-relevant questions that should always return no answers.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| What campus dorms have the best study environment if I need no noise? | In corpus | 0.425 |
| Which dining halls have wait times that never exceed 20 minutes? | In corpus | 0.421 |
| Which classes have the most amount of outside class work each week? | In corpus | 0.356 |
| What's the best dorm to stay in if I want to be near a dining hall? | In corpus | 0.353 |
| Which course has the most exams during a semester? | In corpus | 0.421 |
| What is the capital of Mongolia? | Not in corpus | 0.790 |
| How do I change the oil in a diesel engine? | Not in corpus | 0.848 |
| Who won the 1994 World Cup? | Not in corpus | 0.765 |
| What is the recommended dosage of ibuprofen for a headache? | Not in corpus | 0.791 |
| How do I write a for loop in Rust? | Not in corpus | 0.831 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

I asked Claude to write the chunking function for me based on the idea that I wanted chunks split by sentence with an overlap of 0 since I believe each thought in the sources really ended at each sentence so each chunk shouldn't lead into another thought. Claude provided the overall structure, splitting it where a period is. What I changed is that I needed a specific number for the chunk size and Claude didn't provide that initially so I added that in.

**2.**

I asked Claude to help with me determining an appropriate chunk size since I knew I wanted it split by sentence but wasn't sure the character count that would be best. It initially suggested 150 characters because it kept most single sentences intact and maintained that readability I was looking for when splitting my chunks by sentence. I validated Claude's suggestion by trying character values that were lower like 80 and 100 to see if those would be sufficient, and they had incomplete thoughts in each chunk, so I ended up sticking with the 150 character limit.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | /5 | /5 | /5 | MET or MISSED |
| 2. Every answer names a source | 5 of 5 | /5 | /5 | /5 | MET or MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. 2 separate questions' answers should not be present in 1 single chunk | 5 of 5 | /5 | /5 | /5 | MET or MISSED |
| 5. Each answer provided links back to a minimum of 1 source document | 5 of 5 | /5 | /5 | /5 | MET or MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

run_eval.py is the function that produced all these responses

### What campus dorms are built for quiet studying? — run 2

- Best distance: 0.4120 (passed the gate)
- Sources retrieved: dining_the_ridgeway_cafe.txt, housing_aldridge_hall_noise.txt, housing_calder_annexe_noise.txt, housing_fenwick_court.txt, housing_fenwick_court_noise.txt, housing_innisfree_hall.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt, study_library_hours.txt

```
Based on the provided documents, there is no mention of any dorms being built specifically for quiet studying. However, documents `housing_aldridge_hall_noise.txt`, `housing_fenwick_court_noise.txt`, and `housing_calder_annexe_noise.txt` note that people living in those buildings end up going to the library to work because it is open until 2am during term.
```

### Which dining halls have wait times that never exceed 20 minutes? — run 2

- Best distance: 0.4214 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe_followup.txt, dining_verrill_street_grill.txt, dining_verrill_street_grill_followup.txt

```
Based on the provided documents, Halden Hall rarely has wait times of more than 8 minutes, even at noon (dining_halden_hall.txt). Verrill Street Grill has wait times under 10 minutes, except on Friday evenings when they go up to 30 minutes (dining_verrill_street_grill.txt).
```

### Which classes have the most amount of outside class work each week? — run 2

- Best distance: 0.3563 (passed the gate)
- Sources retrieved: advising_registration.txt, course_biol_160.txt, course_cs_210.txt, course_cs_210_workload.txt, course_econ_101.txt, course_econ_101_workload.txt, course_stat_150.txt, course_stat_150_workload.txt, money_jobs.txt

```
BIOL 160 has the most outside class work, requiring 9 to 11 hours a week (course_biol_160.txt).
```

### What's the best dorm to stay in if I want to be near a dining hall? — run 2

- Best distance: 0.3528 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_pellew_dining_hall.txt, dining_verrill_street_grill.txt, housing_aldridge_hall.txt, housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_morrow_house.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt

```
I don't have enough information to answer your question from the provided documents.
```

### Which course has the most exams during a semester? — run 2

- Best distance: 0.4211 (passed the gate)
- Sources retrieved: admin_graduation_requirements.txt, advising_registration.txt, course_biol_160.txt, course_biol_160_workload.txt, course_cs_210_exams.txt, course_math_220.txt, course_math_220_exams.txt, course_phys_130.txt, money_textbooks.txt

```
I do not have enough information to answer which course has the most exams during a semester.
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
