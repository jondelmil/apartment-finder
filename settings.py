import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 700

# The maximum rent you want to pay per month.
MAX_PRICE = 900

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'austin'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
# unnecessary for Austin -jdm
# AREAS = ["eby", "sfc", "sby", "nby"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "south_congress": [
        [30.217319, -97.735877],
        [30.261291, -97.762656],
    ],
    "south_lamar": [
        [30.228518, -97.762485],
        [30.249503, -97.793555],
    ],
    "bouldin": [
        [30.24194, -97.750297],
        [30.264368, -97.76418],
    ],
    "zilker": [
        [30.245314, -97.764351],
        [30.265406, -97.799714],
    ],
    "hyde_park": [
        [30.296684, -97.711008],
        [30.317729, -97.738559],

    ],
    "east_austin": [
        [30.26396, -97.697167],
        [30.283233, -97.7321],
    ],
    "tarrytown": [
        [30.27634, -97.758536],
        [30.307467, -97.784543],
    ],
    "east_cesar_chavez": [
        [30.248354, -97.704914],
        [30.264071, -97.737572],
    ],
    "clarksville": [
        [30.269594, -97.752335],
        [30.287383, -97.768471],
    ],
    "downtown": [
        [30.262218, -97.731049],
        [30.289384, -97.756541],
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["south congress", "south lamar", "bouldin", "zilker", "travis heights", "barton hills", "hyde park",
                 "east austin", "westfield", "tarrytown", "east cesar chavez", "clarksville", "downtown"]


## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60  # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
