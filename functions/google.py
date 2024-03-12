
from gpt4 import GPT
from gpt4 import find_code

def search_google(Query):
    if Query != "":
        res = GPT("open google and search: " + Query)
        print(res)
        python_code = find_code(res)
        try:
            exec(python_code)
            res = res[: res.index("python") - 3]
            return res
        except:
            return "Sorry! Unable to do this"
    else:
        return "Sorry! Not Able to Search that can you speak it again?"

search_google('Gadani Panth')