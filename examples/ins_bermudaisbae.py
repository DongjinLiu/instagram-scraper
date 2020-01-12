from context import Instagram # pylint: disable=no-name-in-module
import time
import random
import os

# proxies = {
#     'http': 'http://123.45.67.8:1087',
#     'https': 'http://123.45.67.8:1087',
# }

print('begin...')
instagram = Instagram()
# instagram.with_credentials('JJPtest123', 'jjptest', '/pathtocache')
# instagram.login()
# print('login success')

# If account is public you can query Instagram without auth

instagram = Instagram()

#f = open('lilmiquela.txt', 'w', encoding="utf-8")

#account_name = input("The account name: ")
#account_post_number = input("The number of post: ")
#medias = instagram.get_medias(account_name, account_post_number)

#https://www.instagram.com/bermudaisbae/
account_name = "bermudaisbae"
account_post_number = 248 

medias = instagram.get_medias(account_name, account_post_number)
print('get medias success')

def time_tran(created_at):
    time_local = time.localtime(created_at)
    created_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return created_time

#media = medias[0]
#account = media.owner
#print(account.get_username())

if __name__ == '__main__':
    print('begin scraper')
    for media in medias:
        #f = open('bermudaisbae No ' + str(cont) +' .csv', 'w')
        if(os.path.exists('E:\\instagram-scraper\\examples\\' +account_name +'\\'+ media.get_short_code() +' .csv')):
            continue
        f = open('E:\\instagram-scraper\\examples\\' +account_name +'\\'+ media.get_short_code() +' .csv', 'w', encoding="utf-8")
        #https://www.instagram.com/p/B3P2xNAHes2/
        f.write(" https://www.instagram.com/p/"+media.get_short_code()+"/   ")
        f.write('\n')
        f.write(time_tran(media.get_media_created_time()))
        f.write('\n')
        try:
            comments = instagram.get_media_comments_by_code(media.get_short_code(),10000)
            for comment in comments['comments']:
                name = comment.owner.get_username()
                text = comment.text
                created_time = time_tran(comment.created_at)
                f.write(name+",\""+text+"\","+created_time)
                f.write('\n')
            f.close()
        except Exception as e:
            print(e)
            f.close()
            time.sleep(120)
            continue
        sleeptime = random.randint(30,100)
        time.sleep(sleeptime)
    print("FINSH")
