from dataclasses import asdict, dataclass
import requests
import json

baseURI = 'https://graph.facebook.com/v12.0/'


@dataclass(order=True)
class User:
    access_token: str = "EAAJeF4dYgocBACSrW8MeRS0Ijlk9CAuZABTwNZAcww8zOvkiwO3T7Khpz8vNximT9fw77e8ZBd9E5ouwU9XxMrF4BUb2Y7ZChzn8Xd7GzBPR92h4NUWJvLTrzQH4nJDusTgY1apDE3TG4umsZCHqSYSPPeASZAjvys3NgGi14mZAAZDZD"
    page_id: int = 108685848177921
    name: str = ''


def main(self):
    print(self.page_id)
    print(self.name)


def get_user_pages(self):
    node = '/me/accounts?access_token={}'.format(self.access_token)
    url = baseURI + node
    try:
        response = requests.get(url).json()  # the pages owned by the user

        print(json.dumps(response, indent=4))

        # replace the page id with the first page id

        page_id = response['data'][0]['id']
        name = response['data'][0]['name']

        self.page_id = page_id
        self.name = name

        # print(self.name)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response


def get_user_info(self):
    node = '{}?fields=about,name,picture&access_token={}'.format(
        self.page_id, self.access_token)
    url = baseURI + node
    try:
        response = requests.get(url).json()
        # print(json.dumps(response['id'], indent=4))

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response

# get page catalogs
def get_page_catalog(self):
    node = f'{self.page_id}/product_catalogs?access_token={self.access_token}'
    url = baseURI + node

    try:
        response = requests.get(url).json()  # catalogs owned by the page

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    return response

# print(get_page_catalog(User()))

@dataclass(init=True, order=True)
class PageCatalog(User):
    catalog_id: int = 207229511605716


def post_to_catalog(products, self):

    product_batch = {
    "allow_upsert": True,
    "requests": f'{products}'
    }

    node = f'{self.catalog_id}/batch?access_token={self.access_token}'
    url = baseURI + node
    try:
        response = requests.post(url, json=product_batch).json()

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response

# get catalog products


def get_catalog_products(self):
    node = f'{self.catalog_id}/products?access_token={self.access_token}'
    url = baseURI + node
    response = requests.get(url).json()
    return response

def get_batch_status(self, handle):
    # handle = 'AcyYxsVFUZsAP64vf8oHUOQPTfxOuwqN7jKcYhSmYy586iDCGIJb3wI7PizG8tUvUeMZe-1CElXWGg2-0Dk325Q_'

    node = f'{self.catalogID}/check_batch_request_status?handle={handle}&access_token={self.access_token}'
    url = baseURI + node
    response = requests.get(url).json()

    return response


# patch product in catalog


def patch_product(self, products):
    product_batch = {
        "allow_upsert": False,
        "requests": f'{products}'
    }

    node = f'{self.catalog_id}/batch?access_token={self.access_token}'
    
    url = baseURI + node
        
    response = requests.post(url, json=product_batch).json()
    
    return response


# delete product in catalog


def delete_product(self, products):

    productBatch = {
        "allow_upsert": False,
        "requests": f'{products}'
    }

    node = f'{self.catalogID}/batch?access_token={self.access_token}'
    url = baseURI + node
    response = requests.post(url, json=productBatch).json()

    return response

# get catalog statistics


def get_catalog_statistics(self):

    # {{catalog_id}}/event_stats?access_token={{access_token}}

    node = f'{self.catalog_id}/event_stats?access_token={self.access_token}'
    url = baseURI + node
    response = requests.get(url).json()
    return response

# print(__post_to_catalog(self=Catalog()))


@dataclass(order=True)
class ProductItem:
    availability: str = ""  # in stock, out of stock, preorder, etc
    brand: str = ""  # Nike, Puma, etc
    color: str = ""  # Blue, Red, etc
    name: str = ""  # name of the product
    category: str = ""  # Shoes, T-Shirts, etc
    image_url: str = ""  # url of the image
    description: str = ""  # Stripped Shoes, etc
    price: int = 0  # price of the product
    currency: str = ""  # currency of the product
    condition: str = ""  # new, used, refurbished, etc
    url: str = ""  # url of where the product can be bought from


def main():
    product = ProductItem('in stock', 'Nike', 'Blue', 'Nike pro', 'Stripped Shoes', 'https://images.unsplash.com/photo-1491553895911-0055eca6402d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80',
                          'Nike Air Max', 15500, 'KES', 'new', 'https://images.unsplash.com/photo-1491553895911-0055eca6402d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80')
    # product = ProductItem('nike')
    print(asdict(product))
    return product