# Use the official fluentd image as the base image
FROM fluent/fluentd:v1.15-debian-armhf-1

# Copy the configuration file and entrypoint script into the container
COPY fluent.conf /fluentd/etc/
COPY entrypoint.sh /

USER root
RUN mkdir -p /home/fluent/.local/share/gem/ruby/3.1.0/cache/ && chown -R fluent:fluent /home/fluent/.local/share/gem/

# Install the necessary plugins
RUN fluent-gem install fluent-plugin-kafka

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]