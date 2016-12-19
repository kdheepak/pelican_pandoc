from bs4 import BeautifulSoup
import bs4


def process_content(content):

    soup = BeautifulSoup(content, 'html.parser')
    footnotes = soup.find(attrs={'class': 'footnotes'})
    if footnotes:
        for tag in footnotes.findAll('li'):
            p = tag.find('p')
            if isinstance(p.contents[0], bs4.element.Tag):
                tag.name = 'aside'
                p.contents = p.contents[1:-1]
                p.contents[0].replaceWith(p.contents[0].lstrip().lstrip(':').lstrip())

                a = soup.find(attrs={'href': '#{}'.format(tag.attrs['id'])})
                span = soup.new_tag('span', id=tag.attrs['id'])

                a.parent.insert_after(tag)
                a.replace_with(span)

        if not footnotes.findAll('li'):
            footnotes.extract()

    content = '\n'.join([unicode(i) for i in soup.contents])
    content = unicode(soup)
    return content


def wrap(to_wrap, wrap_in):
    contents = to_wrap.replace_with(wrap_in)
    wrap_in.append(contents)

