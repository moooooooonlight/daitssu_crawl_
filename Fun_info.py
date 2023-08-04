# 제목, 내용, 이미지, 게시글url, 생성시각, 업데이트 시각
from bs4 import BeautifulSoup
import requests

Fun = "https://fun.ssu.ac.kr/ko/guide/notice/list/"

for i in range(3):
    html = requests.get(Fun+ str(i))
    html_text = html.text
    soup = BeautifulSoup(html_text, 'html.parser')
    tag_ul = soup.find('ul', {"class": "black"})
    print("====================================+"+ str(i)+"page===========================")
    for store in tag_ul.find_all('li',{"class":"tbody notice"}):
        # 공지사항 제목
        store_span = store.find('span',{"class":"title"})
        store_title = store_span.find("a")
        store_title_text = store_title.get_text()
        print(store_title_text)

        # 공지사항 게시글url
        store_title_href = store_title['href']
        print("https://fun.ssu.ac.kr"+store_title_href)

        # 공지사항 내용
        content = "https://fun.ssu.ac.kr"+store_title_href
        html_content = requests.get(content)
        html_content_text = html_content.text
        soup_content = BeautifulSoup(html_content_text, 'html.parser')

        # 공지사항 생성시각
        store_span = soup_content.find('li',{"class":"date"})
        store_date = store_span.find('time')
        store_date_text = store_date.get_text()
        print(store_date_text)

        # 공지사항 내용
        for tag in soup_content.find_all(['p', 'table']):
            # p 태그인 경우
            if tag.name == 'p':
                if tag.find('img'):
                    img_src = tag.find('img')['src']
                    print(f"Image: {img_src}")
                else:
                    # 첨부파일인 경우
                    if tag.find('a'):
                        link_tag = tag.find('a')
                        link_href = link_tag['href']
                        link_text = link_tag.get_text(strip=True)
                        print(f"Link: {link_text} - {link_href}")
                    else:
                        # 동영상인 경우
                        if tag.find('iframe'):
                            link_tag = tag.find('iframe')
                            link_href = link_tag['src']
                            link_text = link_tag.get_text(strip=True)
                            print(f"video Link: {link_text} - {link_href}")
                        # 텍스트인 경우
                        else:
                            text_content = tag.get_text(strip=True)
                            print(f"Text: {text_content}")

            # table 태그인 경우
            elif tag.name == 'table':
                print("Table found! Contents:")
                # 테이블 내의 각 행(<tr>)을 찾기
                for row in tag.find_all('tr'):
                    # 각 셀(<td>)의 내용을 출력
                    row_contents = [cell.get_text(strip=True) for cell in row.find_all('td')]
                    print(" - ".join(row_contents))

        # 공지사항 업데이트 시각

        print("========================================================================================")


    for store in tag_ul.find_all('li',{"class":"tbody"}):
        # 공지사항 제목
        store_span = store.find('span',{"class":"title"})
        store_title = store_span.find("a")
        store_title_text = store_title.get_text()
        print(store_title_text)

        # 공지사항 게시글url
        store_title_href = store_title['href']
        print("https://fun.ssu.ac.kr"+store_title_href)

        # 공지사항 내용
        content = "https://fun.ssu.ac.kr"+store_title_href
        html_content = requests.get(content)
        html_content_text = html_content.text
        soup_content = BeautifulSoup(html_content_text, 'html.parser')

        # 공지사항 생성시각
        store_span = soup_content.find('li',{"class":"date"})
        store_date = store_span.find('time')
        store_date_text = store_date.get_text()
        print(store_date_text)

        # 공지사항 내용
        for tag in soup_content.find_all(['p', 'table']):
            # p 태그인 경우
            if tag.name == 'p':
                if tag.find('img'):
                    img_src = tag.find('img')['src']
                    print(f"Image: {img_src}")
                else:
                    # 첨부파일인 경우
                    if tag.find('a'):
                        link_tag = tag.find('a')
                        link_href = link_tag['href']
                        link_text = link_tag.get_text(strip=True)
                        print(f"Link: {link_text} - {link_href}")
                    else:
                        # 동영상인 경우
                        if tag.find('iframe'):
                            link_tag = tag.find('iframe')
                            link_href = link_tag['src']
                            link_text = link_tag.get_text(strip=True)
                            print(f"video Link: {link_text} - {link_href}")
                        # 텍스트인 경우
                        else:
                            text_content = tag.get_text(strip=True)
                            print(f"Text: {text_content}")

            # table 태그인 경우
            elif tag.name == 'table':
                print("Table found! Contents:")
                # 테이블 내의 각 행(<tr>)을 찾기
                for row in tag.find_all('tr'):
                    # 각 셀(<td>)의 내용을 출력
                    row_contents = [cell.get_text(strip=True) for cell in row.find_all('td')]
                    print(" - ".join(row_contents))

        # 공지사항 업데이트 시각

        print("========================================================================================")
