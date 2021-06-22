# Counter app for OBS
Download [docker-compose.yml](https://raw.githubusercontent.com/TheTrueCoder/stream-counter/main/docker-compose.yml) and run it with:

`docker-compose up -d`

Then on local system visit: [http://localhost](http://localhost)

# Manual
Run nginx webserver and run flask api server and head to [http://localhost/?endpoint=localhost:5000](http://localhost/?endpoint=localhost:5000). Or just run flask and open the html file in your browser and add `?endpoint=localhost:5000` to the end.