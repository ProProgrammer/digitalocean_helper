The code here requires:
* [digitalocean python library](https://github.com/koalalorenzo/python-digitalocean)
* Access to [Digital Ocean API token](https://www.digitalocean.com/docs/api/create-personal-access-token/)
* Digital Ocean API token added as [environment variable](https://www.twilio
.com/blog/2017/01/how-to-set-environment-variables.html) named `DO_API_TOKEN`

Sample usage:
* Clone the repository where you want to run the commands
* Navigate to digitalocean_helper directory

```python
import os
import only_file

API_TOKEN = os.environ["DO_API_TOKEN"]

manager = only_file.get_digitalocean_manager(api_token=API_TOKEN)

# list all active droplets
all_droplets = only_file.list_active_droplets(manager)

# get a droplet instance
droplet = all_droplets[0]

# Check if a droplet is shutdown
only_file.is_droplet_shutdown(droplet)

# Turn off a droplet
only_file.shutdown_droplet(droplet)

# Destroy all turned off droplets
only_file.destroy_turnedoff_droplets(manager)

```