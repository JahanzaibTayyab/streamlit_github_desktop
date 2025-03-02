import os
import sys

from streamlit.web import cli


def app():
    sys.argv = ["streamlit", "run", "src/streamlit_github_desktop/main.py"]
    cli.main()


def app2():
    sys.argv = ["streamlit", "run", "src/streamlit_github_desktop/main.py"]
    cli.main()
