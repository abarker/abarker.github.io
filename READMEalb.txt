#!albNotes

Note that preview does not copy the files to the `master` branch, just to the
`output` directory.  Use `publish` to also update `master` branch.

## indexing with Google

To update on Google there is a file in the `content/static_html` dir (set in the
`STATIC_PATHS` config list) to verify ownership.  Then:
   1) goto https://www.google.com/webmasters/tools/ 
   2) log in
   3) click on site name already set up and verified
   4) Click Crawl->Fetch as Google to get realtime (maybe) crawling
See:
   https://stackoverflow.com/questions/9466360/how-to-request-google-to-re-crawl-my-website

Some say that submitting a new sitemap makes Google crawl it (if it didn't
with above way).

