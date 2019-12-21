from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Users
from math import ceil
from django.core.files.storage import FileSystemStorage
import random
import os
from django.shortcuts import redirect


userName = 'User'
userInitials = 'U'
logState = 'LogIn'
userState = 'notasked'
nowUser = None


def index(request):
    global userName, userInitials, logState, userState, userKeys, nowUser
    blogs = Blog.objects.all()
    users = Users.objects.all()
    # print(users)
    noOfBlogs = len(blogs)
    noOfSlides = noOfBlogs//3+ceil(noOfBlogs/3-noOfBlogs//3)
    buttonReceived = request.POST.get('logInButton')
    params = {'blog':blogs,'nblogs':noOfBlogs,'nslides':noOfSlides,'range':range(noOfBlogs), 'userName':userName,'userInitials':userInitials,'userState':userState,'logState':'LogIn'}
    signButton = request.POST.get('signButton')
    print(f"ss is {signButton}")
    if signButton == 'logIn':
        email = request.POST.get('logEmail')
        password = request.POST.get('logPasswd')
        if email == "techroveradmin@techrover.com" and password == "JARVIS":
            nowUser = 'adminUser'
            return render(request,'edit.html',params)
        params['userState'] = 'notFound'
        for user in users:
            print(f"Check all users")
            if user.email == email:
                params['userState'] = 'mismatch'
                print(f'Username is {user.fname}')
                if user.passwd == password:
                    nowUser = user
                    print(f"User complete is {nowUser}")
                    userState = 'check'
                    params['userState'] = userState
                    userName = user.fname
                    params['userName'] = nowUser.fname
                    userInitials = str(str(user.fname)[0] + str(user.lname)[0])
                    params['userInitials'] = nowUser.fname[0] + nowUser.lname[0]
                    logState = 'LogOut'
                    params['logState'] = logState
                    userKeys = list(nowUser.fblogs)
                    print(params['logState'])
                    ###      Redirecting to OTP Page
                    params['fullname'] = nowUser.fname + ' ' + nowUser.lname
                    params['vemail'] = nowUser.email
                    params['vpassword'] = nowUser.passwd
                    params['otp'] = nowUser.verified
                    return render(request,'index.html',params)
    elif signButton == 'signUp':
        notThere = True
        Email = request.POST.get('signEmail')
        print(f"earlier email is {Email}")
        for user in users:
            if user.email == Email:
                notThere = False
                break
        if notThere:
            firstName = request.POST.get('fname')
            lastName = request.POST.get('lname')
            email = request.POST.get('signEmail')
            password = request.POST.get('signPasswd')
            print('first name is {}'.format(firstName))
            print('last name is {}'.format(lastName))
            print('email is {}'.format(email))
            print('password is {}'.format(password))
            otp = random.randrange(1000,9999)
            newUser = Users(fname=firstName,lname=lastName,email=email,passwd=password,verified=str(otp))
            newUser.save()
            nowUser = newUser
            params['userState'] = 'check'
            params['userName'] = nowUser.fname
            params['userInitials'] = str(nowUser.fname[0] + nowUser.lname[0])
            params['logState'] = 'LogOut'
            

        else:
            params['userState'] = 'exist'

    elif request.POST.get('logOutValue') == "out":
        userState = 'notasked'
        userName = 'User'
        userInitials = 'U'
        logState = 'LogIn'
        params['userState'] = userState
        params['userName'] = userName
        params['userInitials'] = userInitials
        params['logState'] = logState
    print(f"Text is {params['logState']}")
    if nowUser != None:
        logState = 'LogIn'
        params['logState'] = logState

    print(f"Userstate is {params['logState']}")
    return render(request,'index.html',params)


def users(request):
    users = Users.objects.all()
    params = {'users':users}
    return render(request,'users.html',params)



