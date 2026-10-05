# Starter projects with automatic checks

**Two ways to test students' work automatically.** The stronger one needs no starter project: add **Automatic tests (hidden from students)** to the assignment in the trainer portal. FesCode then runs your tests on every GitHub hand-in, students cannot see or change them, and any public repository works. Use a starter project as well when you want students to begin from a set structure (folders, file names, sample data), so your hidden tests know where to find their code. The rest of this guide is about tests kept inside the student's repository, which students can see.

Each folder here is a starter project for one kind of course:

| Folder | For | Checks run with |
| --- | --- | --- |
| python-pytest | Python, software and data engineering | pytest |
| data-analytics-python | Data analytics with pandas | pytest |
| javascript-node | JavaScript and Node.js | npm test (Node's built-in test runner, no packages to install) |

Each one has example work in `src`, the checks in `tests` (or `test`), and the file that makes GitHub run them on every push: `.github/workflows/tests.yml`. Replace the example with your own assignment: write the function names and descriptions students must fill in, and the tests their work must pass.

## Setting one up for an assignment (once)

1. On GitHub, create a new public repository under the FesCode account, for example `fescode/da-week3-sales`.
2. Copy the contents of one starter folder into it, including the hidden `.github` folder. Write your assignment into `src` and your checks into the tests folder.
3. Check it on your own computer: the tests should FAIL on the starter code and PASS on your own model answer. Do not commit the model answer.
4. Push. In the repository's Settings, tick **Template repository**.
5. In the trainer portal, create the assignment with **Students hand in: GitHub repository**, and put the template's link in the brief.

## What students do

They open the template link, press **Use this template**, and create their own public repository from it. They work, push, and hand in the link from their portal. GitHub runs the checks on every push.

## What you see

Beside each hand-in on the marking page: passed, failed (with the names of the failing checks and a link to the details on GitHub), still running, or no automatic tests. The result is for the exact commit handed in, so later pushes do not change what you are marking.

## Good to know

- Checks help you mark faster. They do not mark for you: a pass means the code runs and meets the checks you wrote, not that it is good work. Use the rubric for the rest.
- Students can see the tests, so test behaviour, not one exact answer. Use several cases, including edge cases (empty input, ties, wrong values).
- GitHub runs these for free on public repositories.
- If a student edits the tests to make them pass, it shows in their commit history (the "Compare with earlier version" link on the marking page helps).
