# Hi, I'm Sandesh

I'm a full-stack developer who enjoys turning product ideas into complete systems—from interfaces and APIs to data models and tests. My own projects include a car-rental prototype, an education portal, and a reinforcement-learning simulation.

[Portfolio](https://sandesh-portfolio-seven.vercel.app/) · [Email](mailto:sandeshkr07@gmail.com) · [GitHub](https://github.com/Sandeshkumar0)

## What I work with

- **Frontend:** JavaScript, TypeScript, React, Next.js, HTML, CSS, Tailwind CSS
- **Backend and data:** Python, Django, REST APIs, PostgreSQL, MongoDB
- **Testing and experiments:** pytest, Gymnasium, Stable-Baselines3/PPO

These are technologies used in my repositories. I care about making the setup and limitations as clear as the features.

## Selected projects

| Project | Engineering focus |
| --- | --- |
| [AeroDrive](https://github.com/Sandeshkumar0/aerodrive_rental) | React and Django rental workflows covering fleet browsing, reservations, OTPs, document uploads, and simulated driver monitoring. |
| [Abacus](https://github.com/Sandeshkumar0/abacus) | A Django education portal with student, teacher, and parent roles, relational data models, assessments, and notifications. |
| [Zombie survival RL](https://github.com/Sandeshkumar0/reinforcement_learning) | Cooperative PPO policies with event-based rewards, deterministic combat, reproducible evaluation, and regression tests. |

## Engineering case study

### Making reinforcement-learning rewards trustworthy

The zombie-survival project had a subtle state-aliasing bug: previous and current states shared mutable objects, so damage and reward deltas could disappear. I replaced those shared references with detached snapshots and immutable combat events, then made the simulation order explicit so a bomber can rescue a human before a lethal zombie attack in the same step.

The result includes one-shot explosion damage, per-bomber damage and kill attribution, stable padded observations, seeded resets, checkpoint resume support, and **24 deterministic regression tests**. A short PPO smoke run is documented honestly: it verifies the full training path, while its mixed results are treated as evidence for more training rather than proof of a strong policy.

[Read the full case study](https://github.com/Sandeshkumar0/Sandeshkumar0/blob/main/case-studies/zombie-survival.md) · [See the implementation](https://github.com/Sandeshkumar0/reinforcement_learning) · [Review the smoke-test report](https://github.com/Sandeshkumar0/reinforcement_learning/blob/main/logs/smoke_v2/REPORT.md)

## Currently working on

Improving the zombie-survival simulation's training curriculum and evaluation, while making each project easier to understand and run from a fresh clone.

## Team projects

- [Graviton](https://github.com/Sandeshkumar0/Graviton) — a JavaScript and Canvas arcade game, shared as a team-project fork.
- [FAR-AWAY](https://github.com/Sandeshkumar0/FAR-AWAY) — a team system-design proof of concept for a personalized learning and skills platform. The public repository currently contains design documents.

I'm targeting full-stack developer roles. The repositories above show the code, current limitations, and next steps behind the projects.
