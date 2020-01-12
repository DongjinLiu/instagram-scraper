from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('JJPtest123', 'jjptest', 'path/to/cache/folder')
instagram.login()

media = instagram.get_media_by_id('2143248849565463035')

#not optimal to many calls
tagged_users = instagram.get_media_tagged_users_by_code(media.shortCode)

print(tagged_users)