def edit(request):
    blogs = Blog.objects.all()
    

    #########################################################
    
    if request.method == "POST" and request.POST.get('newBlog') == 'Upload':
        blogTitle = request.POST.get('blogTitle')
        blogContent = request.POST.get('blogContent')
        print(blogTitle)
        print(blogContent)
        print(request.FILES)
        thisKey = random.randrange(10000,99999)
        keyOK = True
        for blog in blogs:
            if blog.key == thisKey:
                keyOK = False
                break
            else:
                keyOK = True
        while(keyOK == False):
            keyOK = True
            thisKey = random.randrange(10000,99999)
        for blog in blogs:
            if blog.key == thisKey:
                keyOK = False
                break
            else:
                keyOK = True
        print(f"key generated is {thisKey}")


        showImg = request.FILES['showPicker']
        fullImg = request.FILES['fullPicker']
        fs1 = FileSystemStorage()
        fs2 = FileSystemStorage()
        print(f"Extension is {showImg.name[-4:]}")
        showName = str(thisKey)+'_show' + showImg.name[-4:]
        fullName = str(thisKey)+'_full' + fullImg.name[-4:]
        fs1name = fs1.save(showName, showImg)
        fs2name = fs2.save(fullName, fullImg)
        url1 = fs1.url(fs1name)
        url2 = fs2.url(fs2name)
        print(showImg.name)
        print(url1,url2)
        newBlog = Blog(show_img = str(url1),full_img = str(url2),title = blogTitle, content=blogContent, key = thisKey)
        newBlog.save()
        print("Blog saved")


        ################################################################

    if request.method == "POST" and (request.POST.get('oldBlog') == "Save" or request.POST.get('oldBlog') == "Delete"):
        thisKey = request.POST.get('key')
        for blog in blogs:
            if blog.key == thisKey:
                currentBlog = blog
                break
        if request.POST.get('oldBlog') == "Save":
            currentBlog.title = request.POST.get('blogTitle')
            currentBlog.content = request.POST.get('blogContent')
            ss = currentBlog.show_img
            ff = currentBlog.full_img
            try:

                os.remove(ss)
                showImg = request.FILES['showPicker']
                fs1 = FileSystemStorage()
                print(f"Extension is {showImg.name[-4:]}")
                showName = str(thisKey)+'_show' + showImg.name[-4:]
                fs1name = fs1.save(showName, showImg)
                url1 = fs1.url(fs1name)
                print(showImg.name)
                print(url1,url2)
                currentBlog.show_img = str(url1)
                
            except:
                currentBlog.show_img = ss
                print('no show image')

            try:
                os.remove(ff)
                fullImg = request.FILES['fullPicker']
                fs2 = FileSystemStorage()
                fullName = str(thisKey)+'_full' + fullImg.name[-4:]
                fs2name = fs2.save(fullName, fullImg)
                url2 = fs2.url(fs2name)
                currentBlog.full_img = str(url2)
            except:
                currentBlog.full_img = ff
                print('no full image')

            currentBlog.save()

        elif request.POST.get('oldBlog') == "Delete":
            currentBlog.delete();

        ##############################################################
    blogs = Blog.objects.all()
    noOfBlogs = len(blogs)
    noOfSlides = noOfBlogs//4+ceil(noOfBlogs/4-noOfBlogs//4)
    params = {'blog':blogs,'nblogs':noOfBlogs,'nslides':noOfSlides,'range':range(noOfBlogs), 'userName':'Admin','userInitials':'ADM','userState':'check','logState':'LogOut'}

    return render(request,'edit.html',params)

def new(request):
    blogs = Blog.objects.all()

    params = {'userName':'Admin','userInitials':'ADM','userState':'check','logState':'LogOut'}

    return render(request,'newBlog.html',params)
    




def blog(request):
    global userName, userInitials, logState, userState, nowUser
    print(f"Values passed are ")
    for i in request.POST:
        print(i)
    key = request.GET.get('key','default')
    #print(request.GET.get('key'))
    blogs = Blog.objects.all()
    for i in blogs:
        if i.key == key:
            currentBlog = i
            break
    favVal = request.POST.get('isFavorite')
    print(f"favorite is {favVal}")
    setClass = False
    print(f"user is {nowUser}")
    if nowUser != None:
        userKeys = nowUser.fblogs
        print(f"userkeys without list conv are {userKeys}")
        userKeys = eval(userKeys)

        print(f"Userkeys in beginning are {userKeys}")
        if favVal == "True":
            userKeys.append(currentBlog.key)
            userKeys = str(userKeys)
            print(f"userkeys while adding a new blog is {userKeys}")
            nowUser.fblogs = userKeys
            nowUser.save()
            print(f"Saveed the key")
        elif favVal == "False":
            userKeys.remove(currentBlog.key)
            nowUser.fblogs = str(userKeys)
            print(f"userKeys while remobing a blog is {userKeys}")
            nowUser.save()
        if currentBlog.key in userKeys:
            setClass = True
        else:
            setClass = False
        print(f"setclass is {setClass}")
    params = {'title':currentBlog.title,'content':currentBlog.content,'simg':currentBlog.show_img,'fimg':currentBlog.full_img,'userName':userName,'userInitials':userInitials,'logState':logState,'userState':userState,'setClass':setClass}
    return render(request,'blog.html',params)


