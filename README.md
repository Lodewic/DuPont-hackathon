DuPont-Hackathon
==============================

DuPont enzyme design hackathon 2019

# Data-Driven Enzyme Engineering Hackathon

Enzymes are natural molecular machines that can perform the amazing feat of enabling and accelerating chemical reactions without themselves being consumed in the process. All living organisms on Earth depend on enzymes to process nutrients, to grow and to reproduce. Thanks to the development of modern biotechnology, enzymes can also be produced in large quantities and employed to speed up all kinds of industrially important reactions, ranging from stain removal by detergents to production of food, feed, and biomaterials.

As our requirements for lower resource use get more demanding, we continuously need to improve our enzymes to make them more stable and effective. At DuPont Industrial Biosciences, we routinely screen thousands of enzymes to obtain models of the relationship between the sequence of amino acid residues that make up the enzyme, its 3D structure, and the observed performance.

In this hackathon, we will provide representative data for our challenge, describe the problem and discuss different approaches of how to employ techniques like deep learning to support enzyme optimization process. Join and help us design the enzymes of tomorrow! 

## Installation

None of the packages used in this repository are required for participating in the hackathon but if you want to follow the examples you can do by first installing pipenv

```
pip install pipenv
```

And then do

```
pipenv install
```

The install the nglview jupyter extension by

```
setup.sh
```

After that you should be able to open the notebook

```
jupyter notebook hackathon.ipynb
```

## Submissions

Submitting sequences for the virtual lab facility is done by

```
import requests

sequences = [('AQSVPWGISRVQAPAAHNRGLTGSGVKVAVLDTGISTHPDLNIRRGGASFVPGEPSTQDGNGHGTHVA'
              'GTIAALNNSIGVLGVAPSAELLYAVKVLGASGSSGGSSVSSIAQGLEWAGNNGMHVANLSLGSPSPSA'
              'TLEQAVNSATSRGVLVVAASGNSGAGSISYPARYANAMAVGATDQNNNRASFSQYGAGLDIVAPGVNV'
              'QSTYPGSTAASLNGTSMATPHVAGAAALVKQKNPSWSNVQIRNHLKNTATSLGGSSTTNNLYGSGLVA'
              'AEAATR'),
             ('AQSVPWGASRVQAPAAHNRGLTGSGVAVAVLDTGISTHPDLNIRRGGASFVPGEPSTQDGNGHGTHVA'
              'GTIAALNNSIGVLGVAPSAELLYAVKVLGASGSSGGSSVSSIAQGLEWAGNNGMHVANLSLGSPSPSA'
              'TLEQAVNSATSRGVLVVAASGNSGAGSISYPARYANAMAVGATDQNNNRASFSQYGAGLDIVAPGVNV'
              'QSTYPGSTYASLNGTSMATPHVAGAAALVKQKNPSWSNVQIRNHLKNTATSLGGSSTTNNLYGSGLVN'
              'AEAATR')]

payload = {'team': 'footeam', 'challenge': 0, 'sequences': sequences}

r = requests.post('http://find-the.best/enzyme', json=payload)
```


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
