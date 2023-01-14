FROM fluent/fluentd:v1.3.0-debian-armhf

# Use root account to use privileged actions
USER root

# Below are the plugins used in this fluentd instance
RUN apt-get update && apt-get install -y ruby-dev
RUN fluent-gem install msgpack
RUN fluent-gem install fluent-plugin-docker-format

# Below are the configurations and scripts used in this fluentd instance
COPY fluent.conf /fluentd/etc/
COPY entrypoint.sh /bin/

# Below are the environment variables used in this fluentd instance
ENV FLUENTD_CONF=fluent.conf

# Below are the ports exposed by this container
EXPOSE 24224

# Below is the command used to start the container
CMD ["/bin/entrypoint.sh"]
