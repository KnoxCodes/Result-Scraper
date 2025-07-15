import os
os.environ['PATH'] += os.pathsep + '/usr/bin'


import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def get_cgpa(roll_no, year):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        
        driver.get(f"http://results.nith.ac.in/scheme{year}/studentresult/index.asp")

    
        input_field = driver.find_element(By.NAME, "RollNumber")
        input_field.send_keys(roll_no)
        input_field.send_keys(Keys.RETURN)

    
        time.sleep(0.5)

        
        cgpa_text = driver.find_element(
            By.XPATH, "(//p[@style='float:right;text-align: right; font-weight:bold;'])[last()-1]"
        ).text.strip()

        cgpa_value = cgpa_text.split('=')[-1].strip() 
        print(f"{roll_no}: CGPA = {cgpa_value}")
        return cgpa_value

    except Exception as e:
        print(f"{roll_no}: Error - {str(e)}")
        return None
    finally:
        driver.quit()


def generate_roll_numbers(year, degree, branch, start=1, end=120):
    roll_numbers = []
    for i in range(start, end + 1):
        roll_num = f"{i:03d}" 
        roll_id = f"{year}{degree}{branch}{roll_num}"
        roll_numbers.append(roll_id)
    return roll_numbers


def get_all_cgpas_parallel(rolls, year, max_workers=5):
    results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_roll = {executor.submit(get_cgpa, roll, year): roll for roll in rolls}
        for future in as_completed(future_to_roll):
            roll = future_to_roll[future]
            try:
                results[roll] = future.result()
            except Exception as e:
                results[roll] = f"Error: {e}"
    return results


def export_to_csv(results, filename='cgpa_results.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Roll Number", "CGPA"])
        for roll, cgpa in results.items():
            writer.writerow([roll, cgpa])
    print(f"\n✅ Results exported to {filename}")


def analyze_and_plot(csv_file='cgpa_results.csv'):
    df = pd.read_csv(csv_file)
    df = df.dropna()
    df['CGPA'] = pd.to_numeric(df['CGPA'], errors='coerce')
    df = df.dropna()

    print("\n--- 📊 Summary Statistics ---")
    print(df['CGPA'].describe())


    plt.figure(figsize=(10, 6))
    sns.histplot(df['CGPA'], bins=20, kde=True, color='skyblue')
    plt.title("CGPA Distribution")
    plt.xlabel("CGPA")
    plt.ylabel("Number of Students")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("cgpa_distribution.png")
    print("📈 Distribution graph saved as 'cgpa_distribution.png'")
    plt.show()
