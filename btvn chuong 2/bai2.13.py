import requests

respone=requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')

if respone.status_code==200:
    json_data=respone.json()
    print('danh sach cac bai post noi bat:')

    print('---------')    
    for posts in json_data:
        print('-',posts['name'])

    print('-'*10)
    print('thong tin cac bai post(lay 3 bai dau): ')
    for post in json_data[:3]:
        print('postId',post['postId'])
        print('id',post['id'])
        print('name',post['name'])
        print('email',post['email'])
        print('body',post['body'])
        print('         ')

else:
    print('khong thanh cong')