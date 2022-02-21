import requests
from bs4 import BeautifulSoup


def request_github_trending(url):
    response = requests.get(url)
    return response


def extract(page):
    salom = BeautifulSoup(page.text, "html.parser")
    return salom.find_all("article")


def transform(html_repos):
    natija = []
    for row in html_repos:
        repository_name = ''.join(row.select_one("h1.h3.lh-condensed").text.split())

        number_stars = ' '.join(row.select_one("span.d-inline-block.float-sm-right").text.split())

        developer_name = row.select_one("img.avatar.mb-1.avatar-user")['alt']
        natija.append({'developer': developer_name, 'repository_name': repository_name, 'nbr_stars': number_stars})
    return natija


def format(repositories_data):
    natija = ["Developer, Repository Name, Number of Stars"]
    for repos in repositories_data:
        row = [repos['developer'], repos['repository_name'], repos['nbr_stars']]
        natija.append(', '.join(row))

    return "\n".join(natija)


def _main():
    url = "https://github.com/trending"
    page = request_github_trending(url)
    html_repos = extract(page)
    repositories_data = transform(html_repos)
    print(format(repositories_data))


_main()