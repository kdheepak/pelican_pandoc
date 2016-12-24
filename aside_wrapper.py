from bs4 import BeautifulSoup


def process_content(content):

    soup = BeautifulSoup(content, 'html.parser')

    for aside_tag in soup.findAll('aside'):
        tmp = dict(aside_tag.attrs)
        try:
            tmp['id'] = 'div-{}'.format(tmp['id'])
        except:
            pass
        wrap(aside_tag, soup.new_tag("div", **tmp))

    for i, s in enumerate(soup.findAll('sup')):
        s.contents = [u'{}'.format(i+1)]

    content = '\n'.join([unicode(i) for i in soup.contents])
    content = unicode(soup)

    return content


def wrap(to_wrap, wrap_in):
    contents = to_wrap.replace_with(wrap_in)
    wrap_in.append(contents)

