# dentate_new

This model, originally written in NEURON and hoc by Soltesz lab members, has been adapted by M. Bezaire to be a hybrid NEURON+Python model for use in a summer course on computational modeling. The original code is available on [ModelDB](https://senselab.med.yale.edu/ModelDB/ShowModel?model=124513#tabs-1).

## Installation and Requirements

This code requires [NEURON](https://www.neuron.yale.edu/neuron/). To run via Python (optional), this code requires Python 3 as well as updated environmental variables so that NEURON can be accessed from within Python. Run `nrnpyenv` for hints.

Download the code as a zip file or, from the terminal with git installed, with the command:
```
git clone https://github.com/risecourse/dentate_new.git
```

Then, in the directory of the model code, compile the *.mod mechanisms by running the following command in a terminal:
* On Windows, run `mknrndll`
* On Mac and Linux, run `nrnivmodl`

## Running the Code
The code can be run from within Spyder or via Anaconda Prompt if you want to run in parallel.

In Spyder, simply run the `main.py` file.  It will run slowly, in serial, and plot at the end.

If using Anaconda Prompt, first find out how many cores your computer has, then launch an Anaconda Prompt from the Anaconda application folder. Change directory (cd) to the CA1_Cutsuridis folder and then enter at the command line (replacing 4 with however many cores your computer has):
`mpiexec -n 4 python main.py`

