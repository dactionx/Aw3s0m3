# Open-source library from Kenneth Reitz.
# Library can be found at https://github.com/psf/requests
import requests
# Converts the URL of the privacy policy into the privacy
# policy's text. This was created by our team.
import grabPolicy

# Location to grab list of sites from
fileWithSites = 'Testing Sites.txt'

# Specifying the POST packet's fields. An area of improvement
# is to pass in the fields as an argument instead of hard-coding
# them.
fieldsReference = {'demo':'0', 
        'paper':'', 
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

# Text file contains the labels of the desired metrics to find in the
# returned HTML response. The metrics are parsed and stored into an
# array. Future versions will instead store all returned metrics in the 
# form of a dictionary {metric:data}.
desiredMetricsFile = "desiredMetrics.txt"
fStream = open(desiredMetricsFile, 'r')
desiredMetrics = fStream.read().split('\n')
fStream.close()

# The free online service we are using to analyze privacy policies.
# In future versions a custom-built NLP MLing model will be trained
# on legal documents for better accuracy.
analysisSite = "https://www.slickwrite.com/"
  
# The goal of this module is to POST and GET data to Slick Write
# in order to retrieve statistics associated with a piece of text.

# Imports a list of sites to grab policies from; note this can be
# altered in the future to get a list of sites from a DB.
def getSites(filename):
    fStream = open(filename, 'r')
    
    # The delimiter is newline for the text file
    sites = fStream.read().split('\n')
    fStream.close()
    
    return sites
    
def getPolicies(sites):
    return [(site, grabPolicy.getPolicyText(site)) for site in sites]
    
def getPolicyAnalysis(policy):
    # Make a shallow copy to avoid accidentally changing fieldsReference
    fields = fieldsReference.copy()
    fields['paper'] = policy
    response = requests.post(analysisSite, data = fields)
    
    # We only care about the POST response's text
    return response.text

#def getPolicyMetrics(policyAnalysis):
#    metrics = {}
#    for desiredMetric in desiredMetrics:
        # To do
#    return metrics
    
#def formatStats(site, stats):
