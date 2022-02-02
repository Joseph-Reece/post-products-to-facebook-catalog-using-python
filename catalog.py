import catalogPlugin as cp
import json

# get user pages obtain page id
# get page catalogs
# get the catalog id

page_id = 'facebook page id'  # page id
catalogID = 'page catalog id'  # catalogID
retailer_id = 'real retailer id'

create_requests = [
    {
        "method": "CREATE",
        "retailer_id": "retailer-6",
        "data": {
            "availability": "in stock",
            "brand": "Nike",
            "color": "Blue",
            "category": "Shoes",
            "description": "Stripped Shoes",
            "image_url": "https://images.unsplash.com/photo-1491553895911-0055eca6402d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
            "name": "Nike Air Max",
            "price": 15500,
            "currency": "KES",
            "condition": "new",
            "url": "https://images.unsplash.com/photo-1491553895911-0055eca6402d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        },
    },
    {
        "method": "CREATE",
        "retailer_id": "retailer-45",
        "data": {
            "availability": "in stock",
            "brand": "Puma",
            "color": "Blue",
            "category": "Shoes",
            "description": "Stripped Shoes",
            "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
            "name": "Puma 300",
            "price": 15000,
            "currency": "KES",
            "condition": "new",
            "url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
        },
    }
]
update_requests = [
    {
        "method": "UPDATE",
        "retailer_id": "retailer-6",
        "data": {
            "availability": "in stock",
            "brand": "Nike",
            "color": "Blue",
            "category": "Shoes",
            "description": "Stripped Shoes",
            "image_url": "https://images.unsplash.com/photo-1491553895911-0055eca6402d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
            "name": "Nikies Air Maxes",
            "price": 15500,
            "currency": "KES",
            "condition": "new",
            "url": "https://images.unsplash.com/photo-1491553895911-0055eca6402d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=580&q=80",
        },
    },
    {
        "method": "UPDATE",
        "retailer_id": "retailer-45",
        "data": {
            "availability": "in stock",
            "brand": "Puma",
            "color": "Blue",
            "category": "Shoes",
            "description": "Stripped Shoes",
            "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
            "name": "Pumas 3000",
            "price": 15000,
            "currency": "KES",
            "condition": "new",
            "url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
        },
    }
]

delete_requests = [
    {
        "method": "DELETE",
        "retailer_id": "retailer-2"
    }
]

def post_products(requests):
    response = cp.post_to_catalog(catalogID, requests)

    # response is a list of handles dicts. They can be used to track progress of batch request.
    print(json.dumps(response, indent=4))
    return response

def update_products(updates):
    response = cp.patch_product(catalogID, updates)

    print(json.dumps(response, indent=4))

def delete_products(catalogID, delete_requests):
    response = cp.delete_product(catalogID, delete_requests)

    print(json.dumps(response, indent=4))

print(update_products(update_requests))
