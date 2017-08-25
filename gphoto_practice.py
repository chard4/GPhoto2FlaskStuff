import gphoto2 as gp

context = gp.gp_context_new()
error, camera = gp.gp_camera_new()
print(error)


#simply doing init() causes gphoto2 to autodetect the camera
#if I want to make it more explicit, I need to do set_abilities()
#and apparently set the port too...

'''
error, abilitieslist = gp.gp_abilities_list_new()
print(gp.gp_result_as_string(error))
error = gp.gp_abilities_list_load(abilitieslist, context)
print(gp.gp_result_as_string(error))
index = gp.gp_abilities_list_lookup_model(abilitieslist, 'Nikon DSC D500')
print(index)
error, abilities = gp.gp_abilities_list_get_abilities(abilitieslist, index)
print(gp.gp_result_as_string(error))
error = gp.gp_camera_set_abilities(camera, abilities)
print(gp.gp_result_as_string(error))
'''

#better idea: use autodetect to get a list of vailable cameras
#then look at the list and pick one

#otherwise, if you do the lookup, you need the port too
#the way the sample code did it is as follows:
'''
have a const char *port
and const char *model

context = gp.gp_context_new()
error, camera = gp.gp_camera_new()

error, abilities = gp.gp_abilities_list_new()
error = gp_abilities_list_load(abilities, context)

then look up model and driver
gp_abilities_list_lookup_model()

gp_abilities_list_get_abilities()

gp_camera_set_abilities()

or something

and then do ports.. :(

'''


error = gp.gp_camera_init(camera, context)
print('done with init')
print(gp.gp_result_as_string(error))
#so I'm gonna add in error checks and all that
#but for now assume that the camera is now correctly initialized

#so let's say I want to make it take a picture
capturetype = gp.GP_CAPTURE_IMAGE
error, path = gp.gp_camera_capture(camera, capturetype, context)
print('took image')
print(gp.gp_result_as_string(error))
filetype = gp.GP_FILE_TYPE_NORMAL #http://www.gphoto.org/doc/api/gphoto2-file_8h.html#ab9f339bdf374343272c62d2352753d69
error, file = gp.gp_camera_file_get(camera, path.folder, path.name, filetype, context)
print(gp.gp_result_as_string(error))
error = gp.gp_file_save(file, path.name)
print(gp.gp_result_as_string(error))
error = gp.gp_camera_exit(camera, context)
print(gp.gp_result_as_string(error))