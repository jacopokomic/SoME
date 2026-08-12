# Neural network self portrait

*by Jacopo Komic — a submission for [3Blue1Brown's Summer of Math Exposition](https://some.3b1b.co/)*

![The network learning, drawn by the notebook itself](preview.gif)

This is a Jupyter notebook that paints its own portrait: **every cell you run draws an animation of what just happened**. From the first shuffle of raw credit data to a neural network built from scratch in pure NumPy — no PyTorch, no TensorFlow, no scikit-learn — the notebook illustrates itself, trains live in front of you, and ends by answering your questions about credit risk through interactive sliders.

## Run it

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jacopokomic/SoME/main?urlpath=tree/neural-network-self-portrait.ipynb)

Click the badge (the first build can take a minute or two), then run the cells top to bottom with **Shift+Enter**. Training takes about half a minute — watch the bar. No installation, no account, nothing to set up.

### Or locally

```
git clone https://github.com/jacopokomic/SoME.git
cd SoME
pip install "numpy>=2" pandas notebook ipython ipywidgets
jupyter notebook neural-network-self-portrait.ipynb
```

For the full visual experience locally, copy `custom.css` to `~/.jupyter/custom/custom.css` (Binder does this automatically).

## What's inside

- `neural-network-self-portrait.ipynb` — the notebook: data preparation, a from-scratch feedforward network (He initialization, ReLU, dropout, class weighting, backpropagation), ROC AUC evaluation, and an interactive prediction widget.
- `animations.py` — the machinery that pairs each cell with its pre-rendered animation and powers the live training bar and sliders.
- `media/` — the 21 animations, rendered with [Manim](https://www.manim.community/).
- `data/` — the [*Give Me Some Credit*](https://www.kaggle.com/c/GiveMeSomeCredit) dataset (Kaggle): 150,000 anonymized, real credit histories.
