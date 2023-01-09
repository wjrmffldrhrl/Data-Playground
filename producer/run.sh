docker rm -f producer
docker run -d --network data-playground \
    --name producer \
    -p 9001:9001 \
    -t producer