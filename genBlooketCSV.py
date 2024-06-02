import datetime

allowDuplicateQuestions=False
blooketTemplate="""Blooket Import Template,,,,,,,,
Question #,Question Text,Answer 1,Answer 2,Answer 3 (Optional),Answer 4 (Optional),Time Limit (sec) (Max: 300 seconds),Correct Answer(s) (only include Answer #),Question Image
"""

blooket = blooketTemplate
questionsSeen=set()
questions=open("questionsBlooket.txt","r",encoding="UTF-8").read().splitlines()
questionNo = 1
for question in questions:
    if question=="":
        continue
    questionText=question.split(" (")[0]
    questionText = questionText.replace('"','""')
    # print(question)
    questionAnswers=question.split(" (")[1].split(")")[0].split(", ")
    questionAnswers=[ans.replace('"', '""') for ans in questionAnswers]
    questionAnswers=[((f"\"{questionAnswers[i]}\"") if (i < len(questionAnswers)) else "") for i in range(4)]
    questionCorrectAnswer=question.split(")")[1].split(": ")[1]
    questionCorrectAnswer=questionCorrectAnswer.replace('"', '""')
    questionCorrectAnswer=f"\"{questionCorrectAnswer}\""
    questionCorrectAnswerIndex  = 0
    questionCorrectAnswerIndex = [ans.lower() for ans in questionAnswers].index(questionCorrectAnswer.lower()) + 1
    qAFormatted=",".join(questionAnswers)
    timeLimit = 5
    questionIMGURL = ""
    questionIMGURL = questionIMGURL.replace('"', '""')
    myQuestionText = f"{questionNo},\"{questionText}\",{qAFormatted},{timeLimit},{questionCorrectAnswerIndex},\"{questionIMGURL}\"\n"
    if (((not allowDuplicateQuestions) and (questionText.lower() in questionsSeen))):
        continue
    questionsSeen.add(questionText.lower())
    blooket += myQuestionText
    print(f"Processed question {questionNo}.")
    questionNo += 1

fileName = datetime.datetime.now().isoformat().replace(":",".")
fileName = f"germanBlooket{fileName}.csv"
with open(fileName,"w",encoding="UTF-8") as f:
    f.write(blooket)