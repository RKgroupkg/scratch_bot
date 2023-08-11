import scratchattach as scratch3 # include the library 


#setup 
session = scratch3.login("username", "password") # put your username and password of scratch acc
studio = session.connect_studio(9807652) # studio id link (the no in the link 🔗)
print("Initilized")


def Invite_Caurate(source,studioID):
    file = open('user.txt','a')
   
    #griffpatch followers
    studio = session.connect_studio(studioID)
    user = scratch3.get_user(source)
    for indx in range(int((int(user.follower_count())/40)+1)):
        offset= indx*40
        Follow_user = user.followers(limit=40, offset=offset)
        for indx_2 in range(41):
            idx_user = indx_2-1
            user_inv = Follow_user[idx_user]
            print("Invited :")
            print(user_inv) 
            studio.invite_curator(user_inv) 
            print((indx*40)+indx_2)
            file.write(str(user_inv)+"\n")

    file.close()        
    
    user.follower_names(limit=40, offset=0)




while True :
    Invite_Caurate("griffpatch",483901) # put the username which followers you want to be invited ( i.g:- griffpatch) and studio id link (the no in the link 🔗)



