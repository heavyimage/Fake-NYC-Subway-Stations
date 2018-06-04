import logging
import time
import re
from random import choice, sample

import tweepy

from secret import *

HASHTAG_INTERVAL = 10

# Setup logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s:\t%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger = logging.getLogger()

# Constants
STATIONLIST = """103rd Street
103rd Street-Corona Plaza
104th Street
110th Street
111th Street
116th Street
116th Street-Columbia University
121st Street
125th Street
135th Street
137th Street-City College
138th Street-Grand Concourse
145th Street
149th Street-Grand Concourse
14th Street
14th Street-Union Square
155th Street
157th Street
15th Street-Prospect Park
161st Street-Yankee Stadium
163rd Street-Amsterdam Avenue
167th Street
168th Street
169th Street
170th Street
174th Street
174th-175th Streets
175th Street
176th Street
181st Street
182nd-183rd Streets
183rd Street
18th Avenue
18th Street
190th Street
191st Street
207th Street
20th Avenue
215th Street
219th Street
21st Street
21st Street-Queensbridge
225th Street
231st Street
233rd Street
238th Street
23rd Street
25th Avenue
25th Street
28th Street
30th Avenue
33rd Street
33rd Street-Rawson Street
34th Street-Herald Square
34th Street-Hudson Yards
34th Street-Penn Station
36th Avenue
36th Street
39th Avenue
40th Street-Lowery Street
42nd Street-Bryant Park
42nd Street-Port Authority Bus Terminal
45th Street
46th Street
46th Street-Bliss Street
47th-50th Streets-Rockefeller Center
49th Street
50th Street
51st Street
52nd Street
53rd Street
55th Street
57th Street
57th Street-Seventh Avenue
59th Street
59th Street-Columbus Circle
61st Street-Woodside
62nd Street
63rd Drive-Rego Park
65th Street
66th Street-Lincoln Center
67th Avenue
68th Street-Hunter College
69th Street
71st Street
72nd Street
74th Street-Broadway
75th Avenue
75th Street-Elderts Lane
77th Street
79th Street
80th Street
81st Street-Museum of Natural History
82nd Street-Jackson Heights
85th Street-Forest Parkway
86th Street
88th Street
90th Street-Elmhurst Avenue
96th Street
Alabama Avenue
Allerton Avenue
Aqueduct Racetrack
Aqueduct-North Conduit Avenue
Astor Place
Astoria Boulevard
Astoria-Ditmars Boulevard
Atlantic Avenue
Atlantic Avenue-Barclays Center
Avenue H
Avenue I
Avenue J
Avenue M
Avenue N
Avenue P
Avenue U
Avenue X
Bay 50th Street
Bay Parkway
Bay Ridge Avenue
Bay Ridge-95th Street
Baychester Avenue
Beach 105th Street
Beach 25th Street
Beach 36th Street
Beach 44th Street
Beach 60th Street
Beach 67th Street
Beach 90th Street
Beach 98th Street
Bedford Avenue
Bedford Park Boulevard
Bedford Park Boulevard-Lehman College
Bedford-Nostrand Avenues
Bergen Street
Beverley Road
Beverly Road
Bleecker Street
Borough Hall
Botanic Garden
Bowery
Bowling Green
Briarwood
Brighton Beach
Broad Channel
Broad Street
Broadway
Broadway Junction
Broadway-Lafayette Street
Bronx Park East
Brook Avenue
Brooklyn Bridge-City Hall
Buhre Avenue
Burke Avenue
Burnside Avenue
Bushwick Avenue-Aberdeen Street
Canal Street
Canarsie-Rockaway Parkway
Carroll Street
Castle Hill Avenue
Cathedral Parkway-110th Street
Central Avenue
Central Park North-110th Street
Chambers Street
Chauncey Street
Christopher Street-Sheridan Square
Church Avenue
City Hall
Clark Street
Classon Avenue
Cleveland Street
Clinton-Washington Avenues
Coney Island-Stillwell Avenue
Cortelyou Road
Cortlandt Street
Court Square
Court Square-23rd Street
Court Street
Crescent Street
Crown Heights-Utica Avenue
Cypress Avenue
Cypress Hills
DeKalb Avenue
Delancey Street
Ditmas Avenue
Dyckman Street
East 105th Street
East 143rd Street-St. Mary's Street
East 149th Street
East 180th Street
East Broadway
Eastchester-Dyre Avenue
Eastern Parkway-Brooklyn Museum
Eighth Avenue
Eighth Street-New York University
Elder Avenue
Elmhurst Avenue
Essex Street
Euclid Avenue
Far Rockaway-Mott Avenue
Fifth Avenue
Fifth Avenue/53rd Street
Fifth Avenue/59th Street
First Avenue
Flatbush Avenue-Brooklyn College
Flushing Avenue
Flushing-Main Street
Fordham Road
Forest Avenue
Forest Hills-71st Avenue
Fort Hamilton Parkway
Fourth Avenue
Franklin Avenue
Franklin Street
Freeman Street
Fresh Pond Road
Fulton Street
Gates Avenue
Graham Avenue
Grand Army Plaza
Grand Avenue-Newtown
Grand Central
Grand Central-42nd Street
Grand Street
Grant Avenue
Greenpoint Avenue
Gun Hill Road
Halsey Street
Harlem-148th Street
Hewes Street
High Street
Houston Street
Howard Beach-JFK Airport
Hoyt Street
Hoyt-Schermerhorn Streets
Hunters Point Avenue
Hunts Point Avenue
Intervale Avenue
Inwood-207th Street
Jackson Avenue
Jackson Heights-Roosevelt Avenue
Jamaica Center-Parsons/Archer
Jamaica-179th Street
Jamaica-Van Wyck
Jay Street-MetroTech
Jefferson Street
Junction Boulevard
Junius Street
Kew Gardens-Union Turnpike
Kings Highway
Kingsbridge Road
Kingston Avenue
Kingston-Throop Avenues
Knickerbocker Avenue
Kosciuszko Street
Lafayette Avenue
Lexington Avenue/53rd Street
Lexington Avenue/59th Street
Lexington Avenue-63rd Street
Liberty Avenue
Livonia Avenue
Longwood Avenue
Lorimer Street
Marble Hill-225th Street
Marcy Avenue
Metropolitan Avenue
Mets-Willets Point
Middle Village-Metropolitan Avenue
Middletown Road
Montrose Avenue
Morgan Avenue
Morris Park
Morrison Avenue-Soundview
Mosholu Parkway
Mount Eden Avenue
Myrtle Avenue
Myrtle-Willoughby Avenues
Myrtle-Wyckoff Avenues
Nassau Avenue
Neck Road
Neptune Avenue
Nereid Avenue
Nevins Street
New Lots Avenue
New Utrecht Avenue
Newkirk Avenue
Newkirk Plaza
Ninth Avenue
Ninth Street
Northern Boulevard
Norwood Avenue
Norwood-205th Street
Nostrand Avenue
Ocean Parkway
Ozone Park-Lefferts Boulevard
Park Place
Parkchester
Parkside Avenue
Parsons Boulevard
Pelham Bay Park
Pelham Parkway
Pennsylvania Avenue
President Street
Prince Street
Prospect Avenue
Prospect Park
Queens Plaza
Queensboro Plaza
Ralph Avenue
Rector Street
Rockaway Avenue
Rockaway Boulevard
Rockaway Park-Beach 116th Street
Roosevelt Island
Saratoga Avenue
Second Avenue
Seneca Avenue
Seventh Avenue
Sheepshead Bay
Shepherd Avenue
Simpson Street
Sixth Avenue
Smith-Ninth Streets
South Ferry
Spring Street
St. Lawrence Avenue
Steinway Street
Sterling Street
Sutphin Boulevard
Sutphin Boulevard-Archer Avenue-JFK Airport
Sutter Avenue
Sutter Avenue-Rutland Road
Third Avenue
Third Avenue-138th Street
Third Avenue-149th Street
Times Square
Times Square-42nd Street
Tremont Avenue
Union Street
Utica Avenue
Van Cortlandt Park-242nd Street
Van Siclen Avenue
Vernon Boulevard-Jackson Avenue
Wakefield-241st Street
Wall Street
West Eighth Street-New York Aquarium
West Farms Square-East Tremont Avenue
West Fourth Street-Washington Square
Westchester Square-East Tremont Avenue
Whitehall Street-South Ferry
Whitlock Avenue
Wilson Avenue
Winthrop Street
Woodhaven Boulevard
Woodlawn
World Trade Center
York Street
Zerega Avenue"""

