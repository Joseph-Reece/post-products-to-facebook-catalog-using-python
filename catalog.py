import json
from catalogPlugin import PageCatalog, get_catalog_products, get_batch_status, post_to_catalog, patch_product, delete_product

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


def posting_to_catalog():
    obj = PageCatalog()
    
    response = post_to_catalog(create_requests, obj)    
    
    return response


# print(posting_to_catalog())

def update_products(updates):
    obj = PageCatalog()
    
    response = patch_product(obj, updates)

    print(json.dumps(response, indent=4))
    return response


def delete_products(delete_requests):
    obj = PageCatalog()
    response = delete_product(obj, delete_requests)

    print(json.dumps(response, indent=4))
    return response


# print(update_products(update_requests))
