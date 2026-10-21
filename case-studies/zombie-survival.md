# Zombie survival RL: making rewards trustworthy

This case study explains one engineering problem in the [zombie-survival reinforcement-learning project](https://github.com/Sandeshkumar0/reinforcement_learning): ensuring that PPO receives rewards from events that actually happened.

## The problem

The engine exposed mutable world objects in both the previous and current state. Because the two states could point to the same entities, changes such as zombie damage or human death appeared in both snapshots. Reward calculations based on the difference between them could therefore miss the event entirely.

Combat also had timing problems. A zombie could resolve a lethal attack before a bomber's rescue action, and an explosion could apply damage repeatedly while its animation remained visible.

## The design

Each step now follows a deterministic sequence:

```text
cooldowns -> human movement/escape -> zombie targeting/movement
          -> bomber detonation -> attacks by surviving zombies
```

The engine returns detached state snapshots and immutable combat events. Every damage event records its actor, target, actual HP removed, and whether the zombie was threatening a human. Explosion damage is applied once at detonation, capped by the zombie's remaining health, and kills are credited once to the responsible bomber.

Observations use stable entity IDs, normalized values, fixed-size padded slots, and presence masks. They include human and zombie health, zombie target and threat state, bomber cooldown, and collision rays for nearby obstacles.

## Verification

The regression suite covers state snapshots, damage, death and escape rewards, threat eligibility, cooldowns, one-shot explosions, same-step rescue, kill attribution, outcomes, seeded resets, observation masks, and zero-zombie navigation episodes. It also runs short real PPO updates and checks save, load, resume, frozen human weights, training-loss logs, and reproducible evaluation.

A 1,024-step smoke run for each policy completed the end-to-end pipeline. Across ten fixed evaluation seeds, the short-trained pair escaped more often than the random pair, but zombie damage stayed equal and invalid explosion attempts increased. The project therefore records the run as an integration check, not evidence of a reliably improved policy.

- [Source repository](https://github.com/Sandeshkumar0/reinforcement_learning)
- [Regression tests](https://github.com/Sandeshkumar0/reinforcement_learning/tree/main/tests)
- [Smoke-test report](https://github.com/Sandeshkumar0/reinforcement_learning/blob/main/logs/smoke_v2/REPORT.md)
- [Per-episode comparison](https://github.com/Sandeshkumar0/reinforcement_learning/blob/main/logs/smoke_v2/comparison.csv)
