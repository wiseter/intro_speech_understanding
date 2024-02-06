import bs4
from bs4 import BeautifulSoup
from gtts import gTTS

def extract_stories_from_NPR_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    # 假设新闻故事在 div 标签类 'story-text' 下
    stories_elements = soup.find_all('div', class_='story-text')  
    stories = []
    for elem in stories_elements:
        # 可能需要根据实际 HTML 结构调整这里的选择器
        title = elem.find('h3').get_text(strip=True) if elem.find('h3') else ''
        teaser = elem.find('p', class_='teaser').get_text(strip=True) if elem.find('p', class_='teaser') else ''
        stories.append((title, teaser))
    return stories

def read_nth_story(stories, n, filename):
    if n < 0 or n >= len(stories):
        raise ValueError("Story index out of range")
    story = stories[n]
    text_to_read = story[0] + ". " + story[1]
    tts = gTTS(text=text_to_read, lang='en')
    tts.save(filename)
