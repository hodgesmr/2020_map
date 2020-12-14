# 2020_map

![2020 map](https://repository-images.githubusercontent.com/312166617/48f6fb80-3e00-11eb-9d19-3d7229d43ddf)

A custom 2020 Electoral College map created by [Matt Hodges](https://hodgesmr1@gmail.com)

 * [Download PNG](https://github.com/hodgesmr/2020_map/blob/main/map.png)

## Build and Run

I built this using Python 3.9, but it probably works with Python 3.6 or later. The fastest way to get up and running is to build and run the [Docker](https://docs.docker.com/get-docker/) image with the provided make target:

```sh
make map
```

This will start the Docker countain mounted to the local `output/` directory, and generate a PNG.

## Keep the Faith!

Faith was one of the core values of the [2020 Biden Campaign Code](https://web.archive.org/web/20201102041950/https://joebiden.com/joes-codes/):

>What I mean by faith in this sense is a belief that you can do extraordinary things, whatever the odds. When I would walk out of my Grandpa Finnegan’s house in Scranton, he would tell me, “Joey, keep the faith.” My grandmother would always yell back, “no, Joey, spread it—spread the faith!” On our campaign, “keep the faith” has always been more than just a saying; it’s a call to keep moving forward, to keep believing, to keep doing what’s right even when the path ahead is murky and the goal feels far away. Through low lows and high highs, our campaign staff and volunteers have kept the faith as we pursued this nomination. We’ve never despaired, and never given up—and as long as we have faith, we never will.

On election night, when results were uncertain and millions of votes were still yet to be counted, Joe Biden had one message for supporters: [Keep the faith](https://twitter.com/JoeBiden/status/1323865811031785472).

A trace of President Biden's [hand-written message](https://twitter.com/hoeflerco/status/1324088537336193024) is featured on this map.

## Licenses

All original code is provided under the [BSD 3-Clause license](https://github.com/hodgesmr/2020_map/blob/master/LICENSE).

This project uses the [Jost* font](https://indestructibletype.com/Jost.html), which is licensed under the [SIL open font license](http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web). The font is included in this repository.

The state geography geojson files are derived from the [U.S. Census Bureau's Cartographic Boundary Files](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html).

Any original output images completely generated by this code are hereby released into the public domain, insofar as I'm able to do so.

It is unclear to me who, if anyone, has copyright on the "Keep The Faith" trace provided in this repository. Nevertheless, I believe that I have used it within the bounds of the [fair use provision](https://www.law.cornell.edu/uscode/text/17/107) as this repository:

* Serves non-commercial, educational, scholarly, or research use
* Is transformative
* Cites published, fact-based content
* Uses minimum and insignificant content
* Has no market effect

## A Matt Hodges project

This project is maintained by [@hodgesmr](http://twitter.com/hodgesmr).

_Please use it for good, not evil._
