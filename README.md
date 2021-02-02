# Starship

I recommend using linux or macOS for this project as future packages (like *fenics*) may be easier to use with those.

1. Install last version of Miniconda (available [here](https://conda.io/miniconda.html)).

     If you already have one installed, you can update it by typing in the shell :
    ```shell 
    conda update conda
    ```
2. Then make a new environment for this project :
    ```shell
    conda create -n SS python=3.9
    ```
3. Activate new environment :

    Using macOS or linux : ```conda activate SS```

    Using Windows : ```activate SS```

4. Install required packages :
    ```shell
    conda install jupyter matplotlib numpy scipy bokeh
    ```
5. Launch Jupyter server :
    ```shell
    jupyter notebook
    ```
Side note : *Bokeh* works better with *jupyter notebook* than *jupyter lab*.
