from django.shortcuts import render, get_object_or_404

from studreg.models import *
# Create your views here.
#red --> work -- pycharm -- process syncup -- red

# ddd/edit -- course

def create_edit_new_course(req):
    msg = ''
    if req.method == 'POST':
        formdata = req.POST
        print('inside post method--',formdata)
       # cr = Courses.objects.filter(id=int(formdata['id'])).first()
        cr = Courses.objects.get()
        print(cr)
        if cr:
            cr.name = formdata['crname']
            cr.fees = formdata['crfees']
            cr.code = formdata['crcode']
            msg = "Course Record Updated"

        else:
            msg = "New Course Added..."
            cr = Courses(
                name=formdata['crname'],
                fees=formdata['crfees'],
                code=formdata['crcode'],
                duration=formdata['crdur'])
        cr.save()

        courselist = Courses.objects.all()
        # print("\n\t", type(courselist),"type of list")
        # print("\n\t", dir(courselist), "the directorry is")
        # print("\n\t", id(courselist), "the id is")
        for i in courselist:
            print("\n\t", i.name)



    return render(req,'course.html',{"resp":msg,
                                     "cr" : Courses.get_empty_course(),
                                     "crlist": Courses.objects.filter(active='Y')})

#once user clicks on edit--> want to papulate values inside form
def fetch_course_info(req,crid):

    return render(req, 'course.html', {
                                       "cr": Courses.objects.get(id=crid),
                                       "crlist": Courses.objects.filter(active='Y')})


# once user clicks on delete --> want soft delete course record
def delete_course_info(req,crid):
    dbcr = Courses.objects.get(id=crid)
    msg = ''
    if dbcr:
        dbcr.active='N'
        dbcr.save()
        msg = 'Course deleted...!'
    return render(req, 'course.html', {"resp": msg,
                                       "cr": Courses.get_empty_course(),
                                       "crlist": Courses.objects.filter(active='Y')})


def create_edit_new_student(req):
    msg = ''
    if req.method=='POST':
        formdata = req.POST
        stud = Student.objects.filter(id=int(formdata['sid'])).first()
        if stud:
            msg ="Updated"
            stud.fname = formdata['sfnm']
            stud.lname = formdata['slnm']
            stud.email = formdata['semail']
        else:
            msg = "Added"


    return render(req, 'stud.html', {"resp": msg,
                                       "cr": Courses.get_empty_course(),
                                       "crlist": Courses.objects.filter(active='Y')})


def fetch_student_info(req):
    return render(req, 'course.html', {"resp": msg,
                                       "cr": Courses.get_empty_course(),
                                       "crlist": Courses.objects.filter(active='Y')})


def delete_student_info(req):
    return render(req, 'course.html', {"resp": msg,
                                       "cr": Courses.get_empty_course(),
                                       "crlist": Courses.objects.filter(active='Y')})
