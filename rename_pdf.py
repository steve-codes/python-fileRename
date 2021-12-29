from os import getcwd, chdir, rename
from glob import glob as glob

# the name of the file directory where the pdfs are stored
directory = 'PDF_FILES'

# the file extension of the doucments we want to rename
# in this case we are trying to change "pdf" file names
extension = 'pdf'

# the character we split the old name off of
# for example filename: TESTINGNEWSYSTEM_Jan_02_2019
# we want to remove "TESTINGNEWSYSTEM" so we split on "_"
splitOn = '_'

# the new text that will replace "TESTINGNEWSYSTEM" in the above example
newName = 'DAVE-INC'

# grabs the current directory path
currDir = getcwd()

# change directory to the "directory variable"
chdir(directory)

# grabs all PDF files in the directory 
# we swtiched to
pdf_list = glob('*.' + extension)

# iterate over our PDF list. pdf is a pdf filename
for pdf in pdf_list:
    # split the string using our splitOn variable "_"
    # on the first occurence of it (prevents multiple splits)
    strSplit = pdf.split(splitOn, 1)

    # construct the new filename (remember to replace the "_" we split on)
    # strSplit[1] is "Jan_02_2019" from the example on line 12
    newFileName = newName + splitOn + strSplit[1]

    # call the rename command to rename the PDF file
    rename(pdf, newFileName)