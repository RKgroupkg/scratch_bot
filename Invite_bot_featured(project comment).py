import scratchattach as scratch3 # import the library

 
Studio_ID = 33688186 # studio invite link (no) past your studio no

#setup 
session = scratch3.login("Username", "password") # your username and password
studio = session.connect_studio(Studio_ID)
print("Initilized")
# login in scratch

def ID_project (Query): #get id of project
  project = scratch3.featured_projects()
  print("project ID : "+ str(project[Query]['id'])) # prints the project id from which it exracted the user name from comments
  return project[Query]['id']


user_dic = [] # all user name stored from comments 



def Get_trending_comment_user (Quantity): #get treanding user commnets
  global User_data
  inv_total = 0
  for inx_2 in range (int(Quantity/20)):
    project = scratch3.get_project(ID_project(inx_2))
    comments = project.comments(limit=20, offset=0)
    total_users = len(comments)
    for indx in range(total_users):
        inv_total += 1
        if inv_total > Quantity :
           return
        else:
           
          user_dic.append(comments[indx]['author']['username'])
          print(comments[indx]['author']['username'])
          print(inv_total)
          print("\n")


def invite_user (studioID):
  file = open('user.txt','a')
  for indx_2 in user_dic:
    user_inv = indx_2
    print("Invited :")
    print(user_inv) 
    studio.invite_curator(user_inv)
    file.write(str(user_inv)+"\n")
  
  file.close()   

# running parts 
Get_trending_comment_user (280) # insert how much user you want
invite_user(Studio_ID) # studio id from variable
