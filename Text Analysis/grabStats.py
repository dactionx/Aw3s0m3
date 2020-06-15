# Open-source library from Kenneth Reitz.
# Library can be found at https://github.com/psf/requests
import requests 
  
# The goal of this module is to POST and GET data to Slick Write
# in order to retrieve statistics associated with a piece of text.

# TO-DO: Actual text needs to go here. Sample used for debugging
# purposes.
req_text = ''' 
this is a test
can this be read?
'''

# The URL we wish to POST and GET data from
ENDPOINT = "https://www.slickwrite.com/"
  
# Specifying the POST packet's fields. A possible area of
# improvement is to pass in the fields as an argument instead of
# hard-coding them.
data = {'demo':'0', 
        'paper':req_text, 
        'preset':'custom', 
        'critiquenotdialog':'1',
        'capitalization':'1',
        'extraspace':'1',
        'doubled':'1',
        'samestart':'1',
        'excessiveprepositions':'1',
        'longsentence':'1',
        'longsentencelimit':'40',
        'passive':'1',
        'wordy':'1',
        'doubleneg':'1',
        'adverb':'1',
        'cliche':'1'
} 

# POST
r = requests.post(url = ENDPOINT, data = data) 
  
# Reading POST response
site_response = r.text 
print("The text is:%s"%site_response) 
