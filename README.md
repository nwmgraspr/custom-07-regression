# datafun-07-regression

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://nwmgraspr.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: linear regression and predictive analytics.

## Project Goal

This project introduces **linear regression**, the process of
fitting a model to data and using it to make predictions.

Think about two variables that might be related:

- Does study time predict exam scores?
- Does temperature predict energy usage?
- Does advertising spend predict revenue?

Your goal: run the example, read the code,
and apply the same approach to a dataset and question of your own choosing.

For data suggestions, please see [data/raw/README.md](data/raw/README.md).

## Working Files

You'll work with just these areas:

- **data/raw** - raw data for exploration
- **docs/** - project narrative and documentation
- **src/** - supporting Python package modules
- **notebooks/** - interactive analysis
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions (pro-analytics-02)

Follow the
[step-by-step workflow guide](https://nwmgraspr.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
running on your machine, and running the example will print out:

```shell
========================
Executed successfully!
========================
```

A new file `project.log` will appear in the root project folder.

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/nwmgraspr/custom-07-regression

cd datafun-07-regression
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

# run the penguin example: is there a linear relationship?
uv run python -m datafun.app_penguins_case

# run the co2 example: is there a linear relationship?
# the line fits poorly; why?  what would you change?
uv run python -m datafun.app_co2_case

# do chores
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT not to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Example Output

```shell
2026-06-25 00:05:16 | INFO | P07 | Correlation between total_bill and tip: 0.6757
2026-06-25 00:05:16 | INFO | P07 | Creating modeling view
2026-06-25 00:05:16 | INFO | P07 | Original rows: 244
2026-06-25 00:05:16 | INFO | P07 | Model rows: 244
2026-06-25 00:05:16 | INFO | P07 | Rows dropped: 0
2026-06-25 00:05:16 | DEBUG | P07 | X shape: (244, 1)
2026-06-25 00:05:16 | DEBUG | P07 | y shape: (244,)
2026-06-25 00:05:16 | INFO | P07 | Fitting linear regression model
2026-06-25 00:05:16 | INFO | P07 | Regression Equation:
2026-06-25 00:05:16 | INFO | P07 | tip = 0.105025 * total_bill + 0.920270
2026-06-25 00:05:16 | INFO | P07 | Predicted tip for a bill of $50.00: $6.17
2026-06-25 00:05:16 | INFO | P07 | ====================
2026-06-25 00:05:16 | INFO | P07 | MODEL EVALUATION
2026-06-25 00:05:16 | INFO | P07 | ====================
2026-06-25 00:05:16 | INFO | P07 | R-squared: 0.4566
2026-06-25 00:05:16 | INFO | P07 | RMSE: 1.0179
2026-06-25 00:05:16 | INFO | P07 | Residual Min: -3.1982
2026-06-25 00:05:16 | INFO | P07 | Residual Max: 3.7434
2026-06-25 00:05:16 | INFO | P07 | Residual Mean: 0.0000
2026-06-25 00:05:17 | INFO | P07 | ====================
2026-06-25 00:05:17 | INFO | P07 | SUMMARY
2026-06-25 00:05:17 | INFO | P07 | ====================
2026-06-25 00:05:17 | INFO | P07 | Dataset: tips
2026-06-25 00:05:17 | INFO | P07 | Feature: total_bill
2026-06-25 00:05:17 | INFO | P07 | Target: tip
2026-06-25 00:05:17 | INFO | P07 | Original Rows: 244
2026-06-25 00:05:17 | INFO | P07 | Model Rows: 244
2026-06-25 00:05:17 | INFO | P07 | Regression Equation: tip = 0.105025 * total_bill + 0.920270
2026-06-25 00:05:17 | INFO | P07 | Interpret the R-squared, RMSE, and residual plots to determine whether a linear model is appropriate.
2026-06-25 00:05:33 | INFO | P07 | Regression workflow complete
2026-06-25 00:05:33 | INFO | P07 | ========================
2026-06-25 00:05:33 | INFO | P07 | Executed successfully!
2026-06-25 00:05:33 | INFO | P07 | ========================
```

## Findings and Visuals

Take screenshots of your charts and provide them here with a discussion.
In Markdown, display a figure by using:
an exclamation mark immediately followed by square brackets containing a useful caption
immediately followed by parentheses containing the relative path to your figure.
Note: When you start typing the path with a dot (.) for "here, in this directory",
the IDE may help complete the path.

In your custom project, discuss these examples, but

- your figures and narrative should reflect your work,
- this `README.md` should include your commands, process, and visuals, and
- `docs/index.md` should include your narrative.

Remove unnecessary instructional comments in your custom files.

Update these figures to present interesting results from your custom project:

## Penguins: Is there a linear relationship?

![Provide a Useful Caption](./docs/images/Figure_1.png)

![Provide a Useful Caption](./docs/images/Figure_2.png)

## World Data: Is there a linear relationship? How can you improve the analysis?

![Provide a Useful Caption](./docs/images/Figure_3.png)

![Provide a Useful Caption](./docs/images/Figure_4.png)

## Project Documentation

Additional instructions, terms, and project notes:

[docs/index.md](docs/index.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