PLACES = STATIONLIST

# Leave streets / avenues off the list as not to cause pluralization problems
CITY_OBJ = ["street", "avenue", "boulevard", "center", "square",
            "place", "circle", "park", "concourse", "drive", "ferry", "hall",
            "heights", "highway", 'junction', 'lane', 'parkway', 'plaza',
            'point', 'road', 'turnpike', 'yards']
BOROUGH = ["bronx", "queens", "brooklyn"]
NATURAL = ["garden", "green", "hill", "hills", "ridge", "bay", "beach", "island"]
MODIFIER = ["north", "south", "east", "west", "new", "grand", "broad", "far",
             "van", "metropolitan", "middle"]
DIRECTIONAL = ["northern", "southern", "eastern", "western"]
INSTITUTION = ["airport", "university", "station", "college", "museum",
               "aquarium", "racetrack"]
SPELLED_NUMBERS = ["first", "second", "third", "forth", "fifth", "sixth",
                   "seventh", "eighth", "ninth", "tenth", "eleventh",
                   "twelveth"]
LETTER = [chr(c) for c in range(65, 91)]

def ordinal_suffix_of(i):
    """ Python version of: https://stackoverflow.com/a/13627586 """
    j = i % 10
    k = i % 100
    i = str(i)
    if j == 1 and k != 11:
        return i + "st"
    if j == 2 and k != 12:
        return i + "nd"
    if j == 3 and k != 13:
        return i + "rd"
    return i + "th"
