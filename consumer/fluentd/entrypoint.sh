#!/bin/bash

#!/bin/bash

# Make sure that the Fluentd configuration file is present
if [ ! -f /fluentd/etc/fluent.conf ]; then
  echo "Fluentd config file not found, exiting..."
  exit 1
fi

# Start Fluentd and pass in the configuration file
exec fluentd -c /fluentd/etc/fluent.conf -p /fluentd/plugins "$@"
