from context import Instagram # pylint: disable=no-name-in-module
import time

def time_tran(created_at):
    time_local = time.localtime(created_at)
    created_time = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return created_time

instagram = Instagram()
# instagram.with_credentials('JJPtest123', 'jjptest', '/pathtocache')
# instagram.login()

# echo "Number of comments: {$medias[0]->get_comments_count()}\n";
# echo "Fetched: " . count($comments) . "\n";
# or by id
print('begin...')
# media = instagram.get_media_by_url('https://www.instagram.com/p/BhzelQ5lCi2/')
media = instagram.get_media_by_url('https://www.instagram.com/p/BhwuJcmlWh8/')
print('get media success...')
# short_code = media.get_short_code()
# print('short_code: ', short_code)
# id = media.get_id_from_code(short_code)
# print('id: ', id)
# print(media.comments)
f = open('E:\instagram-scraper\examples\data_new\\' + media.get_short_code() +' .csv', 'w', encoding="utf-8")
f.write(" https://www.instagram.com/p/"+media.get_short_code()+"/   ")
f.write('\n')
f.write(time_tran(media.get_media_created_time()))
f.write('\n')
# time.sleep(5)
comments = instagram.get_media_comments_by_code(media.get_short_code(),10000)
for comment in comments['comments']:
    name = comment.owner.get_username()
    text = comment.text
    created_time = time_tran(comment.created_at)
    f.write(name+",\""+text+"\","+created_time)
    f.write('\n')
f.close()
print('finsh...')




# comments = instagram.get_media_comments_by_id(id, 10000)

# for comment in comments['comments']:
#     print(comment.text)
#     print(comment.owner)


# You can start loading comments from specific comment by providing comment id
# comments = instagram.getMediaCommentsByCode('BG3Iz-No1IZ', 200, comment.identifier)
