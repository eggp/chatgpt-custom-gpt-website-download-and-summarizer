import os
from bs4 import BeautifulSoup
import re
from transformers import pipeline

def process_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # HTML feldolgozása BeautifulSoup segítségével
    soup = BeautifulSoup(html_content, 'html.parser')

    # Csak a fő tartalom kivonása
    main_content = soup.find('main')
    if not main_content:
        main_content = soup.find('article')
    if not main_content:
        main_content = soup.body  # Ha nincs 'main' vagy 'article', az egész 'body'-t használjuk

    text = main_content.get_text() if main_content else soup.get_text()

    # Szöveg tisztítása
    cleaned_text = re.sub('\s+', ' ', text).strip()

    return cleaned_text

def summarize_text(text, summarizer):
    # Szöveg felosztása kisebb részekre, ha szükséges
    chunk_size = 1000  # a modell bemeneti korlátja miatt
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Kivonatok készítése
    summaries = []
    for chunk in chunks:
        max_length = min(142, len(chunk) // 2)  # A max_length csökkentése a bemeneti hosszhoz igazítva
        summary = summarizer(chunk, max_length=max_length)[0]['summary_text']
        summaries.append(summary)

    # Kivonatok összefűzése
    final_summary = " ".join(summaries)

    return final_summary

def process_directory(directory_path, summarizer):
    summaries = {}

    # Könyvtár bejárása
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")

                # HTML fájl feldolgozása
                text = process_html_file(file_path)

                # Szöveg összefoglalása
                summary = summarize_text(text, summarizer)

                # Eredmények tárolása
                summaries[file_path] = summary

    return summaries

def main():
    directory_path = 'html_files'  # A konténerben elérhető könyvtár útvonala
    summarizer = pipeline("summarization")

    summaries = process_directory(directory_path, summarizer)

    with open('summaries/summaries.txt', 'w', encoding='utf-8') as output_file:
        for file_path, summary in summaries.items():
            output_file.write(f"Summary for {file_path}:\n{summary}\n\n")

if __name__ == "__main__":
    main()