def all(request):
    blogs = Blog.objects.all();
    params = {'blogs':blogs}
    return render(request,'allblogs.html',params)


def editor(request):
    key = request.GET.get('key')
    blogs = Blog.objects.all()
    for i in blogs:
        if i.key == key:
            currentBlog = i
            break
    params = {'title':currentBlog.title,'content':currentBlog.content,'simg':currentBlog.show_img,'fimg':currentBlog.full_img,'key':currentBlog.key}
    return render(request,'editor.html',params)


###############################################################




def favorite(request):
    global userName, userInitials, logState, userState, userKeys, nowUser
    blogs = Blog.objects.all()
    users = Users.objects.all()
    # print(users)
    csblogs = []
    if nowUser != None:
        favBlogs = eval(nowUser.fblogs)
        print(f"Blogs to be showed are {favBlogs} and its tyle is {type(favBlogs)}")
        for blog in blogs:
            if blog.key in favBlogs:
                csblogs.append(blog)
        blogs = csblogs

    #########################################
    noOfBlogs = len(blogs)
    noOfSlides = noOfBlogs//3+ceil(noOfBlogs/3-noOfBlogs//3)
    buttonReceived = request.POST.get('logInButton')
    params = {'blog':blogs,'nblogs':noOfBlogs,'nslides':noOfSlides,'range':range(noOfBlogs), 'userName':userName,'userInitials':userInitials,'userState':userState,'logState':'LogOut'}
    signButton = request.POST.get('signButton')
    print(f"ss is {signButton}")
    if signButton == 'logIn':
        email = request.POST.get('logEmail')
        password = request.POST.get('logPasswd')
        if email == "techroveradmin@techrover.com" and password == "JARVIS":
            return render(request,'edit.html',params)
        params['userState'] = 'notFound'
        for user in users:
            print(f"Check all users")
            if user.email == email:
                params['userState'] = 'mismatch'
                print(f'Username is {user.fname}')
                if user.passwd == password:
                    nowUser = user
                    print(f"User complete is {nowUser}")
                    userState = 'check'
                    params['userState'] = userState
                    userName = user.fname
                    params['userName'] = userName
                    userInitials = str(str(user.fname)[0] + str(user.lname)[0])
                    params['userInitials'] = userInitials
                    logState = 'LogOut'
                    params['logState'] = logState
                    userKeys = list(user.fblogs)
                    print(params['logState'])
    elif signButton == 'signUp':
        notThere = True
        Email = request.POST.get('signEmail')
        print(f"earlier email is {Email}")
        for user in users:
            if user.email == Email:
                notThere = False
                break
        if notThere:
            firstName = request.POST.get('fname')
            lastName = request.POST.get('lname')
            email = request.POST.get('signEmail')
            password = request.POST.get('signPasswd')
            print('first name is {}'.format(firstName))
            print('last name is {}'.format(lastName))
            print('email is {}'.format(email))
            print('password is {}'.format(password))
            newUser = Users(fname=firstName,lname=lastName,email=email,passwd=password)
            newUser.save()
            params['userState'] = 'check'
            params['userName'] = firstName
            params['userInitials'] = str(firstName[0] + lastName[0])
            params['logState'] = 'Log Out'
        else:
            params['userState'] = 'exist'

    elif request.POST.get('logOutValue') == "out":
        userState = 'notasked'
        userName = 'User'
        userInitials = 'U'
        logState = 'LogIn'
        params['userState'] = userState
        params['userName'] = userName
        params['userInitials'] = userInitials
        params['logState'] = logState
    print(f"Text is {params['logState']}")


    return render(request,'favorite.html',params)


def verify(request):
    global nowUser
    gotEmail = request.GET.get('email')
    gotOTP = request.GET.get('otp')
    users = Users.objects.all()
    for user in users:
        if user.email == gotEmail:
            gotUser = user
            break
    if User.verified == gotOTP:
        user.verified = 'V'
    user.save()
    nowUser = user
    
    # response = redirect('/')
    # return response
    return render(request,'verified.html')


def profile(request):
    pass