
QuestionBank = dict()
# Question Number: Question Dict
# Question Dict["Question"]: "?"
# Question Dict["Option A"]: "A"
# Question Dict["Option B"]: "B"
# Question Dict["Option C"]: "C"
# Question Dict["Option D"]: "D"
# Question Dict["Answer"]: "A"

import requests
from bs4 import BeautifulSoup
url = "http://jule-iii.com/cgi-bin/uscg/uscg.pl?Book=1&mode=All"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
for AnswerChunk in soup.find_all("ul"):
    Answers = AnswerChunk.text
    CorrectAnswer = AnswerChunk.find("b").text
print(soup.text)