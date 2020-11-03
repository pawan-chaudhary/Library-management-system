def read_file(unknown):
    file  = open(unknown,"r")
    content  = file.readlines()
    return content
def content_2dlist(unprep):
    db = []
    for i in unprep:
        db.append(i.replace("\n","").split(","))
    return db


