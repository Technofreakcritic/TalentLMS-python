                       
#   ___  __ _ _ __ ___  
#  / __|/ _` | '_ ` _ \ 
#  \__ \ (_| | | | | | |
#  |___/\__,_|_| |_| |_|
                      
                    
import talentlms

API_KEY = 'xxxxxxxxxxxxxxxxxxx'

lms = talentlms.api('example.talentlms.com', API_KEY)

# try:
#     new_user = lms.user_signup({
#         'email': 'jsmith@example.com',
#         'first': 'John',
#         'last': 'Smith',
#         'login' 'jsmith',
#         'password': 'XXXXXXXXXXXXX'
#     })
#     lms.user_set_status(new_user['id'], 'active')
# except talentlms.UserAlreadyExistsError:
#     pass



# lmfao = lms.add_user_to_course("arshaad.mohiadeen@regentmarket.com", "605", role='learner')
# print(lmfao)

# # Get user status in course
# llll = lms.get_user_status_in_course("656", "132")
# print(llll)


# ---- Get User ID via email id -----

x = input('Employee email id:')
search_user_via_email = lms.users(x)
actual_id = search_user_via_email.get("id")
# print(actual_id)

# ----- Assign course -------
# Current course has been set to Security Data Handling

course_assignment = lms.add_user_to_course(actual_id, "605", role='learner')
print(course_assignment)

# ------ Remove course ------

# rofl = lms.remove_user_from_course(actual_id, "605")



