## Fake NYC Subway Station bot

This code is for a twitter bot that makes me fake NYC subway stations by shufffling real NYC stations / locations around.
It rejects actual subway stations if it makes one by mistake.

It posts every 6 hours [@fake_nyc_subway](https://www.twitter.com/fake_nyc_subway)

## To run:
Clone the repo and create a file called secret.py alongside bot.py with the following contents:

    consumer_key = 'XXX'
    consumer_secret = 'XXX'
    access_token = 'XXX'
    access_secret = 'XXX'

Then run bot.py

## Acknowledgements
* Based a bit on the simple code that governs my first twitter bot, [@drydernicknames](https://github.com/heavyimage/DRyderNicknames)
* Inspired by [@sametomorrow's](https://www.twitter.com/sametomorrow) amazing [subway station tile resource](http://nytrainproject.com/)
* I used the excellent [tweep dumper](https://gist.github.com/yanofsky/5436496) to download a bunch of [@NYCTSubway](https://www.twitter.com/NYCTSubway)'s tweets to make fake sounding announcement tweets!

## TODO
* Place arbitrary stations somewhere on a map somehow and figure out what trains might go there?
* Figure out if a station is a terminus or not to aid in "XXX-bound YYY trains" etc.
* A real goal for this project is to procedurally generate and render a tile mosaic of the supposed subway station featuring custom nyc subway-like art.
    * I'm now tackling this is in another project for now; watch the skies.
* Create more variations by using other nyc-central sources of content
    * Add in famous recent New Yorkers worthy of a station stop!
    * Add more NYC-y place names that actually don't have subway stations
        * <http://www.oldstreets.com/>
        * <https://data.cityofnewyork.us/City-Government/Street-name-Dictionary/w4v2-rv6b>
        * <https://en.wikipedia.org/wiki/Category:Streets_in_New_York_City>
        * <https://en.wikipedia.org/wiki/List_of_eponymous_streets_in_New_York_City>
        * <https://geographic.org/streetview/usa/ny/new_york.html>
        * <https://streeteasy.com/blog/nyc-places-named-for-african-americans/>
        * <https://streeteasy.com/blog/nyc-presidents-street-names/>
        * <https://untappedcities.com/2013/09/26/history-of-nyc-streets-why-is-there-king-street-prince-street-but-no-queen-or-princess-street-manhattan/>
        * <https://untappedcities.com/2014/03/21/history-of-streets-streets-in-nyc-that-start-with-q-x-y-z/>
        * <https://untappedcities.com/2016/11/16/history-of-streets-10-nyc-neighborhoods-with-thematic-street-names/>
        * <https://www.nycgo.com/articles/nyc-street-name-meanings>
        * <https://www.nytimes.com/2014/02/26/nyregion/honorific-streets-now-cataloged.html>


