# Imposter & Truth-Teller Logic Solver

## Overview

This project implements a **logic-based reasoning engine** that determines the truthfulness of individuals in a group based on their statements. It is inspired by classical logic puzzles such as *Knights and Knaves* and modern scenarios like imposter detection or distributed system fault identification.

The solver combines **graph-theoretic modeling** for pairwise relationships and **Boolean logic** for complex statements, providing a flexible, accurate, and extendable framework.

---

## Inspiration

While exploring logic puzzles and online games involving liars and truth-tellers, I noticed two major challenges:

1. Many online platforms present puzzles with inconsistent or ad-hoc rules, where statements could be right or wrong independent of the speaker’s type.
2. There was no simple, interactive tool that could handle **multiple statement types** (pairwise, OR, AND, EXACTLY ONE) and provide consistent, logically sound outcomes.

This motivated the development of a formal, **graph + Boolean logic-based solver** that can handle any number of participants and statements while maintaining academic rigor.

---

## Features

* **Interactive menu**: Add any number of people and statements dynamically.
* **Statement types supported**:

  * Pairwise Truth: “A says B is truthful”
  * Pairwise Lie: “A says B lies”
  * OR statement: “At least one of A, B, C lies”
  * AND statement: “All listed people lie”
  * EXACTLY ONE statement: “Exactly one of the listed people lies”
* **Formal logic evaluation**: All statements are evaluated conditionally based on speaker truth.
* **Solver engine**: Uses combinatorial Boolean assignments and graph-based pruning for efficiency.
* **Consistent and reproducible results**: Provides all valid truth assignments.

---

## Graph-Theoretic Modeling

Pairwise statements are represented using a **graph abstraction**:

* **Nodes**: Individuals
* **Edges**: Logical constraints (SAME = same truth value, DIFFERENT = opposite truth value)

Graph-based checks allow **fast pruning** of inconsistent assignments.
For example, if “A says B is truthful” and “B says C lies,” the graph can help propagate constraints efficiently before evaluating all possible Boolean assignments.

Complex statements (OR, AND, EXACTLY ONE) are handled via **Boolean evaluation**, ensuring correct outcomes in multi-statement scenarios.

---

## Development Process

1. **Requirement Analysis**: Studied classic logic puzzles, identified key statement types, and noted limitations of existing online solvers.
2. **Graph & Boolean Design**: Modeled pairwise relationships with graphs and complex statements with Boolean evaluation.
3. **Iterative Implementation**:

   * Built an interactive menu to enter people and statements.
   * Developed classes to represent **pairwise** and **logic statements**.
   * Designed a solver using **combinatorial assignment** with graph-based pruning.
4. **Testing & Validation**:

   * Tested on standard puzzles (Ulric-Xenia-Tina, Olivia-Iris-Alice-Yates).
   * Ensured only logically consistent solutions are returned.
5. **Documentation**: Explained graph theory usage, logic propagation, and solver reasoning.

---

## Usage

Run the program:

```bash
python solver.py
```

* Enter the number of people and their names.
* Select statement types from the interactive menu.
* Input details for each statement.
* The program outputs all possible truth/lie assignments consistent with the statements.

Example:

```
Number of people: 3
Name 1: Ulric
Name 2: Xenia
Name 3: Tina

Number of statements: 2
Statement 1:
Speaker: Ulric
Type: 1
Target: Xenia

Statement 2:
Speaker: Ulric
Type: 3
How many people involved? 3
Person 1: Tina
Person 2: Ulric
Person 3: Xenia

Solution 1:
Ulric: Truth
Xenia: Truth
Tina: Liar
```

---

## Applications

* Academic exploration of **logic puzzles**
* Modeling **truth/lie detection** in social or online games
* Fault detection in **distributed systems**
* Foundation for **formal logic solvers and SAT-based systems**

---

## Future Work

* Natural language parsing for direct statement input
* Graph visualization of truth propagation
* Integration with SAT solvers for larger datasets
* Web-based interface for interactive puzzle solving

---

## Conclusion

This project combines **graph theory, Boolean logic, and combinatorial reasoning** to provide a flexible, robust solver for truth-teller/liar puzzles. It demonstrates a formal approach to a problem often handled inconsistently online, providing both educational value and a foundation for future research in logic-based systems.
