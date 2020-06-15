# Open-source repo from Kenneth Reitz.
# Repo can be found at https://github.com/psf/requests
import requests
# Open-source repo from Aaron Swartz.
# Repo can be found at https://github.com/Alir3z4/html2text
import html2text

# The goal of this module is to convert the URL of where the
# privacy policy is located at into the policy's text.

def getPolicyHTML(url):
    # Server's response to HTTP request
    response = requests.get(url)
    
    # Return the text of the HTTP response
    return response.text

def convertHTMLToReadableText(htmlPage):
    # Only interested in text, don't care about formatting
    htmlParser = html2text.HTML2Text()
    htmlParser.ignore_links = True
    htmlParser.ignore_images = True
    htmlParser.ignore_emphasis = True
    
    return htmlParser.handle(htmlPage)

def getPolicyText(url):
    htmlPage = getPolicyHTML(url)
    policyText = convertHTMLToReadableText(htmlPage)
    
    return policyText