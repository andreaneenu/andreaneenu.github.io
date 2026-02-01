---
layout: page
title: Crowd Evacuation Simulation
description: Agent-based modeling of crowd panic situations using numerical schemes (Euler, RK4).
img: assets/img/crowd_pic.png
importance: 1
category: Research
tags: [Crowd Dynamics, Agent-Based Modeling, Numerical Schemes, Social Force Model, Physics, Python, Computational Physics]
related_publications: false
---

## Project Overview

In this project, we designed simulation-based strategies to reduce fatalities in high-density panic situations. By using **agent-based models** and **numerical schemes** (Euler and Runge-Kutta 4th Order), we implemented an improved Social Force Model (SFM) to see how individuals interact within a crowd during emergency evacuations.

The increasing number of refugees due to natural and man-made disasters presents significant challenges, particularly in ensuring the safe and efficient distribution of food in refugee camps. Panic-driven motion during food distribution often leads to overcrowding, collisions, and fatalities.
In this study, we model the food distribution process using a crowd dynamics framework to analyze how movement patterns contribute to injuries and deaths. Our simulations show that as food distribution begins, refugees rush toward the food distribution point, leading to high-density congestion and dangerous interactions. We explore strategies to mitigate these risks by introducing fixed obstacles near the food distribution point. The results demonstrate that a single obstacle can reduce fatalities by approximately 15%, while an optimized two-obstacle configuration achieves up to a 70% reduction. Additionally, we examine the impact of varying obstacle parameters—such as size, placement, and gap distance—and discuss their effects on crowd flow. The findings suggest that strategic obstacle placement can significantly improve safety, offering a practical and low-cost intervention for refugee camps. Future work could explore additional measures, such as increasing the number of food distribution points, to further enhance efficiency while addressing logistical constraints.

### Key Achievements
- **70% Fatality Reduction**: Successfully demonstrated strategies that significantly decreased death rates in simulated high-density environments.
- **Multidisciplinary Approach**: Combined principles from statistical physics, numerical analysis, sociophysics and behavior modeling.
- **High-Performance Computation**: Implemented efficient simulation loops to handle large agent counts.

## Methodology

The simulation treats each person as an 'agent' with specific behavioral rules, such as:
1. **Desired Velocity**: The direction and speed an agent wants to move towards the exit.
2. **Social Force**: Repulsion from other agents to maintain personal space.
3. **Obstacle Force**: Interaction with walls and stationary objects.

We solved the equations of motion using **RK4** to ensure numerical stability and accuracy over time-steps.

### Visualization

The simulation results were visualized to analyze "clogging" effects near exits and the effectiveness of placed obstacles in diverting crowd flow.

---

You can find the full source code and more technical details on [GitHub](https://github.com/andreaneenu/crowd_evacuation).

---

### Research Paper

This project is based on our research work that investigates **Crowd dynamics and obstacle-based safety strategies** for food distribution in refugee camps.

You can read the paper here:  
👉 [**A simple model for panic driven motion in a refugee camp∗ (PDF)**](https://github.com/YashJayswal24/crowd_evacuation/blob/main/panic_driven.pdf)

---