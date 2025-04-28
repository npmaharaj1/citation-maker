import requests
import json

def crossref(jsondata):
    # Get Author
    author = dict(jsondata["author"][0])
    print(f"Author: {author["given"]} {author["family"]}")

    # Get Article Title
    title = jsondata["title"][0]
    print(f"Article Title: {title}")

    # Journal Title
    jtitle = jsondata["container-title"][0]
    print(f"Journal Title: {jtitle}")

    # Get Volume
    volume = jsondata["volume"]
    print(f"Volume: {volume}")

    # Get Issue
    issue = jsondata["issue"]
    print(f"Issue: {issue}")

    # Get Publication Date
    try:
        date = jsondata["published-online"]["date-parts"][0]
    except:
        date = jsondata["published-print"]["date-parts"][0]
    if len(date) == 3:
        print(f"Published: {date[2]}/{date[1]}/{date[0]}")
    elif len(date) == 2:
        print(f"Published: {date[1]}/{date[0]}")
    else:
        print(f"Published: {date[0]}")

    # Get Short Title
    short = jsondata["short-title"]
    print(f"Short Title: {short}")

    # Get DOI
    doi = jsondata["DOI"]
    print(f"DOI: {doi}")



def main():
    userInput = input("Insert URL or DOI: ")

    if userInput[0:6] == "https://":
        print("Defaulting to Crossref...")
        jsondata = dict(json.loads(requests.get(input(userInput)).content)["message"])
        crossref(jsondata)
    else:
        print("Interpreting DOI...")
        jsondata = dict(json.loads(requests.get(f"https://api.crossref.org/works/{userInput}").content)["message"])
        crossref(jsondata)


    # Uncomment to prettify output
    # print(json.dumps(jsondata, indent=4))

if __name__ == "__main__":
    main()
