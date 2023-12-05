import feedparser, time

URL="https://ppaekkomlog.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """

![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=WELCOME&desc=Chan's%20Github%20Profile&descAlignY=70&descAlign=70&fontSize=90)

<h3 align="center"> Hi👋🏻, I'm ChanHeum!😄</h3>

---
<h4 align="center" > I am junior back-end developer who love development </h4>

<h4 align="center">❗ Contact Me! ❗</h4>
<p align="center">
<a href="mailto:33cks1423@naver.com"><img src="https://img.shields.io/badge/Email-Green?style=flat-square&logo=Gmail&logoColor=white&link=mailto:333cks1423@naver.com"/></a>
<p>

<h4 align="center">💡 Back Tech Stack 💡</h4>
<p align="center">
<img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white"/> 
 <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white"/>

</p>

---

<h3 align="center"> 💡 My BackJoon Tier💡</h3>
<p align="center">
  <a href="https://github.com/fineman999">
    <img align="center" src="http://mazassumnida.wtf/api/v2/generate_badge?boj=fineman999" />
  </a>
</p>

<h3 align="center">💡 My Most Used Languages 💡</h3>
<p align="center">
 <a href="https://github.com/fineman999">
    <img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=fineman999&layout=compact&show_icons=true&show_owner=false&hide_title=true&theme=nord"/>
  </a>
</p>
<h3 align="center"> 💡 My Git Stats💡</h3>

<p align="center">
  <a href="https://github.com/fineman999">
    <img align="center" src="https://github-readme-stats.vercel.app/api?username=fineman999&show_icons=true&theme=radical&hide_title=true" />
  </a>
</p>

---
<h3 align="center"> 💡 My AWS Certification 💡</h3>

<!--START_SECTION:badges-->
[![AWS Certified Developer – Associate](https://images.credly.com/size/110x110/images/b9feab85-1a43-4f6c-99a5-631b88d5461b/image.png)](http://www.credly.com/badges/4f9ef0af-26da-4e6c-9a4e-b4104fd1a559 "AWS Certified Developer – Associate")
[![AWS Certified Cloud Practitioner](https://images.credly.com/size/110x110/images/00634f82-b07f-4bbd-a6bb-53de397fc3a6/image.png)](http://www.credly.com/badges/4ddde47f-aa17-443a-9729-dc28e59f7f89 "AWS Certified Cloud Practitioner")
<!--END_SECTION:badges-->

## ✅ Latest Blog Post

"""  

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    feed_date = feed['published_parsed']
    markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
    
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
    