NUMBERED = [ordinal_suffix_of(i) for i in range(1, 272)] + SPELLED_NUMBERS

ABBREVIATIONS = {
    'square': 'sq',
    'square': 'sq.',
    'street': 'st',
    'street': 'st.',
    'avenue': 'ave',
    'avenue': 'ave.',
    'road': 'rd',
    'road': 'rd.',
    'boulevard': 'blvd',
    'boulevard': 'blvd.',
}


def get_api():
    """ Access and authorize our Twitter credentials from secrets.py
    and produce api object """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    return api


class Template(object):
    def __init__(self, chunks):
        self.chunks = chunks

        # Set some flags
        if "%" not in "".join(self.chunks):
            self.BAD = True

        self.invariant = " ".join(c.strip()
                for c in re.split("%\w+%", "".join(
                        chunks).replace("-", " "))).strip()

        self.numeric = chunks[0] == "%NUMBERED%"

    def render(self):
        str_ = " ".join(self.chunks)
        str_ = str_.replace(" - ", "-")
        return str_

    def __hash__(self):
        return hash(tuple(self.chunks))
    def __eq__(self, other):
        return self.chunks == other.chunks

    def substitute(self):
        """ Given a template, perform substitutions and return a new place """
        subst = {
                    "%LETTER%" : sample(LETTER, len(LETTER)),
                    "%CITY_OBJ%" : sample(CITY_OBJ, len(CITY_OBJ)),
                    "%MODIFIER%" : sample(MODIFIER, len(MODIFIER)),
                    "%BOROUGH%" : sample(BOROUGH, len(BOROUGH)),
                    "%DIRECTIONAL%" : sample(DIRECTIONAL, len(DIRECTIONAL)),
                    "%NATURAL%" : sample(NATURAL, len(NATURAL)),
                    "%INSTITUTION%" : sample(INSTITUTION, len(INSTITUTION)),
                    "%NUMBERED%" : sample(NUMBERED, len(NUMBERED)),
                }

        output = self.render()
        for key in subst.keys():
            while key in output:
                pop = subst[key].pop()
                if pop[0] not in [str(i) for i in range(10)]:
                    pop = pop.title()
                output = output.replace(key, pop , 1)

        # Don't mistakenly re-create a real place...
        if output in PLACES:
            return self.substitute()

        return output

    def representations(self, substition):
        reps = []
        # Throw away city_obj (eg:pennsylvania station --> pennsylvania)
        reps.append(self.invariant)
        reps.append(".".join(word[0] for word in self.invariant.split(" ") if word))

        substition = substition.lower()
        for search, replace in ABBREVIATIONS.items():
            result = substition.replace(search, replace)
            if result != substition:
                reps.append(result)

        # TODO: abreviate city obj (street --> st. square --> sq, boulevard --> bvld.)
        # th / rd--> superscript w/ underline or dots
        # small glyphs:
            # if numeric just print number
            # else:
                # first letter for each word (sometimes with .s between...?)
                # Just a single letter
        return reps


