import requests

respone=requests.get('https://jsonplaceholder.typicode.com/posts')


if respone.status_code==200:
    json_data=respone.json()
    print('thanh cong')

    for post in json_data:
        print("userID", post['userId'])
        print("ID",post['id'])
        print("title",post['title'])
        print("body",post['body'])
    print('tong so bai post:', len(json_data))
else:
    print('khong thanh cong, ma trang thai:', respone.status_code)

