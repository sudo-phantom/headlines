import feedparser
from flask import Flask , render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
	     'cnn': 'http://rss.cnn.com/rss/edition.rss',
	     'fox': 'http://feeds.foxnews.com/foxnews/latest',
	     'hackernews': 'http://news.ycombinator.com/rss'}
#BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
@app.route("/<publication>")

def get_news(publication="bbc"):
	feed = feedparser.parse(RSS_FEEDS[publication])
	'''render_template("home.html",
					title=first_article.get("title"),
					published=first_article.get("published"),
					summary=first_article.get("summary"))'''
	return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
	app.run(port=5000, debug=True)
