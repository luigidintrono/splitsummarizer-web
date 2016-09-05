# Split Summarizer
A simple flask based web application that makes your readings thrice as short.
Uses Miso Belica's sumy package for Python.

# Set up Instructions.

We use virtual environemtns for working with split. To get Split running on your own local machine, you will need Python 2, pip, and virtualenv.

* Clone this repository to your own machine.
    `$ git clone https://github.com/SplitSummarizer/splitsummarizer-web ./split`
* Navigate to the newly cloned repository.
* Use `virtualenv` to create your virtual environment.
    `$ virtualenv spsum`
* Activate your virtual environment. (this should add `(spsum)` to your working prompt)
    `$ source ./spsum/bin/activate`
* Install all the requirements using pip.
    `$ pip install -r requirements.txt`
