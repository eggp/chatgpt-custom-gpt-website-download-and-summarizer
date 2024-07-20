# Mire jo?

HTML fajlokon tud vegig menni es abban a `main` es `article` elemek menten a tartalmat kiszedi a html-bol es gpt-nek megfeleloen probalja formazni.
A vegen kapunk egy txt-t amit a gpt-nek tanulasra oda is adhatunk.
(Amennyiben specialis oldal-val talalkozzunk akkor a main.py-t modositani kell, erre pelda angular.dev -hez => main-angular.py, 
ha modositod akkor erdemes a main.py-be irni mert akkor a docker es egyeb fajlokat nem kell atirni)

### Docker build

`docker build -t html-summarizer .`

### Run in docker

Mielott futtatod, a project gyokerbe egy mappaba masold be a html fajlokat es azt add meg a `yourhtmlfilesdirectory` helyen.

`docker run -v ./yourhtmlfilesdirectory:/app/html_files -v ./summaries:/app/summaries html-summarizer`

Valoszinuleg fogsz warning-okat kapni, de ne torodj vele... 
(Sajnos nagyon sok ideig fog futni, peldaul egy mac studio 2 ultra-n a sass-lang.com feldolgozasa tobb ora volt) 
