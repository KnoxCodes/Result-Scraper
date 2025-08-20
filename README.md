# Result Scraper
## 🗂️ Description

The Result Scraper is a web scraping tool designed to extract CGPA data from a specific website. It provides a user-friendly interface to input admission year, degree, branch, start and end roll numbers, and the number of parallel threads. The tool then scrapes the CGPA data, generates a CSV file, and displays summary statistics, a histogram of CGPA distribution, and a table of top performers. This project is ideal for users who need to analyze CGPA data for a large number of students.

The Result Scraper uses a combination of technologies such as Streamlit, Pandas, Matplotlib, Seaborn, and Selenium to achieve its functionality. The tool is designed to be easy to use and provides a simple way to visualize and analyze CGPA data.

## ✨ Key Features

* **Web Scraping**: Extracts CGPA data from a specific website using Selenium with Chrome and Chromedriver.
* **User Interface**: Provides a user-friendly interface to input admission year, degree, branch, start and end roll numbers, and the number of parallel threads.
* **Data Analysis**: Generates summary statistics, a histogram of CGPA distribution, and a table of top performers.
* **Data Export**: Exports results to a CSV file.

## 🗂️ Folder Structure

```mermaid
graph TD;
    src-->app.py;
    src-->scraper.py;
    src-->setup.sh;
    src-->requirements.txt;
```

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-3498db?logo=streamlit&logoColor=white&style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white&style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?logo=matplotlib&logoColor=white&style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?logo=seaborn&logoColor=white&style=for-the-badge)
![Selenium](https://img.shields.io/badge/Selenium-43B3A1?logo=selenium&logoColor=white&style=for-the-badge)

## ⚙️ Setup Instructions

To run the project locally, follow these steps:

* Git clone the repository: `https://github.com/KnoxCodes/Result-Scraper.git`
* Navigate to the repository: `cd Result-Scraper`
* Install dependencies: `pip install -r requirements.txt`
* Run the setup script: `./setup.sh`
* Run the application: `streamlit run app.py`

## 🤖 GitHub Actions

The repository uses GitHub Actions to automate the setup and deployment process. The workflow is defined in the `.github/workflows/main.yml` file and includes the following steps:

* Checkout code
* Install dependencies
* Run setup script
* Run application

Note: The `.github/workflows/main.yml` file is not included in the provided file summaries, but it is assumed to exist in the repository.

## 📝 Usage

To use the Result Scraper, simply run the application and follow the prompts:

1. Input admission year, degree, branch, start and end roll numbers, and the number of parallel threads.
2. Click the "Scrape" button to extract CGPA data.
3. The tool will generate a CSV file and display summary statistics, a histogram of CGPA distribution, and a table of top performers.



<br><br>
<div align="center">
<img src="https://avatars.githubusercontent.com/u/217230820?v=4" width="120" />
<h3>Knox</h3>
<p>No information provided.</p>
</div>
<br>
<p align="right">
<img src="https://gitfull.vercel.app/appLogo.png" width="20"/>  <a href="https://gitfull.vercel.app">Made by GitFull</a>
</p>
    