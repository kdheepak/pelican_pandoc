from bs4 import BeautifulSoup


def process_content(content):

    soup = BeautifulSoup(content, 'html.parser')
    section = soup.find(attrs={'class': 'footnotes'})
    tag = BeautifulSoup('<h1 id=footnotes>Notes</h1>')
    if section:
        section.insert(0, tag)

    content = '\n'.join([unicode(i) for i in soup.contents])
    content = unicode(soup)
    return content
