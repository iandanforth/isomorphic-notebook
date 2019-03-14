# isomorphic-notebook
A template notebook that runs in both local Jupyter and in Colab as an entry 
point to a repository.

## Usage

 - Initialize a new repository and copy in these files.
 - Update the variables `github_account` and `repository_name` in `main.ipynb`
 - Update the repository information and `requires` list in `setup.py`
 - Develop `main.ipynb` as an entry point into your repository. 

 Your users can now interact with your notebook in two ways:

  - Clone your repository locally, run `jupyter notebook` and open `main.ipynb`
  - Open `main.ipynb` from Google colab.

You may also want to add the following section to your `README.md` to encourage
your users to install the colab browser plugin so they can 
launch `main.ipynb` with one click.

### Install Browser Plugin

You can open a github hosted jupyter notebook in colab in one click!

[Firefox Addon](https://addons.mozilla.org/en-US/firefox/addon/open-in-colab/)

[Chrome extension](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo)
