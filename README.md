# Webinar: Software Engineering Tips For Data Scientists

This repository contains the contents created during the live demonstration during this [webinar](https://info.datascience.salon/leveraging-software-engineering-secrets-in-your-data-science-workflows).
The slides presented can be found [here](https://docs.google.com/presentation/d/1FlJZT4q6bbdt7JIntDg-O0oZ5Vh3fT_j5acduQqn_nI/edit?usp=sharing).

The webinar requires an installation of `conda`, which can be installed via Anaconda distribution or miniconda.
For more installation details, please check [Anaconda Nucleus](https://anaconda.cloud/installers).

## Installing `anaconda-project`

This example uses [`anaconda-project`](https://anaconda-project.readthedocs.io/en/latest/) for dependency specification and reproducibility.
You should install `anaconda-project` into either your base or another `conda` environment.

If using the `base` environment, at your command-line type:

```shell
conda install anaconda-project
```

Otherwise, first create another `conda` environment prior to the above command, for example:

```shell
conda create -n <my-environment> anaconda-project
conda activate <my-environment>
```

where `<my-environment>` can be any name you prefer.

## Running the project

There are four different run configurations stored to run the project.

### Dev environment

The following command will launch `jupyter-lab` with the `git` extension, all within its own local `conda` environment:

```shell
anaconda-project run dev
```

### Notebook

The following command will launch a simple `jupyter` notebook that the user can experiment with, without installing `jupyter-lab`:

```shell
anaconda-project run notebook
```

### Panel dashboard

The following command will launch a [`Panel`](https://panel.holoviz.org/) dashboard in a browser, served from a local webserver:

```shell
anaconda-project run dashboard
```

### Run automated tests

The following command will run the automated test(s) with [`pytest`](https://docs.pytest.org/):

```shell
anaconda-project run tests
```
