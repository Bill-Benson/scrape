import requests
from bs4 import BeautifulSoup
import argparse


def sort_news_by_score(news):
    sorted_news = sorted(news, key=lambda k: k["Score"], reverse=True)
    for pri_news in sorted_news:
        print(pri_news)


def pages(page):
    result = requests.get("https://news.ycombinator.com/?p=" + page)
    soup = BeautifulSoup(result.text, "html.parser")
    links = soup.select(".titleline")
    scores = soup.select(".subtext")
    return links, scores


def create_custom_news(n_links, subtext):
    news = []
    for idx, item in enumerate(n_links):
        title = item.getText()
        href = item.select_one("a")["href"]
        votes = subtext[idx].select_one('.score')
        if votes is not None:
            points = int(votes.getText().replace(' points', ''))
            if points > 99:
                news.append({"Title": title, "Link": href, "Score": points})
    return news


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("page", nargs="?", default="1", type=str, help="Page number to scrape")
    return parser.parse_args()


def main():
    args = get_arguments()
    link, score = pages(args.page)
    hacker_news_dict = create_custom_news(link, score)
    sort_news_by_score(hacker_news_dict)


if __name__ == "__main__":
    main()
