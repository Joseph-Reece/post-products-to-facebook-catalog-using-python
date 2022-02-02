import requests
import json

# Your Access Keys
access_token = 'paste your access token here'

baseURI = 'https://graph.facebook.com/v12.0/'


# get user info graph api


def get_user_info(page_id):
    node = '{}?fields=about,name,picture&access_token={}'.format(page_id, access_token)
    url = baseURI + node
    try:
        response = requests.get(url).json()

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    return response

# get users pages graph api


def get_user_pages():
    node = '/me/accounts?access_token={}'.format(access_token)
    url = baseURI + node
    try:
        response = requests.get(url).json()  # the pages owned by the user
        # print(json.dumps(response, indent=4))
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    return response

# print(get_user_pages())

# get page catalogs
def get_page_catalogs(page_id):
    node = f'{page_id}/product_catalogs?access_token={access_token}'
    url = baseURI + node

    try:
        response = requests.get(url).json()  # catalogs owned by the page

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    return response

# post batch to catalog


def post_to_catalog(catalog_id, products):
    product_batch = {
        "allow_upsert": True,
        "requests": f'{products}'
    }

    node = f'{catalog_id}/batch?access_token={access_token}'
    url = baseURI + node
    try:
        response = requests.post(url, json=product_batch).json()

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

    return response


# get catalog products


def get_catalog_products(catalog_id):
    node = f'{catalog_id}/products?access_token={access_token}'
    url = baseURI + node
    response = requests.get(url).json()
    return response

# get batch request status


def get_batch_status(catalogID, handle):
    # handle2 = 'AcyYxsVFUZsAP64vf8oHUOQPTfxOuwqN7jKcYhSmYy586iDCGIJb3wI7PizG8tUvUeMZe-1CElXWGg2-0Dk325Q_'

    node = f'{catalogID}/check_batch_request_status?handle={handle}&access_token={access_token}'
    url = baseURI + node
    response = requests.get(url).json()

    return response

# patch product in catalog


def patch_product(catalog_id, products):
    product_batch = {
        "allow_upsert": False,
        "requests": f'{products}'
    }

    node = f'{catalog_id}/batch?access_token={access_token}'
    
    url = baseURI + node
        
    response = requests.post(url, json=product_batch).json()
    
    return response


# delete product in catalog


def delete_product(catalogID, products):

    productBatch = {
        "allow_upsert": False,
        "requests": f'{products}'
    }

    node = f'{catalogID}/batch?access_token={access_token}'
    url = baseURI + node
    response = requests.post(url, json=productBatch).json()

    return response

# get catalog statistics


def get_catalog_statistics(catalog_id):

    # {{catalog_id}}/event_stats?access_token={{access_token}}

    node = f'{catalog_id}/event_stats?access_token={access_token}'
    url = baseURI + node
    response = requests.get(url).json()
    return response
