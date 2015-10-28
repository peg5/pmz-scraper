# pmz-scraper
What It Does

A Python script that scrapes the New Releases section of ProgMetalZone.com for the names of bands and writes them to a CSV file.

Why I Wrote It

I am always looking for new prog metal bands to listen to. Rather than visit ProgMetalZone.com routinely to check for new bands, I wrote a script to do that for me and also to record them so that I have a list of bands to listen to and check them off as I go.

How to Use It

Make sure you have the requests, beautifulsoup (bs4) and csv Python modules imported.
Thenn, simply run the script, via either:

-the command line
-the Python IDLE
-double-clicking the script, assuming you've got your environment set up to support that

You will see a message indicating that it is finished running. Afterwards, you will notice that you have a new file in the same directory as the script called bands.csv. This contains the names of all the bands listed on the front page of the New Releases section of ProgMetalZone.com.
