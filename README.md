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

## TODO
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

    * Rendering support
        * A real goal for this project is to procedurally generate and render a tile mosaic of the supposed subway station featuring custom nyc subway-like art.


## Mosaic Rendering
### Pipeline
* Generate names
    * Excecute name generation code in Blender or passin?
    * Choose representation based on multiple sign conventions (fort --> ft; boulevard --> blvd.etc)
* Decide some properties of the mosaiac
    * age of "station"
    * color scheme w/ variations
        * inherit from original station options?
        * 2 - 5 colors max but a "color" can have slight variantions in tiles of that color
* Build scene:
    * Create regionmap:
        * block but not also ---____---- sorta stuff
        * always mirrored on x, not nessisarily on y
        * inner most region must fit stationname
        * assign depth
        * ??? clip corners of regionmap or join with others?
        * Add tiny accent regions that are diamons or other shapes
    * Create tiles within each region
        * rules:
            * outer tiles are either  4 3/8" x 4 3/8" or 6x3 (NOT ALWAYS WHITE but OFTEN)
            * each inner tile region has an integer scale on tiles
            * white text, white walls
            * each tile should draw it's own grout
            * clip tiles to region
        * options:
            * staggered tiles
    * Color tiles:
        * checkboard
        * random w/ differnt weights
        * solid colors
    * Add name of station:
        * cushing?
    * "render" scene (2d image, layering regions)
* Export tile positions
* Geo generation
    * varying depths?
    * roundess?
    * add materials to geo
        * colors
        * aged vs. shiny
    * missing / damaged tiles?
* Displace / warp geo
* Render
* Comp
    * lens distortion?
    * chromab
    * instagram-esque filters?
* Post on twitter

### Resources
* [Incredible NYC subway station tile resource](http://nytrainproject.com/)
* [NYC Subway font analysis](https://www.aiga.org/the-mostly-true-story-of-helvetica-and-the-new-york-city-subway)
* [Subway tile design resources](http://www.nysubwaymosaics.com/design.html)
* [Tile Shading](https://www.youtube.com/watch?v=NDIZvJyMj1o)
* [Procedural Tile Material](https://www.youtube.com/watch?v=PobPKHuX8pM)
* [Dead Easy Tiles](https://www.youtube.com/watch?v=H-quCLfoHbk)
