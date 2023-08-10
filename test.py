import requests as rq


BASE_URL = "http://127.0.0.1:8000"
TOKEN = "32e773268e32bfd62119896e7d0a5258143f6d33"




# ---------------- USERS ----------------

# create_user = rq.post(f'{BASE_URL}/api/v1/users/register',
#                         data={
#                             "name":"Sarvarbek",
#                             "mail":"Sarvarbek.Aminov01@mail.ru",
#                             "password":654321
#                         },
#                         headers={'Authorization':f'Token {TOKEN}'})


# detail_user = rq.get(f'{BASE_URL}/api/v1/users/user/detail/5',
#                         headers={'Authorization':f'Token {TOKEN}'})


# update_user = rq.put(f'{BASE_URL}/api/v1/users/user/update/5',
#                         data={
#                             "name":"Sarvar",
#                             "mail":"Sarvarbek@gmail.com",
#                             "password":654321
#                         },
#                         headers={'Authorization':f'Token {TOKEN}'})





# print(create_user.json(), create_user)
# print(detail_user.json(), detail_user)
# print(update_user.json(), update_user)


# ------------------ PRODUCTS - ----------------

# create_product = rq.post(f'{BASE_URL}/api/v1/products/create',
#                         json={
#                             "name":"Vitamin",
#                             "description":"C vitaminli dori.",
#                             "price":21000,
#                             "daily_amount":2,
#                             "number":5,
#                             "worker":{
#                                 "worker_id":2,
#                                 "name":"Ischi 1",
#                                 "mail":"ishchi1@gmail.com"
#                             },
#                             "user":5
#                         },
#                         headers={'Authorization':f'Token {TOKEN}'})


# detail_product = rq.get(f'{BASE_URL}/api/v1/products/product/detail/4',
#                         headers={'Authorization':f'Token {TOKEN}'})


# update_product = rq.put(f'{BASE_URL}/api/v1/products/product/update/1',
#                         json={
#                             "name":"Vitamin C",
#                             # "description":"C vitaminli dori.",
#                             # "price":21000.0,
#                             # "daily_amount":2,
#                             # "number":5,
                              # "user":5,
#                             # "worker":{
#                             #     "name":"Test user",
#                             #     "mail":"Ishchi3@gmail.com"
#                             # }
#                         },
#                         headers={'Authorization':f'Token {TOKEN}'})


# delete_product = rq.delete(f'{BASE_URL}/api/v1/products/product/delete/4',
#                         headers={'Authorization':f'Token {TOKEN}'})

# user_products = rq.get(f'{BASE_URL}/api/v1/products/user-products/5',
#                         headers={'Authorization':f'Token {TOKEN}'})

# print(create_product.json(), create_product)
# print(detail_product.json(), detail_product)
# print(update_product.json(), update_product)
# print(delete_product.json(), delete_product)
# print(user_products.json(), user_products)

# ------------------- ACTIONS -------------------

# user_and_worker_product = rq.get(f'{BASE_URL}/api/v1/actions/user-products/5/2',
#                         headers={'Authorization':f'Token {TOKEN}'})



# print(user_and_worker_product.json(), user_and_worker_product)