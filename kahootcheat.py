import urllib.request as ur
import json

gameid = input(dd50f853-6ea6-4688-891b-c34a11dc98af)
url = "https://play.kahoot.it/rest/kahoots/" + dd50f853-6ea6-4688-891b-c34a11dc98af
q = json.loads(ur.urlopen(url).read())["questions"]
colours_list = ["red", "blue", "yellow", "green"]

for index, slide in enumerate(q):
    if slide.get("type") == "quiz":
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"] == True:
                print("Question number: {}\n{}\n{}\n".format(
                    index + 1, slide["choices"][i].get("answer"), colours_list[i]))
