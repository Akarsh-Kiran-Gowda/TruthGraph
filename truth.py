import itertools

# ---------------------------------------
# STATEMENT CLASSES
# ---------------------------------------

class Statement:
    def __init__(self, speaker):
        self.speaker = speaker

    def is_satisfied(self, assign):
        raise NotImplementedError


class PairwiseStatement(Statement):
    # "X says Y is truthful"  OR  "X says Y lies"
    def __init__(self, speaker, target, says_truthful=True):
        super().__init__(speaker)
        self.target = target
        self.says_truthful = says_truthful

    def is_satisfied(self, assign):
        s = assign[self.speaker]
        t = assign[self.target]

        # what the statement CLAIMS
        if self.says_truthful:
            statement_truth = t
        else:
            statement_truth = not t

        # speaker truthfulness rule
        return s == statement_truth


class LogicStatement(Statement):
    # OR, AND, EXACTLY_ONE
    def __init__(self, speaker, kind, people):
        super().__init__(speaker)
        self.kind = kind
        self.people = people

    def is_satisfied(self, assign):
        s = assign[self.speaker]

        if self.kind == "OR":
            statement_truth = any(not assign[p] for p in self.people)
        elif self.kind == "AND":
            statement_truth = all(not assign[p] for p in self.people)
        elif self.kind == "EXACTLY_ONE":
            statement_truth = sum(not assign[p] for p in self.people) == 1
        else:
            raise ValueError("Unknown logic type")

        return s == statement_truth


# ---------------------------------------
# SOLVER
# ---------------------------------------

def solve(people, statements):
    solutions = []

    for values in itertools.product([True, False], repeat=len(people)):
        assign = dict(zip(people, values))

        valid = True
        for st in statements:
            if not st.is_satisfied(assign):
                valid = False
                break

        if valid:
            solutions.append(assign)

    return solutions


# ---------------------------------------
# INTERACTIVE MENU
# ---------------------------------------

def main():
    print("\n=== General Imposter / Truth-Teller Solver ===\n")

    n = int(input("Number of people: "))
    people = [input(f"Name {i+1}: ") for i in range(n)]

    print("\nStatement Types:")
    print("1 -> X says Y is truthful")
    print("2 -> X says Y lies")
    print("3 -> OR statement (At least one lies)")
    print("4 -> AND statement (All lie)")
    print("5 -> EXACTLY ONE lies\n")

    m = int(input("Number of statements: "))
    statements = []

    for i in range(m):
        print(f"\nStatement {i+1}")
        speaker = input("Speaker: ")
        stype = int(input("Type (1-5): "))

        if stype in (1, 2):
            target = input("Target: ")
            statements.append(
                PairwiseStatement(
                    speaker,
                    target,
                    says_truthful=(stype == 1)
                )
            )

        else:
            k = int(input("How many people involved? "))
            involved = [input(f"Person {j+1}: ") for j in range(k)]

            kind = {
                3: "OR",
                4: "AND",
                5: "EXACTLY_ONE"
            }[stype]

            statements.append(
                LogicStatement(speaker, kind, involved)
            )

    solutions = solve(people, statements)

    print("\n=== RESULTS ===")
    if not solutions:
        print("❌ No valid solution.")
    else:
        for i, sol in enumerate(solutions, 1):
            print(f"\nSolution {i}:")
            for p in people:
                print(f"  {p}: {'Truth' if sol[p] else 'Liar'}")


if __name__ == "__main__":
    main()
