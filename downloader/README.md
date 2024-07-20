# Mire jó?

A python script egy megadott url-t letölt Httrack segitsegevel.
Felhivas:
Sajnos valamiert letolt kapcsolod oldalakat is, azt olyankor nyugodtan toroljuk a kimenetbol.

### Docker build

`docker build -t web-downloader .`

### Run in docker

`docker run --platform linux/arm64 -e WEBSITE_URL="https://yourpage.com" -e DOWNLOAD_DIRECTORY="/app/SITENAME" -v $(pwd):/app -v $(pwd)/script:/app/script web-compressor`

`WEBSITE_URL` -nek fel vennie azt az url cimet amit le kell tolteni
`DOWNLOAD_DIRECTORY` ez mindig /app -val kezododik mert azt mountoljuk. Utana adj meg egy nevet, ami letre fog jonni(javasoljuk elore letrehozni) a project gyokerbe es oda kerul a site lementesre.

A `DOWNLOAD_DIRECTORY`-ba letrejovo mappaban talalod a site url-vel elatott mappat. Arra lesz szukseged.

### Takaritas

Sajnos a httrack annak ellenere hogy beallitottuk hogy mit toltson le, letolt neha kepeket vagy js vagy css fajlokat is :( 
Erre csinaltunk egy nodejs script-et. A `delete.js`, mielott futtatod a fajlt szerkeszd es a legaljan allitsd be az utvonalat.
