from context import Instagram # pylint: disable=no-name-in-module
import time

instagram = Instagram()
instagram.with_credentials('JJPtest123', 'jjptest', '/pathtocache')
instagram.login()

# If account is public you can query Instagram without auth

instagram = Instagram()

#f = open('lilmiquela.txt', 'w', encoding="utf-8")

#account_name = input("The account name: ")
#account_post_number = input("The number of post: ")
#medias = instagram.get_medias(account_name, account_post_number)

medias = instagram.get_medias("lil_wavi", 283)

def time_tran(created_at):
    time_local = time.localtime(created_at)
    created_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return created_time

#media = medias[0]
#account = media.owner
#print(account.get_username())

cont = 0

if __name__ == '__main__':
    for media in medias:
        if cont == 283:
            break
        #f = open('lilmiquela No ' + str(cont) +' .csv', 'w')
        f = open('lil_wavi No ' + str(cont) +' .csv', 'w', encoding="utf-8")
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
                f.write(name+","+text+","+created_time)
                f.write('\n')
            #f.write('\n\n\n')
            f.close()
            print(cont)
            time.sleep(35)
            if cont%5 == 0:
                time.sleep(204)
            elif cont%10 == 0:
                time.sleep(155)
            elif cont%40 == 0:
                time.sleep(179)
        except Exception as e:
            print(e)
            time.sleep(301)
            continue
        cont  += 1
    print("FINSH")
