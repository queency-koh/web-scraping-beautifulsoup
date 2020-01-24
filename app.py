import requests
import pandas as pd
from bs4 import BeautifulSoup

base_url = "https://stackoverflow.com/questions"
question_list = []
for page in range(1, 6):
    response = requests.get(f"{base_url}?tab=newest & page={page}")

    soup = BeautifulSoup(response.text, "html.parser")

    questions = soup.select('.question-summary')
    for question in questions:
        title = question.select_one(".question-hyperlink").getText()
        votes = question.select_one(".vote-count-post").getText()
        question_list.append({"question": title, "votes": votes})

data = pd.DataFrame(question_list)
data.to_excel("stackover-flow-questions.xlsx")
