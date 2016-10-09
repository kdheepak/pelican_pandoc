from bs4 import BeautifulSoup, Tag


def process_content(content):

    content = wrap_tag('aside', content)

    return content


def wrap_tag(tag, content):
    soup = BeautifulSoup(content, 'html.parser')
    aside_tags = soup.findAll(tag)
    for tag in aside_tags:
        aside = Tag(soup, name=tag, attrs=tag.attrs)
        div = Tag(soup, name='div', attrs={'id': 'div-{}'.format(tag.attrs['id'])})
        div.contents = tag.contents
        tag.replaceWith(aside)
        div.insert(0, tag)
    content = unicode(soup)
    return content
