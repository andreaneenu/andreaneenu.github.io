---
layout: page
title: Quantum Hydrodynamic Description of Plasma
description: Validated Wigner-Poisson formulations and implemented a high-performance N-body simulation (PIC approach).
img: assets/img/quantum_plasma.png
importance: 2
category: Research
tags: [Physics, Plasma Physics, Quantum Mechanics, PIC Simulation, Python, HPC, Computational Physics]
related_publications: false
---

## Abstract

A quantum hydrodynamic description of plasma is a theoretical framework that attempts to describe the behaviour of a plasma at a macroscopic level, taking into account both quantum mechanics and the principles of fluid dynamics. In this framework, the plasma is treated as a collection of charged particles, such as ions and electrons, that interact with each other through the electromagnetic force. 

The behaviour of the plasma is described by a set of hydrodynamic equations, which describe the motion of the particles, their interactions, and the electromagnetic fields that they generate. At the quantum level, the particles are treated as wave functions, and the hydrodynamic equations are modified to include quantum effects such as wave-particle duality and uncertainty principle. One of the key advantages of a quantum hydrodynamic description of plasma is that it allows for a more accurate and comprehensive understanding of plasma behaviour than classical models. This can be particularly important in fields such as astrophysical plasmas.

---

## B.Tech Thesis Paper

This project is a result of research work involving a hydrodynamic description of astrophysical plasma.

You can read the full report here:  
👉 [**Quantum Hydrodynamic Description of Plasma (PDF)**](https://github.com/andreaneenu/Quantum_plasma/blob/main/Quantum_Plasma_Thesis_Paper.pdf)

---

## Simulation: Particle-In-Cell (PIC) System

In plasma physics, the PIC method is a numerical approach that simulates a collection of charged particles that interact via external and self-induced electromagnetic fields. A spatial grid is used to describe the field while the particles move in continuous space. The field and the particle motion are solved concurrently.

This project implements a **self-consistent 1D electrostatic plasma simulation** under the following assumptions:

1. No variation in plasma and particle quantities (charge density, velocity, position, etc.) or in the electric field along the z-direction.  
2. The magnetic field is zero along the x-axis in which the particles move.  
3. Distances are restricted to the order of the **Debye length**, where charge separation occurs and charge density is non-zero.  
4. Simulation time is limited to the order of the **electron plasma frequency**, ensuring zero average current densities (no self-magnetic field).  
5. **Collisions are neglected.**

Under these conditions, **Maxwell’s equations reduce to Poisson’s equation**, which specifies the electric field distribution at any given time.

### PIC Algorithm for 1D Electrostatic Plasma Simulation

1. **Initialize** particle data (positions, velocities, perturbation distribution).
2. **Initialize** grid (number of cells, grid length, cell spacing).
3. **While** `t < t_max` do:
    - Compute particle contributions to the grid.
    - Calculate the electric field (stored in discretized grid array).
    - Update forces acting on particles.
    - Move particles to new positions.
    - Advance time: `t → t + t_step`.
4. **End loop**.
5. **Output** particle and grid data.
6. **Compute** and print simulation statistics.

---

### Key Technical Contributions
- **Validated Wigner-Poisson formulations** within the hydrodynamic framework.
- **Implemented high-performance N-body simulation** using the PIC approach.
- **Python Wrappers**: Developed Python wrappers for fortran subroutines, achieving a **10X visualization speedup** for real-time analysis.

---

## Source Code
The complete source code and technical implementation details are available on [GitHub](https://github.com/andreaneenu/Quantum_plasma).

## Acknowledgment
- Used **LCPFCT** routines developed by Boris, Jay P. and team at the Naval Research Lab Washington DC.
- Implemented Python wrappers with the help of the [Scivision](https://github.com/letapk/espic1d) project.
- Results cross-checked using the **ESPIC1D** code.

## References
- Birdsall, C. K., & Langdon, A. B. *Plasma Physics via Computer Simulation*, McGraw-Hill (1985).  
- Hockney, R. W., & Eastwood, J. W. *Computer Simulation Using Particles*, Taylor & Francis (1988).  
