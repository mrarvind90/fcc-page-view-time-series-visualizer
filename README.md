[![freeCodeCamp Social Banner](https://s3.amazonaws.com/freecodecamp/wide-social-banner.png)](https://www.freecodecamp.org/)

<p style="text-align: center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python 3"/></a>
  <a href="https://numpy.org"><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy"/></a>
</p>

# Page View Time Series Visualizer

<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg" /></a>
<a href="https://github.com/psf/black"><img alt="Code Style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>

A Python program to create a time series visualizer of the page views on freeCodeCamp forum.

## Technologies Used

- pandas
- matplotlib
- seaborn

## Features

- Generate a line plot of page views on freeCodeCamp forum from 5/2016 to 12/2019
- Generate a bar plot of average page views on freeCodeCamp forum grouped by year-month 2016 to 2019
- Generate a year-wise and month-wise page view box plot

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10 or higher installed on your system. You can download Python
  from [python.org](https://www.python.org/downloads/).
- Poetry 1.6.1 installed on your system. You can install Poetry
  from [python-poetry.org](https://python-poetry.org/docs/#installation)

## Installation and Setup

Follow these steps to install and set up Poetry for this project:

1. **Install Poetry**:
   Poetry is a Python package manager that simplifies dependency management and virtual environments. You can install
   Poetry by following their guide [here](https://python-poetry.org/docs/#installing-with-the-official-installer).
2. Clone the repository
   ```shell
   git clone git@github.com:mrarvind90/fcc-page-view-time-series-visualizer.git
   ```
3. Change into the Project Directory
   ```shell
   cd fcc-page-view-time-series-visualizer
   ```
4. Install Dependencies:
   ```shell
   poetry install
   ```
5. Run the Project:
   ```shell
   poetry run python3 main.py 
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Code Style

We follow the black code style for this project. You can format your code using:

```shell
black .
```