def make_templates():
    """ Generate templates from strings """
    templates = set()
    items = set(PLACES.split("\n"))

    for item in items:
        output = []

        # 'escape' strange delimiters so subsitutions can happen
        item = item.replace("-", " - ")
        item = item.replace("/", " - ")

        words = item.split(" ")

        # Special Cases
        #
        # Fix eg Avenue X
        if words[0] == "Avenue":
            templates.add(Template(["Avenue", "%LETTER%"]))
            continue

        # Def going to match with a real station
        elif len(words) == 1:
            continue

        for word in words:
            if word.lower() in CITY_OBJ:
                output.append("%CITY_OBJ%")
            elif word.lower() in MODIFIER:
                output.append("%MODIFIER%")
            elif word.lower() in DIRECTIONAL:
                output.append("%DIRECTIONAL%")
            elif word.lower() in BOROUGH:
                output.append("%BOROUGH%")
            elif word.lower() in NATURAL:
                output.append("%NATURAL%")
            elif word.lower() in INSTITUTION:
                output.append("%INSTITUTION%")
            elif word.lower()[0] in [str(i) for i in range(10)] or word.lower() in SPELLED_NUMBERS:
                output.append("%NUMBERED%")
            else:
                output.append(word)

        templates.add(Template(output))

    templates = sorted(templates)

    logger.info("\n".join(t.render() for t in templates))
    logger.info("\n------\n%s templates!\n\n" % len(templates))
    return templates


def main():
    """ entry point """

    counter = 0
    followers = set()

    # Initialize templates once
    templates = make_templates()

    # Main loop
    while True:

        # make
        template = choice(templates)
        station = template.substitute()

        # TODO: Representations -- used for mosaic generation later...
        # reps = template.representations(station)
        # for r in reps:
        #     print "\t", r

        # api
        api = get_api()

        # tweet
        msg = station
        if counter % HASHTAG_INTERVAL == 0:
            msg += " #mta #subway #nysubway"

        api.update_status(msg)
        counter +=1

        # log
        logger.info("Posted msg #%s: %s" % (counter, msg))

        # Check for new followers:
        try:
            for follower in tweepy.Cursor(api.followers).items():
                handle = follower.screen_name
                if handle not in followers:
                    logger.info("New Follower: %s" % handle)
                    followers.add(handle)
        except tweepy.RateLimitError:
            logger.info("Exceeded rate limit searching for followers :-(")

        # sleep for 6 hours
        time.sleep(21600)

if __name__ == "__main__":
    main()
