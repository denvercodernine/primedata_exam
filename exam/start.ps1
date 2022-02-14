docker build -t timerservice .\timerservice
docker build -t loggerservice .\loggerservice
docker run -dp 8080:8080 --name timerservice timerservice
docker run -dp 8081:8081 --name loggerservice loggerservice