
import os

folder='/Users/nick/Dropbox/Python/Python Workplace/Tools/pic'



# retrieve the folder then return a list of current files (images in this programme)
def find_names(object):
    for folder,dirnames,file_names in object:
        return file_names

# filter images whos size is less than 3000 (damage image downloaded)
def size_filter(filenames):
    #delete the file whose size is less than 3000 (damaged image)
    for each_image in filenames:
        fileDir=os.path.join(folder,each_image)
        if os.stat(fileDir).st_size < 3000:
            print('deleting file ',each_image)
            os.remove(fileDir)

def rename():
    n=0
    object=os.walk(folder)
    file_names=find_names(object)
    for each in file_names:
        os.renames(folder+'/'+each,folder+'/'+'pic_'+n.__str__()+'.jpg')
        n=n+1

if __name__ == '__main__':
    # Generate the file names
    object = os.walk(folder)
    file_names=find_names(object)

    # filter the files based on their size.
    size_filter(file_names)
    # rename the files, due to the file name's inconsistency after deleting some of the files
    rename()