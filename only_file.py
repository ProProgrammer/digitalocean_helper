import digitalocean
import requests


def get_digitalocean_manager(api_token):
    return digitalocean.Manager(token=api_token)


def list_active_droplets(digitalocean_manager):
    return digitalocean_manager.get_all_droplets()


def is_droplet_shutdown(droplet):
    droplet_actions = droplet.get_actions()
    most_recent_droplet_action = droplet_actions[0]
    return most_recent_droplet_action.type == 'power_off' and most_recent_droplet_action.status == 'completed'


def shutdown_droplet(droplet):
    return droplet.shutdown()


def delete_droplet(droplet, api_token):
    print 'droplet:', droplet
    print 'api_token:', api_token
    delete_api_endpoint = "https://api.digitalocean.com/v2/droplets/{droplet_id}".format(droplet_id=droplet.id)
    headers = {
        'Authorization': 'Bearer {api_token}'.format(api_token=api_token),
    }
    return requests.delete(delete_api_endpoint, headers=headers)


def destroy_turnedoff_droplets(digitalocean_manager):
    all_droplets = list_active_droplets(digitalocean_manager)
    for droplet in all_droplets:
        print 'droplet in destroy_turnedoff_droplets:', droplet
        print 'type of droplet:', type(droplet)
        if is_droplet_shutdown(droplet):
            response = delete_droplet(droplet, digitalocean_manager.token)
            print '{droplet} deleted, response: {response}'.format(droplet=droplet, response=response)
