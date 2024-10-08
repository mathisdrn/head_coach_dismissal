## Analysis of the effect of head coach change in football teams performance

This repository hosts the code, text and data of a research study on the relation between head coach and change of performance in football teams. 

To view the content of this research study, you can either:
- Visit the [hosted version](https://mathisdrn.github.io/head_coach_dismissal/) of this paper
- Download the [PDF version](https://raw.githubusercontent.com/mathisdrn/head_coach_dismissal/master/exports/head_coach_dismissal.pdf) of this paper
- See the presentation of this paper [here](https://docs.google.com/presentation/d/e/2PACX-1vRDbll6G-B2zQX_NrwABFr2VdhHO8NlmM-pfXadGm8QmPfjMPE5643PZw4hWosE9my_a2CN9pr5Ur10/pub?start=false&loop=false&delayms=10000000)

### Usage

To run the code in this repository, you will need to create a conda environment with the dependencies specified in the `requirements.yml` file. You can do so by running the following command in your terminal:

```bash
conda env create -f requirements.yml
```

Then, you can activate the environment and run the code in the Jupyter notebooks.

You can build the paper by installing [Typst](https://github.com/typst/typst) and running the following command in your terminal:

```bash
myst build Paper.md --pdf
```

You can also serve a static webpage of the paper by running the following command in your terminal:

```bash
myst start
```