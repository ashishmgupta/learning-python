from bs4 import BeautifulSoup
# file name = website.html
contents = ""
with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')

# Get the anchor tag with the URL "https://angelabauer.github.io/cv/contact-me.html"
# <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>
# Use soup.find_all(tagname=<>, attributename=<>)
all_anchor_tags = soup.find_all(name="a", href="https://angelabauer.github.io/cv/contact-me.html")
for anchor_tag in all_anchor_tags:
    print(anchor_tag.getText())
    print(anchor_tag.get("href"))


# Get the anchor tag which is nested in a p > em > strong tag
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
# Use soup.select_one(selector=<nested tag order>)
company_url = soup.select_one(selector="p em strong a")
print(company_url.getText())
print(company_url.get("href"))

# Get all headings using soup.select(<tag name>)
all_headings = soup.select("h3")
print(all_headings)

# Get all headings using soup.find_all(name=<tag name>)
all_headings3 = soup.find_all(name="h3")
print(all_headings3)
