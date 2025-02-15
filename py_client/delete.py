
import requests

product_id =input("What is the product id that you want to delete\n")
try:
    product_id=int(product_id)
except:
    product_id =None
    print(f'{product_id} not a valid id')
endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"



get_response=requests.delete(endpoint)

if get_response.status_code == 204:
    print(f"✅ Product {product_id} deleted successfully!")
elif get_response.status_code == 404:
    print(f"⚠️ Product {product_id} not found!")
else:
    print(f"❌ Failed to delete product {product_id}. Status code: {get_response.status_code}")
