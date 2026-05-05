# find-bad-review

`find-bad-review` is a reusable skill for researching representative public bad reviews about a product across channels such as Amazon, Chewy, Walmart, Reddit, TikTok, and brand or retailer sites.

The core workflow lives in [skills/find-bad-review/SKILL.md](skills/find-bad-review/SKILL.md).

## Install

Install to both Codex and Claude Code from GitHub:

```bash
npx skills add xolarvill/find-bad-review --skill find-bad-review -a codex -a claude-code -g
```

Install only to Codex:

```bash
npx skills add xolarvill/find-bad-review --skill find-bad-review -a codex -g
```

Install only to Claude Code:

```bash
npx skills add xolarvill/find-bad-review --skill find-bad-review -a claude-code -g
```

If your environment prefers copies instead of symlinks:

```bash
npx skills add xolarvill/find-bad-review --skill find-bad-review -a codex -a claude-code -g --copy
```

## Use

In Codex:

```text
$find-bad-review Analyze the public bad reviews for a dog leash across Amazon, Chewy, Walmart, Reddit, TikTok, and brand sites.
```

In Claude Code:

```text
/find-bad-review Analyze the public bad reviews for a dog leash across Amazon, Chewy, Walmart, Reddit, TikTok, and brand sites.
```

## What the skill does

It guides the agent to:

1. Confirm the product target
2. Search public channels
3. Collect negative evidence
4. De-duplicate and cluster complaints
5. Pick representative examples
6. Turn the fact pattern into business judgments
7. Write a compact report with confidence and gaps

This is optimized for human-triggered, evidence-backed research. It is not a full crawler, review API, or login-based collection system.

## What we learned from real runs

- Broad category prompts can be surprisingly valuable, but mainly as `direction-finding` runs.
- In a broad category, the best outcome is often not "here are the top complaints," but "here is the complaint-heavy subtype you should investigate next."
- Narrower prompts usually produce stronger, more decision-ready outputs than very broad prompts.

In practice:

- `dog leash` worked well because the run surfaced `retractable leashes` as a distinct complaint-heavy subtype.
- `dog collar` worked best as a category-mapping run: it separated `standard collars`, `bark/training collars`, and `smart/GPS collars`, then showed that the functional subtypes carry very different complaint structures.

Use the skill in two modes:

1. `Category scan`
   Use a broad term like `dog collar` when you want to discover the real battleground inside the category.
2. `Subtype decision`
   Follow up with a narrower term like `gps dog collar`, `bark collar`, or `standard dog collar` when you want conclusions that are closer to a merchandising or product decision.

As a rule of thumb, broad-category runs are great for:

- finding complaint-heavy subtypes
- spotting structurally weak product formats
- generating commercially useful follow-up questions

Narrower runs are better for:

- evaluating a specific subtype
- comparing likely hero-SKU directions
- making a more concrete product or positioning judgment

## Tutorial example

### Prompt

```text
$find-bad-review Analyze the public bad reviews for a dog leash across Amazon, Chewy, Walmart, Reddit, TikTok, and brand sites. Focus on representative complaint themes, not generic sentiment.
```

### Process used in this example

1. Confirmed the product target as the broad `dog leash` category, with special attention to retractable leashes because that subtype surfaced the strongest public negative evidence.
2. Searched public retailer review pages and community discussion using complaint-oriented queries.
3. Collected only public, attributable negative evidence.
4. Clustered repeated complaints into concrete failure modes instead of generic labels.
5. Marked channel gaps where public evidence was weak or hard to verify in this pass.

### Coverage in this sample run

| Channel | Result |
| --- | --- |
| Amazon | Weak public sample in this pass |
| Chewy | Strong |
| Walmart | Strong |
| Reddit | Strong |
| TikTok | Weak public sample in this pass |
| Brand / retailer sites | Limited beyond Chewy and Walmart in this pass |

### Category-level readout

- `Retractable leashes` emerged as a distinct high-complaint subtype inside the broader `dog leash` category.
- The strongest negative signal was not around style or price, but around `failure under use`: retraction failure, lock failure, and loss of handler control.

### Commercial judgments

- Retractable leashes appear to be a structurally complaint-heavy subcategory, not just a few bad listings.
- For this category, reliability and control look more commercially important than aesthetics.
- Standard leashes may offer a cleaner broad-market merchandising story because the complaint pattern is narrower and less severe.

### Representative findings

#### 1. Retractable mechanism failures are a recurring complaint

- Chewy examples describe lines twisting, shredding, or failing to retract, and lock buttons that stop working.
- Walmart examples show similar issues: leash material breaking, retractors failing after a short period, and stop buttons breaking.
- This is the clearest repeated bad-review pattern in the public sample.

Confidence: `high`

Example pages:

- [Chewy: Frisco Retractable Dog Leash reviews](https://www.chewy.com/frisco-retractable-dog-leash/product-reviews/768902)
- [Chewy: Hyper Pet Retractable Dog Leash reviews](https://www.chewy.com/hyper-pet-retractable-dog-leash/product-reviews/149219)
- [Walmart: Retractable Dog Leash 16ft reviews](https://www.walmart.com/reviews/product/408047039)

### 2. Safety risk is a top concern, not just product annoyance

- Reddit discussions repeatedly frame retractable leashes as a control and injury risk.
- Common complaints include friction burns, difficulty pulling a dog back quickly, dropped handles scaring the dog, and failures in high-risk situations.
- This theme matters because even less-frequent failures can have higher severity than comfort complaints.

Confidence: `high`

Example pages:

- [Reddit: Are retractable leashes bad?](https://www.reddit.com/r/dogs/comments/zxtynv/are_retractable_leashes_bad/)
- [Chewy: My Bestie Retractable Dog Leash reviews](https://www.chewy.com/my-bestie-retractable-dog-leash/product-reviews/394114)

### 3. Hardware durability and clip reliability also show up outside retractable mechanics

- Chewy examples for non-retractable leashes mention carabiner or clip failures and repeated hardware defects.
- This suggests that for standard leashes, the key negative theme is not retraction but attachment-point reliability.

Confidence: `medium`

Example pages:

- [Chewy: Tuff Mutt Dual Handle Rope Dog Leash reviews](https://www.chewy.com/tuff-mutt-dual-handle-rope-dog-leash/product-reviews/213679)
- [Chewy: The Foggy Dog Onyx Marine Rope Dog Leash reviews](https://www.chewy.com/foggy-dog-onyx-marine-rope-dog-leash/product-reviews/212616)

### Abridged result

For `dog leash`, the most representative public bad-review themes were:

- retractable leash does not retract smoothly or stops retracting
- lock or brake mechanism breaks
- leash or tape shreds or breaks too early
- hardware or clip failure can create a safety issue
- retractable format reduces handler control in fast or crowded situations

The strongest cross-channel pattern was that negative feedback was more specific and more serious around `failure under use` than around aesthetics or price.

## Repo layout

- `skills/find-bad-review/`: main skill
- `platforms/`: portability notes for Codex and Claude Code
- `examples/`: sample output shape
