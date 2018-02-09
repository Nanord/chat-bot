# import sys
# sys.path.append("..")
# import command_system
# from keras.models import Model
# from keras.models import load_model

# def number(photo):
#    get_number(photo)
#    message = 'Цифра: '

#    return message, ''

# info_command = command_system.Command()

# info_command.keys = photo
# info_command.desciption = 'Команды: '
# info_command.process = info




# def get_number(photo):
# 	photo = photo.reshape(1, 28 * 28)
# 	photo = photo.astype('float32')
# 	photo /= 255

# 	model = Model.load_model('model.h5')
# 	model.predict(photo)

	


# def get_random_wall_picture(group_id):
#     max_num = api.photos.get(owner_id=group_id, album_id='wall', count=0)['count']
#     num = random.randint(1, max_num)
#     photo = api.photos.get(owner_id=str(group_id), album_id='wall', count=1, offset=num)['items'][0]['id']
#     attachment = 'photo' + str(group_id) + '_' + str(photo)
#     return attachment