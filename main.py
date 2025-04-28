import requests
import json

def main():
    jsondata = dict(json.loads(requests.get(input("Insert URL: ")).content)["message"])

    # Get Author
    author = dict(jsondata["author"][0])
    print(f"Author: {author["given"]} {author["family"]}")

    # Get Article Title
    title = jsondata["title"][0]
    print(f"Article Title: {title}")

    # Get Volume
    volume = jsondata["volume"]
    print(f"Volume: {volume}")

    # Get Issue
    issue = jsondata["issue"]
    print(f"Issue: {issue}")

    # Get Publication Date
    date = jsondata["published-online"]["date-parts"][0]
    print(f"Published: {date[2]}/{date[1]}/{date[0]}")

    # Get Short Title
    short = jsondata["short-title"]
    print(f"Short Title: {short}")

    # Get DOI
    doi = jsondata["DOI"]
    print(f"DOI: {doi}")

    # Uncomment to prettify output
    # print(json.dumps(jsondata, indent=4))

if __name__ == "__main__":
    main()
