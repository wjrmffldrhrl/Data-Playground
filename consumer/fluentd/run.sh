docker build -t fluentd .
docker rm -f fluentd
docker run -d  --network data-playground \
    --name fluentd fluentd
