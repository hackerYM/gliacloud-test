import requests
from bs4 import BeautifulSoup
from marshmallow import Schema, fields

basic_url = "https://www.ptt.cc"
ptt_url = "https://www.ptt.cc/bbs/Soft_Job/index1450.html"
topic_name = "Soft_Job"


class ContentPTT(object):
    def __init__(self, topic, title, content, author, date):
        self.topic = topic
        self.title = title
        self.content = content
        self.author = author
        self.date = date


class PTTSchema(Schema):
    topic = fields.Str()
    title = fields.Str()
    content = fields.Str()
    author = fields.Str()
    date = fields.Str()


def get_web_page(web_url):

    headers = {
        "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    }
    resp = requests.get(url=web_url, headers=headers, timeout=3)  # Connection Timeouts set 3 seconds

    if resp.status_code == 200:
        return resp.text
    else:
        raise requests.exceptions.ReadTimeout("Failed get web page by invalid url.")


def get_sub_web(content_url):

    soup = BeautifulSoup(get_web_page(content_url), 'html.parser')
    content = soup.find("div", "bbs-screen bbs-content").text.strip()

    return content


def web_crawler():

    soup = BeautifulSoup(get_web_page(ptt_url), 'html.parser')
    block_list = soup.find_all("div", "r-ent")

    ptt_object_list = []

    for block in block_list:
        title_data = block.find("div", "title")
        title = title_data.text.strip()
        content = get_sub_web(basic_url + title_data.find("a").get('href'))

        meta_data = block.find("div", "meta")
        author = meta_data.find("div", "author").text.strip()
        date = meta_data.find("div", "date").text.strip()

        ptt_object = ContentPTT(topic_name, title, content, author, date)
        ptt_object_list.append(ptt_object)

    return ptt_object_list


if __name__ == '__main__':

    ptt_object_list = web_crawler()
    ptt_data = PTTSchema().dump(ptt_object_list, many=True).data

    # print(ptt_data)
